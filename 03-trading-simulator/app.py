import random
from flask import Flask, jsonify, request, send_file

app=Flask(__name__)
trades=[]

def make_trade(mode):
    symbol=random.choice(["XAUUSD","BTCUSD","EURUSD"])
    side=random.choice(["BUY","SELL"])
    entry=round(random.uniform(3300,3400),2)
    pnl=round(random.uniform(50,250),2) if mode=="win" else round(random.uniform(-250,-50),2) if mode=="loss" else round(random.uniform(-250,250),2)
    trade={"id":len(trades)+1,"symbol":symbol,"side":side,"entry_price":entry,
           "exit_price":round(entry+pnl/10,2),"quantity":0.10,"pnl":pnl}
    trades.append(trade)
    return trade

@app.get("/")
def home():
    return send_file("index.html")

@app.get("/api/trades")
def get_trades():
    after_id=int(request.args.get("after_id",0))
    return jsonify({"trades":[t for t in trades if t["id"]>after_id]})

@app.post("/api/generate/random")
def random_trade():
    return jsonify(make_trade("random"))

@app.post("/api/generate/win")
def winning_trade():
    return jsonify(make_trade("win"))

@app.post("/api/generate/loss")
def losing_trade():
    return jsonify(make_trade("loss"))

app.run(host="0.0.0.0",port=5002)
