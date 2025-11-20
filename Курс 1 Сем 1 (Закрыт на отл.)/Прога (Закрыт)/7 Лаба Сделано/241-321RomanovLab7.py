# -*- coding: UTF-8 -*-
from tkinter import *
import json

class Product:
    def __init__(self, name, store, price, quantity):
        self.name = name
        self.store = store
        self.price = price
        self.quantity = quantity

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.products = []
        self.create_widgets()

    def create_widgets(self):
        # Создание интерфейса для ввода нового товара
        self.name_label = Label(self, text="Название товара:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = Entry(self)
        self.name_entry.grid(row=0, column=1)

        self.store_label = Label(self, text="Название магазина:")
        self.store_label.grid(row=1, column=0)
        self.store_entry = Entry(self)
        self.store_entry.grid(row=1, column=1)

        self.price_label = Label(self, text="Стоимость (тыс. руб.):")
        self.price_label.grid(row=2, column=0)
        self.price_entry = Entry(self)
        self.price_entry.grid(row=2, column=1)

        self.quantity_label = Label(self, text="Количество:")
        self.quantity_label.grid(row=3, column=0)
        self.quantity_entry = Entry(self)
        self.quantity_entry.grid(row=3, column=1)

        self.add_button = Button(self, text="Добавить товар", command=self.add_product)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.sort_button = Button(self, text="Сортировать по названию", command=self.sort_products)
        self.sort_button.grid(row=5, column=0, columnspan=2)

        self.search_label = Label(self, text="Введите название товара для поиска:")
        self.search_label.grid(row=6, column=0)
        self.search_entry = Entry(self)
        self.search_entry.grid(row=6, column=1)

        self.search_button = Button(self, text="Поиск", command=self.search_product)
        self.search_button.grid(row=7, column=0, columnspan=2)

        self.save_button = Button(self, text="Сохранить в файл", command=self.save_to_file)
        self.save_button.grid(row=8, column=0, columnspan=2)

        self.output_label = Label(self, text="")
        self.output_label.grid(row=9, column=0, columnspan=2)

    def add_product(self):
        name = self.name_entry.get()
        store = self.store_entry.get()
        price = float(self.price_entry.get())
        quantity = self.quantity_entry.get()
        product = Product(name, store, price, quantity)
        self.products.append(product)
        self.output_label.config(text=f"Товар '{name}' добавлен.")

    def sort_products(self):
        self.products.sort(key=lambda x: x.name)  # Сортировка по названию товара
        self.output_label.config(text="Список товаров отсортирован.")

    def search_product(self):
        name = self.search_entry.get()
        for product in self.products:
            if product.name == name:
                self.output_label.config(text=f"Товар: {product.name}, Магазин: {product.store}, Цена: {product.price} тыс. руб., Количество: {product.quantity}")
                return
        self.output_label.config(text="Товар не найден.")

    def save_to_file(self):
        filename = "products.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([p.__dict__ for p in self.products], f, ensure_ascii=False)
        self.output_label.config(text=f"Список сохранен в файл '{filename}'.")

root = Tk()
root.title("Управление списком товаров")
app = Application(master=root)
root.mainloop()
