class NameDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('name', None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Ism matn bo‘lishi kerak.")
        if len(value) < 4:
            raise ValueError("Ism kamida 4 ta harfdan iborat bo‘lishi kerak.")
        instance.__dict__['name'] = value

    def __delete__(self, instance):
        raise ValueError("Ism o‘chirib bo‘lmaydi!")

class IdDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('id',None)

    def __set__(self, instance, value):
        if not isinstance(value,int):
            raise ValueError("Id faqat raqam bolish kerak")
        if len(value)>3 and len(value)<3:
            raise ValueError("Id 3ta raqamdan iborat bo'lish kerak")
        instance.__dict__['id']=value

    def __delete__(self, instance):
        raise ValueError("Ism o‘chirib bo‘lmaydi!")

class Student:
    name = NameDescriptor()
    id=IdDescriptor

    def __init__(self,name,id):
        self.name=name
        self.id=id

try:
    student1=Student("ali",324)
except Exception as e:
    print(e)
try:
    student2=Student("alii",4)
except Exception as e:
    print(e)