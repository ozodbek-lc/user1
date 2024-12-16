import json
import re
import os


def add_kard():
    while True:
        cars = {}
        status = input("Qoshish uchun 1, Ochirish uchun 2: ")

        if status == "1":
            if os.path.exists("malumotlar.json"):
                with open("malumotlar.json", "r") as file:
                    cars = json.load(file)
            else:
                cars = {}

            while True:
                cars_number = input("Mashinani davlat raqamini kiriting: ")
                if re.match(r'^\d{2}[A-Z]{1}\d{3}[A-Z]{2}$', cars_number):  # Mashina raqami formatini tekshirish
                    cars[cars_number] = {}
                    break
                else:
                    print("Bunday nomer mavjud emas (01A123AB) namuna ko'rinishi bo'lishi kerak.")

            while True:
                name = input("Mashina egasini ismini kiriting: ")
                if re.match(r'^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$', name):  # Ism formatini tekshirish
                    cars[cars_number] = {'name': name}  # Ismni mashina raqami bilan bog'lash
                    break
                else:
                    print("Bunday ism to'g'ri kelmaydi. Iltimos qayta urinib ko'ring.")

            while True:
                tex_pasport = input("Tex pasport kiriting: ")
                if re.match(r'^[A-Z]{2}\d{7}$', tex_pasport):  # Tex pasport formatini tekshirish
                    cars[cars_number]['tex_pasport'] = tex_pasport  # Tex pasportni mashina raqami bilan bog'lash
                    break
                else:
                    print("Bunday tex pasport to'g'ri kelmaydi. Iltimos qaytadan urinib ko'ring.")

            with open("malumotlar.json", "w") as file:
                json.dump(cars, file, indent=4)
            print("Ma'lumotlar muvaffaqiyatli qo'shildi.")

        elif status == "2":
            if os.path.exists("malumotlar.json"):
                with open("malumotlar.json", "r") as file:
                    cars = json.load(file)
            else:
                cars = {}

            while True:
                cars_remove = input("O'chirmoqchi bo'lgan mashina raqamini kiriting: ")
                if re.match(r'^\d{2}[A-Z]{1}\d{3}[A-Z]{2}$', cars_remove):  # Mashina raqami formatini tekshirish
                    if cars_remove in cars:
                        cars.pop(cars_remove)
                        print("Amaliyot muvaffaqiyatli yakunlandi.")
                        break
                    else:
                        print("Afsuski bunday mashina raqami mavjud emas.")
                        break
                else:
                    print("Qaytadan urinib ko'ring.")

            with open("malumotlar.json", "w") as file:
                json.dump(cars, file, indent=4)


add_kard()
