import json


def create_data(data:dict,file_name:str,status:str):
    with open(f"{file_name}",f"{status}") as file:
        if status=="w":
            json.dump(data,file,indent=4)
            return "ok"
        else:
            s=json.load(file)
            return s