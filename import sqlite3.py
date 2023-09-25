import sqlite3
banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

cursor.execute("UPDATE Cursos SET nome = 'Estética' WHERE id = 4")
cursor.execute("DELETE FROM Cursos WHERE id = 5")
banco.commit()
banco.close()
