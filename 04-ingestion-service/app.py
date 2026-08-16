import os,time,threading,requests,psycopg2
from flask import Flask,jsonify

app=Flask(__name__)
TRADING_URL=os.getenv("TRADING_URL","http://trading-app:5002")
POLL_INTERVAL=int(os.getenv("POLL_INTERVAL","3"))

def db():
    return psycopg2.connect(host=os.getenv("DB_HOST","db"),
        database=os.getenv("DB_NAME","trading"),
        user=os.getenv("DB_USER","trader"),
        password=os.getenv("DB_PASSWORD","traderpass"))

def sync_once():
    conn=db()
    try:
        with conn.cursor() as c:
            c.execute("SELECT COALESCE(MAX(source_id),0) FROM ingested_trades")
            last_id=int(c.fetchone()[0])

        r=requests.get(f"{TRADING_URL}/api/trades",params={"after_id":last_id},timeout=3)
        r.raise_for_status()
        trades=r.json()["trades"]
        inserted=0

        with conn.cursor() as c:
            for t in trades:
                c.execute("""
                    INSERT INTO ingested_trades
                    (source_id,symbol,side,entry_price,exit_price,quantity,pnl)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (source_id) DO NOTHING
                """,(t["id"],t["symbol"],t["side"],t["entry_price"],
                     t["exit_price"],t["quantity"],t["pnl"]))
                inserted+=c.rowcount
        conn.commit()
        return {"fetched":len(trades),"inserted":inserted}
    finally:
        conn.close()

def polling_loop():
    while True:
        try:
            result=sync_once()
            if result["fetched"]:
                print(f"Fetched={result['fetched']} Inserted={result['inserted']}",flush=True)
        except Exception as exc:
            print(f"Ingestion retry: {exc}",flush=True)
        time.sleep(POLL_INTERVAL)

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/sync")
def sync():
    try:
        return jsonify(sync_once())
    except Exception as exc:
        return jsonify({"error":str(exc)}),503

threading.Thread(target=polling_loop,daemon=True).start()
app.run(host="0.0.0.0",port=5001)
