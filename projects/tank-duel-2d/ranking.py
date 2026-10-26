"""Chỉ trận xếp hạng được phép gọi record_match."""
import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("ranking.db")


def rank(points):
    for minimum, name in ((1000, "Huyền Thoại"), (700, "Kim Cương"),
                          (450, "Bạch Kim"), (250, "Vàng"), (100, "Bạc")):
        if points >= minimum:
            return name
    return "Đồng"


def connect():
    db = sqlite3.connect(DB)
    db.execute("""CREATE TABLE IF NOT EXISTS players (
        name TEXT PRIMARY KEY COLLATE NOCASE, matches INTEGER NOT NULL DEFAULT 0,
        wins INTEGER NOT NULL DEFAULT 0, losses INTEGER NOT NULL DEFAULT 0,
        points INTEGER NOT NULL DEFAULT 0)""")
    db.execute("""CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT, played_at TEXT NOT NULL DEFAULT (datetime('now','localtime')),
        player1 TEXT NOT NULL, player2 TEXT NOT NULL, winner TEXT,
        old1 INTEGER NOT NULL, delta1 INTEGER NOT NULL, new1 INTEGER NOT NULL,
        old2 INTEGER NOT NULL, delta2 INTEGER NOT NULL, new2 INTEGER NOT NULL)""")
    return db


def leaderboard():
    with connect() as db:
        return db.execute("SELECT name,matches,wins,losses,points FROM players "
                          "ORDER BY points DESC,wins DESC,name COLLATE NOCASE LIMIT 12").fetchall()


def recent_matches():
    with connect() as db:
        return db.execute("SELECT played_at,player1,player2,winner,delta1,delta2 "
                          "FROM history ORDER BY id DESC LIMIT 12").fetchall()


def record_match(names, winner):
    """winner: 0, 1 hoặc None (hòa). Giao dịch lưu cả hai cùng lúc."""
    if names[0].strip().casefold() == names[1].strip().casefold():
        raise ValueError("Hai tên phải khác nhau")
    results = []
    with connect() as db:
        for i, name in enumerate(names):
            db.execute("INSERT OR IGNORE INTO players(name) VALUES (?)", (name,))
            old = db.execute("SELECT points FROM players WHERE name=? COLLATE NOCASE", (name,)).fetchone()[0]
            delta = 0 if winner is None else (20 if winner == i else -10)
            new = max(0, old + delta)
            db.execute("UPDATE players SET matches=matches+1,wins=wins+?,losses=losses+?,points=? "
                       "WHERE name=? COLLATE NOCASE", (int(winner == i), int(winner is not None and winner != i), new, name))
            results.append((name, old, delta, new, rank(new)))
        db.execute("INSERT INTO history(player1,player2,winner,old1,delta1,new1,old2,delta2,new2) "
                   "VALUES (?,?,?,?,?,?,?,?,?)",
                   (names[0], names[1], None if winner is None else names[winner],
                    results[0][1], results[0][2], results[0][3],
                    results[1][1], results[1][2], results[1][3]))
    return results
