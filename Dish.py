import sqlite3


class Dish:
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

    def get_all(self):
        sqlite_select_query = "SELECT * from Dish"
        self.cursor.execute(sqlite_select_query)
        total_rows = self.cursor.fetchone()
        print('get_all')

    def insert_dish(self, name, quantity, price):
        sqlite_insert_query = "INSERT INTO Dish (name, quantity, price) VALUES (?, ?, ?)";
        value = [name, quantity, price];
        self.cursor.execute(sqlite_insert_query, value)
        total_rows = self.cursor.fetchone()
        print('insert_dish')

    def end(self):
        if (self.sqlite_connection):
            self.sqlite_connection.close()
            print("Соединение с SQLite закрыто")

    def delete_dish(self, id):
        sql_delete_query = "DELETE from Dish where id_dish = ?"
        value = [id];
        self.cursor.execute(sql_delete_query, value)
        print("delete_dish")

    def update_dish(self, name, price):
        sql_update_query = "Update Dish set price = ? where name = ?"
        value = [price, name];
        self.cursor.execute(sql_update_query, value)
        print("update_dish")
    
        




