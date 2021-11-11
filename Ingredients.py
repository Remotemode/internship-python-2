import sqlite3

import sqlite3


class Ingredients:
    def __init__(self):
        try:
            self.sqlite_connection = sqlite3.connect('Cookie.db')
            self.cursor = self.sqlite_connection.cursor()
            print("База данных создана и успешно подключена к SQLite")
            record = self.cursor.fetchall()
            print("Версия базы данных SQLite: ", record)
            return
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

    def get_all_ingredients(self):
        sqlite_select_query = "SELECT * from Ingredients"
        for row in self.cursor.execute(sqlite_select_query):
            print(row)
        total_rows = self.cursor.fetchone()
        print('get_all_Ingredients')

    def insert_ingredients(self, name, count, price):
        sqlite_insert_query = "INSERT INTO Ingredients (name, count, price) VALUES (?, ?, ?)";
        value = [name, count, price];
        self.cursor.execute(sqlite_insert_query, value)
        total_rows = self.cursor.fetchone()
        self.sqlite_connection.commit()
        print('insert_ingredients')

    def delete_ingredients(self, id):
        sql_delete_query = "DELETE from Ingredients where id_ingredient = ?"
        value = [id];
        self.cursor.execute(sql_delete_query, value)
        self.sqlite_connection.commit()
        print("delete_ingredients")

    def update_ingredients(self, name, price):
        sql_update_query = "Update Ingredients set price = ? where name = ?"
        value = [price, name];
        self.cursor.execute(sql_update_query, value)
        self.sqlite_connection.commit()
        print("update_ingredients")

    def end(self):
        if (self.sqlite_connection):
            self.sqlite_connection.close()
            print("Соединение с SQLite закрыто")