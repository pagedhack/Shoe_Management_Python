from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Shoe:
    def __init__(self, model, size, numbers, color, stock, code):
        self.model = model
        self.size = size
        self.numbers = numbers
        self.color = color
        self.stock = stock
        self.code = code

class Menu:
    def __init__(self, window):
        self.window = window
        self.window.title("Menu")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.register = Button(self.window, text="Register", command=self.register)
        self.register.place(x=100, y=50)

        self.delete = Button(self.window, text="Delete", command=self.delete)
        self.delete.place(x=100, y=100)

        self.modify = Button(self.window, text="Modify", command=self.modify)
        self.modify.place(x=100, y=150)

        self.show = Button(self.window, text="Show", command=self.show)
        self.show.place(x=100, y=200)

        self.exit = Button(self.window, text="Exit", command=self.window.destroy)
        self.exit.place(x=100, y=250)

    def register(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Register")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.model = Entry(self.window)
        self.model.place(x=100, y=50)
        self.model.focus()

        self.size = Entry(self.window)
        self.size.place(x=100, y=100)

        self.numbers = Entry(self.window)
        self.numbers.place(x=100, y=150)

        self.color = Entry(self.window)
        self.color.place(x=100, y=200)

        self.stock = Entry(self.window)
        self.stock.place(x=100, y=250)

        self.register = Button(self.window, text="Register", command=self.register_shoe)
        self.register.place(x=100, y=300)

        self.back = Button(self.window, text="Back", command=self.back)
        self.back.place(x=200, y=300)

    def register_shoe(self):
        model = self.model.get()
        size = self.size.get()
        numbers = self.numbers.get()
        color = self.color.get()
        stock = self.stock.get()
        code = model[0:3] + size[0:3] + numbers[0:3] + color[0:3] + stock[0:3]

        if model == "" or size == "" or numbers == "" or color == "" or stock == "":
            messagebox.showwarning("Warning", "All fields are required")
        else:
            try:
                query = "INSERT INTO shoes VALUES(%s, %s, %s, %s, %s, %s)"
                values = (model, size, numbers, color, stock, code)
                cursor.execute(query, values)
                connection.commit()
                messagebox.showinfo("Success", "Shoe registered")
            except:
                messagebox.showwarning("Warning", "Shoe already registered")

    def delete(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Delete")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.code = Entry(self.window)
        self.code.place(x=100, y=50)
        self.code.focus()

        self.delete = Button(self.window, text="Delete", command=self.delete_shoe)
        self.delete.place(x=100, y=100)

        self.back = Button(self.window, text="Back", command=self.back)
        self.back.place(x=200, y=100)

    def delete_shoe(self):
        code = self.code.get()

        if code == "":
            messagebox.showwarning("Warning", "Code field is required")
        else:
            try:
                query = "DELETE FROM shoes WHERE code = %s"
                values = (code,)
                cursor.execute(query, values)
                connection.commit()
                messagebox.showinfo("Success", "Shoe deleted")
            except:
                messagebox.showwarning("Warning", "Shoe not found")

    def modify(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Modify")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.code = Entry(self.window)
        self.code.place(x=100, y=50)
        self.code.focus()

        self.model = Entry(self.window)
        self.model.place(x=100, y=100)

        self.size = Entry(self.window)
        self.size.place(x=100, y=150)

        self.numbers = Entry(self.window)
        self.numbers.place(x=100, y=200)

        self.color = Entry(self.window)
        self.color.place(x=100, y=250)

        self.stock = Entry(self.window)
        self.stock.place(x=100, y=300)

        self.modify = Button(self.window, text="Modify", command=self.modify_shoe)
        self.modify.place(x=100, y=350)

        self.back = Button(self.window, text="Back", command=self.back)
        self.back.place(x=200, y=350)

    def modify_shoe(self):
        code = self.code.get()
        model = self.model.get()
        size = self.size.get()
        numbers = self.numbers.get()
        color = self.color.get()
        stock = self.stock.get()

        if code == "":
            messagebox.showwarning("Warning", "Code field is required")
        else:
            try:
                query = "UPDATE shoes SET model = %s, size = %s, numbers = %s, color = %s, stock = %s WHERE code = %s"
                values = (model, size, numbers, color, stock, code)
                cursor.execute(query, values)
                connection.commit()
                messagebox.showinfo("Success", "Shoe modified")
            except:
                messagebox.showwarning("Warning", "Shoe not found")

    def show(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Show")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.tree = ttk.Treeview(self.window, height=10, columns=("model", "size", "numbers", "color", "stock", "code"))
        self.tree.place(x=0, y=0)
        self.tree.heading("#0", text="Model")
        self.tree.heading("#1", text="Size")
        self.tree.heading("#2", text="Numbers")
        self.tree.heading("#3", text="Color")
        self.tree.heading("#4", text="Stock")
        self.tree.heading("#5", text="Code")

        self.back = Button(self.window, text="Back", command=self.back)
        self.back.place(x=200, y=250)

        self.show_shoes()

    def show_shoes(self):
        query = "SELECT * FROM shoes"
        cursor.execute(query)
        shoes = cursor.fetchall()
        for shoe in shoes:
            self.tree.insert("", 0, text=shoe[0], values=(shoe[1], shoe[2], shoe[3], shoe[4], shoe[5]))

    def back(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Menu")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.register = Button(self.window, text="Register", command=self.register)
        self.register.place(x=100, y=50)

        self.delete = Button(self.window, text="Delete", command=self.delete)
        self.delete.place(x=100, y=100)

        self.modify = Button(self.window, text="Modify", command=self.modify)
        self.modify.place(x=100, y=150)

        self.show = Button(self.window, text="Show", command=self.show)
        self.show.place(x=100, y=200)

        self.exit = Button(self.window, text="Exit", command=self.window.destroy)
        self.exit.place(x=100, y=250)

class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("Login")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.username = Entry(self.window)
        self.username.place(x=100, y=50)
        self.username.focus()

        self.password = Entry(self.window)
        self.password.place(x=100, y=100)

        self.login = Button(self.window, text="Login", command=self.login)
        self.login.place(x=100, y=150)

        self.register = Button(self.window, text="Register", command=self.register)
        self.register.place(x=200, y=150)

        self.exit = Button(self.window, text="Exit", command=self.window.destroy)
        self.exit.place(x=100, y=200)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
            messagebox.showwarning("Warning", "All fields are required")
        else:
            try:
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                values = (username, password)
                cursor.execute(query, values)
                user = cursor.fetchone()
                if user[0] == username and user[1] == password:
                    self.window.destroy()
                    self.window = Tk()
                    self.window.title("Menu")
                    self.window.geometry("300x300")
                    self.window.config(bg="white")
                    self.window.resizable(0,0)

                    self.register = Button(self.window, text="Register", command=self.register)
                    self.register.place(x=100, y=50)

                    self.delete = Button(self.window, text="Delete", command=self.delete)
                    self.delete.place(x=100, y=100)

                    self.modify = Button(self.window, text="Modify", command=self.modify)
                    self.modify.place(x=100, y=150)

                    self.show = Button(self.window, text="Show", command=self.show)
                    self.show.place(x=100, y=200)

                    self.exit = Button(self.window, text="Exit", command=self.window.destroy)
                    self.exit.place(x=100, y=250)
                else:
                    messagebox.showwarning("Warning", "Username or password incorrect")
            except:
                messagebox.showwarning("Warning", "Username or password incorrect")

    def register(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Register")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.username = Entry(self.window)
        self.username.place(x=100, y=50)
        self.username.focus()

        self.password = Entry(self.window)
        self.password.place(x=100, y=100)

        self.register = Button(self.window, text="Register", command=self.register_user)
        self.register.place(x=100, y=150)

        self.back = Button(self.window, text="Back", command=self.back)
        self.back.place(x=200, y=150)

    def register_user(self):
        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
            messagebox.showwarning("Warning", "All fields are required")
        else:
            try:
                query = "INSERT INTO users VALUES(%s, %s)"
                values = (username, password)
                cursor.execute(query, values)
                connection.commit()
                messagebox.showinfo("Success", "User registered")
            except:
                messagebox.showwarning("Warning", "User already registered")

    def back(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.window.resizable(0,0)

        self.username = Entry(self.window)
        self.username.place(x=100, y=50)
        self.username.focus()

        self.password = Entry(self.window)
        self.password.place(x=100, y=100)

        self.login = Button(self.window, text="Login", command=self.login)
        self.login.place(x=100, y=150)

        self.register = Button(self.window, text="Register", command=self.register)
        self.register.place(x=200, y=150)

        self.exit = Button(self.window, text="Exit", command=self.window.destroy)
        self.exit.place(x=100, y=200)

if __name__ == "__main__":
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="shoes")
    cursor = connection.cursor()
    window = Tk()
    login = Login(window)
    window.mainloop()
