import sqlite3


conn = sqlite3.connect("university.db")
cursor = conn.cursor()

conn.commit()
cursor.execute("INSERT  INTO users (name, email, age, country) VALUES (?, ?, ?, ?)", ("Сергей", "raserzh09@gmail.com",
                                                                                      26,  "Беларусь"))
print("✅ Данные о новом пользователе вставлены в таблицу")
cursor.execute("SELECT * FROM users WHERE country = ?", ("Беларусь",))
rows = cursor.fetchall()
for row in rows:
    print(row)
    assert row[1] == "Сергей"
conn.commit()

cursor.execute("DELETE FROM users WHERE name = ?", ("Сергей",))
print("✅ Данные о пользователе удалены")
conn.commit()