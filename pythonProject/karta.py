import json
import re


def add_card():
    a = input("Karta qo'shmoqchi bo'lsangiz 1 ni bosing, o'chirmoqchi bo'lsangniz 2 ni bosing : ")
    if a == "1":
        cards = {}
        with open("Malumot1.json", "r") as file:
            try:
                cards = json.load(file)
            except:
                cards = {}

        while True:
            card_number = input("Karta raqamingizni kiriting : ")
            if re.match(r'^(4\d{12}|\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}|5[1-5]\d{14}|3[47]\d{13})$', card_number):
                cards[card_number] = {}
                break
            else:
                print("Qaytadan urinib ko'ring, karta raqamlari odatda 16 xonadan iborat bo'ladi")

        while True:
            name = input("Ismingizni kiriting : ")
            if re.match(r'^[A-Za-zА-Яа-яЁё]+(?:\s[A-Za-zА-Яа-яЁё]+)*$', name):
                cards[card_number]["name"] = name
                break
            else:
                print("Bosh harfi katta bilan yozilganiga e'tibor bering")

        while True:
            balans = input("Hisobingizdagi mablag'ni kiriting : ")
            if re.match(r'^\d+(\.\d{1,2})?$', balans):
                cards[card_number]["balans"] = balans

                break
            else:
                print("Sonlar orasi nuqta(.) bilan yozilganiga e'tibor bering")

        while True:
            password = input("4 xonali parol kiriting : ")
            if re.match(r'^\d{4}$', password):
                cards[card_number]["password"] = password

                break
            else:
                print("Parolda faqat sonlar ishtirok etishi kerak")

        while True:
            date = input("Amal qilish muddati MM/YY : ")
            if re.match(r'^(0[1-9]|1[0-2])\/(\d{2})$', date):
                cards[card_number]["date"] = date

                break
            else:
                print("MM - oylarni (0-12), YY - yillarni kiritishingiz lozim")

        print("Amaliyot muvaffaqiyatli yakunlandi")

    elif a == "2":
        cards = {}
        with open("Malumot1.json", "r") as file:
            try:
                cards = json.load(file)
            except:
                cards = {}

        while True:
            card_remove = input("O'chirmoqchi bo'lgan karta raqamingizni kiriting : ")
            if re.match(r'^(4\d{12}|\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}|5[1-5]\d{14}|3[47]\d{13})$', card_remove):
                if card_remove in cards:
                    cards.pop(card_remove)
                    print("Amaliyot muvaffaqiyatli yakunlandi")
                else:
                    print("Afsuski bunday karta mavjud emas")
                break
            else:
                print("Qaytadan urinib ko'ring, karta raqamlari odatda 16 xonadan iborat bo'ladi")

    with open("Malumot1.json", "w") as file:
        json.dump(cards, file, indent=4)


add_card()