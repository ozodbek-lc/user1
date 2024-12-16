import json
import os
import re


def student_javdal():
    while True:
        student = {}
        status = input("Q'shish uchun 1:\n O'chirish uchun 2 :\n yozing : ")

        if status == "1":
            if os.path.exists("students_jadval.json"):
                with open("students_jadval.json","r") as file:
                    student = json.load(file)
            else:
                student = {}

            while True:
                student_id = input("ID raqamini kiriting : ")
                if re.match(r'^\d{5}$', student_id):  # Student ID raqamini tekshirish uchun
                    student[student_id] = {}
                    break
                else:
                    print("bunday ID raqam ishlatish uchun yaroqsiz (29914) namuna ko'rinishida bolishi kerak ")

            while True:
                name = input("Ismizni kiriting : ")
                if re.match(r'^[a-z0-9_-]{3,15}$', name):  # Student ismini tekshirish uchun
                    student[student_id] = {"name": name}
                    break
                else:
                    print("Bunday ism mavjud emas bosh harfi katta bolishi kerka (Ali) namunu uchun")

            while True:
                namee = input("Familiani kiriting : ")
                if re.match(r'^[a-z0-9_-]{3,15}$', namee):  # Student familiasini tekshirish uchun
                    student[student_id]['namee']=namee
                    break
                else:
                    print("Bunday ism mavjud emas bosh harfi katta bolishi kerka (Aliyev yoki Aliyeva) namunu uchun")

            while True:
                nomer = input("Telefon raqamizni kiriting : ")
                if re.match(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', nomer):  # nomerini tekshirish uchun
                    student[student_id]['nomer']= nomer
                    break
                else:
                    print("Bunday telefon nomer yaroqsiz (+998XXXXXXXXX) korinishida bolishi kerak")

            with open("students_jadval.json", "w") as file:
                student = json.dump(student, file, indent=4)
            print("Student malumotlari muvofiqatli yakunlandi")
        # ID orqali student ma'lumotlarini o'chirish
        elif status == "2":
            if os.path.exists("students_jadval.json"):
                with open("students_jadval.json", "r") as file:
                    student = json.load(file)
            else:
                student = {}

            while True:
                student_remove = input("O'chirish uchun student ID sini kiriting : ")
                if re.match(r'^\d{5}', student_remove):  # Student ID raqamini yozib ma'lumotlarini o'chirish
                    if student_remove in student:
                        student.pop(student_remove)
                        print("Amalyot muvoffaqatli yakunlandi")
                        break
                    else:
                        print("Afsuski bunday student ID raqami mavjud emas")
                else:
                    print("Qayta urinib ko'ring")
            with open("students_jadval.json", "w") as file:
                json.dump(student, file, indent=4)


student_javdal()
