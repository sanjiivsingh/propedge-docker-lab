import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST","db"),
        database=os.getenv("DB_NAME","trading"),
        user=os.getenv("DB_USER","trader"),
        password=os.getenv("DB_PASSWORD","traderpass"))

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/api/login")
def login():
    data=request.get_json(force=True)
    conn=db()
    try:
        with conn.cursor() as c:
            c.execute("SELECT id FROM users WHERE username=%s AND password=%s",
                      (data.get("username",""),data.get("password","")))
            ok=c.fetchone() is not None
        return jsonify({"authenticated":ok}), (200 if ok else 401)
    finally:
        conn.close()

@app.get("/api/dashboard")
def dashboard():
    conn=db()
    try:
        with conn.cursor() as c:
            c.execute("SELECT starting_balance FROM account WHERE id=1")
            starting=float(c.fetchone()[0])
            c.execute("SELECT COALESCE(SUM(pnl),0),COUNT(*),COUNT(*) FILTER (WHERE pnl>0) FROM ingested_trades")
            pnl,total,wins=c.fetchone()
            pnl,total,wins=float(pnl),int(total),int(wins)
            c.execute("SELECT COALESCE(SUM(pnl),0) FROM ingested_trades WHERE created_at::date=CURRENT_DATE")
            daily=float(c.fetchone()[0])
            c.execute("SELECT pnl FROM ingested_trades ORDER BY source_id")
            curve_rows=[float(x[0]) for x in c.fetchall()]
            c.execute("SELECT symbol,side,entry_price,exit_price,pnl FROM ingested_trades ORDER BY source_id DESC LIMIT 10")
            rows=c.fetchall()

        balance=starting+pnl
        win_rate=wins/total*100 if total else 0
        drawdown=max(0,starting-balance)
        status="FAILED" if daily<=-1000 or drawdown>=2500 else "PASSING"
        curve=[starting]; current=starting
        for x in curve_rows:
            current+=x; curve.append(current)

        return jsonify({
            "balance":balance,"total_pnl":pnl,"daily_pnl":daily,
            "win_rate":win_rate,"total_trades":total,"drawdown":drawdown,
            "status":status,"equity_curve":curve,
            "recent_trades":[
                {"symbol":r[0],"side":r[1],"entry_price":float(r[2]),
                 "exit_price":float(r[3]),"pnl":float(r[4])} for r in rows
            ]})
    finally:
        conn.close()

app.run(host="0.0.0.0",port=5000)
