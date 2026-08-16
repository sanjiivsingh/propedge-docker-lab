CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE account (
    id INTEGER PRIMARY KEY,
    account_name TEXT NOT NULL,
    starting_balance NUMERIC(12,2) NOT NULL
);

CREATE TABLE ingested_trades (
    source_id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    side TEXT NOT NULL,
    entry_price NUMERIC(14,4) NOT NULL,
    exit_price NUMERIC(14,4) NOT NULL,
    quantity NUMERIC(12,4) NOT NULL,
    pnl NUMERIC(12,2) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

INSERT INTO users (username,password) VALUES ('trader','trader123');
INSERT INTO account (id,account_name,starting_balance) VALUES (1,'DEMO-50000',50000.00);
