import sqlite3
banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()
#cursor.execute ("CREATE TABLE Cursos (id integer, nome text, instituição text)")

#cursor.execute("INSERT INTO Cursos VALUES(01,'Desenvolvedor Mobile', 'SENAI')")
#cursor.execute("INSERT INTO Cursos VALUES(02,'Culinária', 'SENAI')")
#cursor.execute("INSERT INTO Cursos VALUES(03,'Engenharia Elétrica', 'SENAI')")
#cursor.execute("INSERT INTO Cursos VALUES(04,'Engenharia Mecânica', 'SENAI')")
#cursor.execute("INSERT INTO Cursos VALUES(05,'Automação Industrial', 'SENAI')")

banco.commit()

cursor.execute("SELECT * FROM Cursos")
print(cursor.fetchall())




