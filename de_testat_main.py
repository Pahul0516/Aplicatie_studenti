from entitati import *
from validator import *
from teste import *

import os

os.system('cls' if os.name == 'nt' else 'clear')

rulare_teste()

student1 = Student(1.1245,"Cineva","Altcineva")
vl=validator_studenti()

try:
    vl.valideaza(student1)
except ValueError as ve:
    print("Validation errors:")
    if isinstance(ve.args[0], list):
        for i, error in enumerate(ve.args[0], start=1):
            print(f"{i}. {error}")
    else:
        print(ve)


print(student1.get_nume_student())

a=1
b=2