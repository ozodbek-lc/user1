from cars_data import create_data  # cars_data dan create_data funksiyasini cars_curdga import qilish
import os
import json
import re

def cars_crud():
    while True:
        cars = {}
        status = input("Qo'shish uchun 1 : \nO'chirish uchun 2 : \nMashina modelini va rangini o'zgartirish 3 : \nChiqish uchun 4 : \nYozing : ")

        if status == "1":
            if os.path.exists("cars_data.json"):
                try:
                    cars = create_data(None, "cars_data.json", "r")
                except Exception as e:
                    print(e)

            # Mashina raqamini aniqlash
            while True:
                car_number = input("Mashinani davlat raqamini kiriting : ")
                if re.match(r'^\d{2}[A-Z]{1}\d{3}[A-Z]{2}$', car_number):  # Mashina raqamini tekshirish uchun
                    cars[car_number] = {}
                    break
                else:
                    print("Bunday nomer mavjud emas (01X123XX) namuna ko'rinishi bo'lishi kerak.")

            color = input("Mashinani rangini kiriting : ")
            model = input("Mashina modelini kiriting : ")
            cars[car_number] = {
                "color": color,
                "model": model
            }
            create_data(cars, "cars_data.json", "w")
            print("<<<Malumot muvofiaqiatli qoshildi>>>")

        elif status == "2":
            if os.path.exists("cars_data.json"):
                try:
                    cars = create_data(None, "cars_data.json", "r")
                except Exception as e:
                    print(e)

                car_number = input("O'chirmoqchi bo'lgan raqamni kiriting: ")
                if car_number in cars:
                    cars.pop(car_number)
                    print("Amaliyot muvaffaqiyatli bajarildi")
                    create_data(cars, "cars_data.json", "w")
                else:
                    print("Kiritilgan raqam mavjud emas.")

        elif status == "3":
            if os.path.exists("cars_data.json"):
                try:
                    cars = create_data(None, "cars_data.json", "r")
                except Exception as e:
                    print(e)

                car_number = input("Modeli va rangini o'zgartirmoqchi bo'lgan mashina raqamini kiriting : ")
                if car_number in cars:
                    color = input("Yangi mashina rangini kiriting : ")
                    model = input("Yangi mashina modelini kiriting : ")
                    cars[car_number]["color"] = color
                    cars[car_number]["model"] = model
                    create_data(cars, "cars_data.json", "w")
                    print("Ma'lumot muvaffaqiyatli o'zgartirildi")
                else:
                    print("Kiritilgan raqam mavjud emas.")

        elif status == "4":
            print("Chiqish...")
            break  # Chiqish

        else:
            print("Noto'g'ri raqam, qayta urinib ko'ring.")
    with open("cars_data.json", "w") as file:
        json.dump(cards, file, indent=4)
cars_crud()
