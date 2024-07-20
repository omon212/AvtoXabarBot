import sqlite3

connect = sqlite3.connect('data.db')
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS xabarlar (id INTEGER PRIMARY KEY,user_id INTEGER,xabar TEXT,vaqt TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS grupalar (id INTEGER PRIMARY KEY,group_id INTEGER, group_name TEXT)")
connect.commit()


async def save_all_data(user_id, xabar, vaqt):
    a = cursor.execute("SELECT * FROM xabarlar WHERE user_id = ?", (user_id,)).fetchall()
    if a == []:
        cursor.execute("INSERT INTO xabarlar (user_id,xabar,vaqt) VALUES (?,?,?)", (user_id, xabar, vaqt))
        connect.commit()
    else:
        cursor.execute("UPDATE xabarlar SET xabar = ?, vaqt = ? WHERE user_id = ?", (xabar, vaqt, user_id))
        connect.commit()


async def save_group_data(group_id, group_name):
    cursor.execute("INSERT INTO grupalar (group_id,group_name) VALUES (?,?)", (group_id, group_name))
    connect.commit()


async def delete_group(id):
    cursor.execute("DELETE FROM grupalar WHERE group_id = ?", (id,))
    connect.commit()


async def get_group():
    a = cursor.execute("SELECT * FROM grupalar").fetchall()
    return a


async def get_xabar(user_id):
    a = cursor.execute("SELECT * FROM xabarlar WHERE user_id = ?", (user_id,)).fetchall()
    return a
