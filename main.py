from db import DB
import tkinter as tk
from tkinter import messagebox, END

db = DB()
root = tk.Tk()

button_style = {"bg": "lightblue", "fg": "black", "font": ("Arial", 12)}
label_style = {"bg": "lightgray", "fg": "black", "font": ("Arial", 12)}


def view_command():
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, row)


def add_command():
    db.insert(product_text.get(), price_text.get(), comment_text.get())
    view_command()


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]  # Это ID выбранного кортежа
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])


def search_command():
    list1.delete(0, END)
    for row in db.search(product_text.get()):
        list1.insert(END, row)


def delete_command():
    db.delete(selected_tuple[0])
    view_command()


def update_command():
    db.update(selected_tuple[0], product_text.get(), price_text.get())
    view_command()


def on_closing():
    if messagebox.askokcancel("", "Закрыть программу?"):
        root.destroy()


# Создание ярлыков
l1 = tk.Label(root, text="Название",**label_style)
l1.grid(row=0, column=0)
l2 = tk.Label(root, text="Стоимость",**label_style)
l2.grid(row=0, column=2)
l3 = tk.Label(root, text="Комментарий",**label_style)
l3.grid(row=1, column=0)

# Создание поля для ввода
product_text = tk.StringVar()
e1 = tk.Entry(root, textvariable=product_text)
e1.grid(row=0, column=1)
price_text = tk.StringVar()
e2 = tk.Entry(root, textvariable=price_text)
e2.grid(row=0, column=3)
comment_text = tk.StringVar()
e3 = tk.Entry(root, textvariable=comment_text)
e3.grid(row=1, column=1)

# Создание поля со списком
list1 = tk.Listbox(root, height=25, width=65)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
sb1 = tk.Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Создание кнопок
b1 = tk.Button(
    root, text="Посмотреть все", width=12, command=view_command, **button_style
)
b1.grid(row=2, column=3)
b2 = tk.Button(root, text="Поиск", width=12, command=search_command, **button_style)
b2.grid(row=3, column=3)
b3 = tk.Button(root, text="Добавить", width=12, command=add_command, **button_style)
b3.grid(row=4, column=3)
b4 = tk.Button(root, text="Обновить", width=12, command=update_command, **button_style)
b4.grid(row=5, column=3)
b5 = tk.Button(root, text="Удалить", width=12, command=delete_command, **button_style)
b5.grid(row=6, column=3)
b6 = tk.Button(root, text="Закрыть", width=12, command=on_closing, **button_style)
b6.grid(row=7, column=3)

# Привязать событие выбора поля списка
list1.bind("<<ListboxSelect>>", get_selected_row)

# Инициализация представления
view_command()

root.mainloop()
