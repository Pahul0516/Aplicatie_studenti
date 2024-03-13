import os
import unittest
import random
from entitati import *
from repository import *
from controler import *
from validator import *
"""
def test_get_id_student():
    
    test1 = Student (1,"John", "Snow")
    test2 = Student (2,"el", "cineva")
    test3 = Student (3,"ea", "altcineva")

    try:
        assert test1.get_id_student()==1
        assert test2.get_id_student()==2
        assert test3.get_id_student()==3

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")


def test_get_nume_student():

    test1 = Student (1,"John", "Snow")
    test2 = Student (2,"el", "cineva")
    test3 = Student (3,"ea", "altcineva")

    try:
        assert test1.get_nume_student()=="John"
        assert test2.get_nume_student()=="el"
        assert test3.get_nume_student()=="ea"

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")


def test_get_prenume_student():

    test1 = Student (1,"John", "Snow")
    test2 = Student (2,"el", "cineva")
    test3 = Student (3,"ea", "altcineva")

    try:
        assert test1.get_prenume_student()=="Snow"
        assert test2.get_prenume_student()=="cineva"
        assert test3.get_prenume_student()=="altcineva"

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")


def test_get_nume_complet_student():
    test1 = Student (1,"John", "Snow")
    test2 = Student (2,"el", "cineva")
    test3 = Student (3,"ea", "altcineva")

    try:
        assert test1.get_nume_complet_student()=="John Snow"
        assert test2.get_nume_complet_student()=="el cineva"
        assert test3.get_nume_complet_student()=="ea altcineva"

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")

def test_get_id_disciplina():
    test1=disciplina(1,"matematica","Marian",None)
    test2=disciplina(2,"romana","Ana",None)
    test3=disciplina(3,"istorie","Ion",None)

    try:
        assert test1.get_id_disciplina()==1
        assert test2.get_id_disciplina()==2
        assert test3.get_id_disciplina()==3

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")  

def test_get_nume_disciplina():
    test1=disciplina(1,"matematica","Marian",None)
    test2=disciplina(2,"romana","Ana",None)
    test3=disciplina(3,"istorie","Ion",None)

    try:
        assert test1.get_nume_disciplina()=="matematica"
        assert test2.get_nume_disciplina()=="romana"
        assert test3.get_nume_disciplina()=="istorie"

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine") 
   
def test_get_profesor():
    test1=disciplina(1,"matematica","Marian",None)
    test2=disciplina(2,"romana","Ana",None)
    test3=disciplina(3,"istorie","Ion",None)

    try:
        assert test1.get_profesor()=="Marian"
        assert test2.get_profesor()=="Ana"
        assert test3.get_profesor()=="Ion"

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")    

def test_generare_random():
    random.seed(0)

    test1=repository_studenti
    student1=Student
    student1=test1.generare_random(test1,1)

    test2=repository_studenti
    student2=Student
    student2=test2.generare_random(test2,2)

    test3=repository_studenti
    student3=Student
    student3=test3.generare_random(test3,3)

    try:

        assert student1.get_id_student()==1
        assert student1.get_nume_student()=="WAcqGFz"
        assert student1.get_prenume_student()=="EwLnG"

        assert student2.get_id_student()==2
        assert student2.get_nume_student()=="siW"
        assert student2.get_prenume_student()=="NZ"

        assert student3.get_id_student()==3
        assert student3.get_nume_student()=="ITZMj"
        assert student3.get_prenume_student()=="gUeRv"

        print ("totul e ok")
    except AssertionError:
        print ("ceva nu e bine")   
def test_adaugare_repository():
    
    val=validator_studenti()

    test1=repository_studenti(val)
    student=Student(1,"Alex", "Mateiu")
    test1.adaugare(student)

    test2=repository_studenti(val)
    student=Student(1,"Alex", "Mateiu")
    test2.adaugare(student)
    student=Student(1,"ceva", "cineva")
    test2.adaugare(student)

    try:
        assert test1.size()==1
        assert test2.size()==2
        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")

def test_adaugare_note():
    val=valideaza_nota()

    test1=repository_note(val)
    nota=note(1,9,1,1)
    test1.adaugare(nota)

    test2=repository_note(val)
    nota=note(1,9,1,2)
    test2.adaugare(nota)
    nota=note(1,10,2,2)
    test2.adaugare(nota)

    try:
        assert test1.size()==1
        assert test2.size()==2
        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")
    
def test_stergere_repository():

    val=validator_studenti()

    test1=repository_studenti(val)
    student=Student(1,"Alex", "Mateiu")
    test1.adaugare(student)

    test2=repository_studenti(val)
    student=Student(1,"Alex", "Mateiu")
    test2.adaugare(student)
    student=Student(2,"ceva", "cineva")
    test2.adaugare(student)

    test1.stergere(1)
    test2.stergere(2)

    try:
        assert test1.size()==0
        assert test2.size()==1
        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")

def test_modificare_repository():

    val=validator_studenti() # avem nevoie de niste valori in repository 

    test1=repository_studenti(val)  
    student=Student(1,"Alex", "Mateiu")
    test1.adaugare(student)

    test2=repository_studenti(val)
    student=Student(1,"Alex", "Mateiu")
    test2.adaugare(student)
    student=Student(2,"ceva", "cineva")
    test2.adaugare(student)  # de asta am facut toate lucrurile acestea intre comentarii

    test1.modificare(1,"Berindeie","Paul")
    test2.modificare(2,"Gabi","Mircea")

    try:
        assert test1.lista[0].get_id_student()==1
        assert test1.lista[0].get_nume_student()=="Berindeie"
        assert test1.lista[0].get_prenume_student()=="Paul"

        assert test2.lista[1].get_id_student()==2
        assert test2.lista[1].get_nume_student()=="Gabi"
        assert test2.lista[1].get_prenume_student()=="Mircea"

        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")

def test_size_repository():
    val=validator_studenti() # avem nevoie de niste valori in repository 

    test1=repository_studenti(val)  
    student=Student(1,"Alex", "Mateiu")
    test1.adaugare(student)

    test2=repository_studenti(val)
    student=Student(1,"Alex", "Mateiu")
    test2.adaugare(student)
    student=Student(2,"ceva", "cineva")
    test2.adaugare(student)  # de asta am facut toate lucrurile acestea intre comentarii

    try:
        assert test1.size()==1
        assert test2.size()==2
        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")


def test_verificare_existenta_id_repsitory():
    val=validator_studenti() # avem nevoie de niste valori in repository 

    test1=repository_studenti(val)  
    student=Student(1,"Alex", "Mateiu")
    test1.adaugare(student)

    test2=repository_studenti(val)
    student=Student(1,"Alex", "Mateiu")
    test2.adaugare(student)
    student=Student(2,"ceva", "cineva")
    test2.adaugare(student)  # de asta am facut toate lucrurile acestea intre comentarii

    try:
        assert test1.verificare_existenta_id(2)==0
        assert test1.verificare_existenta_id(1)==1
        assert test2.verificare_existenta_id(2)==1
        assert test2.verificare_existenta_id(3)==0
        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")

def test_sortare_dupa_disciplina():
    val_nota=valideaza_nota()
    val_stu=validator_studenti()
    val_dis=valideaza_disciplina()

    repo_note=repository_note(val_nota)
    repo_stu=repository_studenti(val_stu)
    repo_dis=repository_discipline(val_dis)

    nota=note(1,9,1,1)
    student=Student(1,"Cineva","Altcineva")
    disciplin=disciplina(1,"mate","el",None)

    repo_note.adaugare(nota)
    repo_stu.adaugare(student)
    repo_dis.adaugare(disciplin)

    legatura=note_Dto(repo_stu,repo_note,repo_dis)
    dictionar=legatura.sortare_dupa_disciplina("mate")
    try:
        assert dictionar =={
            "Cineva Altcineva": [9]
        }
        print("totul e ok")
    except AssertionError:
        print("ceva nu e bine")

def test_salvare_fis():
    pass


def rulare_teste():
   test_get_id_student()
   test_get_nume_student()
   test_get_prenume_student()
   test_get_nume_complet_student()
   test_get_id_disciplina()
   test_get_nume_disciplina()
   test_get_profesor()
   test_generare_random()
   test_adaugare_repository()
   test_stergere_repository()
   test_modificare_repository()
   test_size_repository()
   test_verificare_existenta_id_repsitory()
"""


class Teste(unittest.TestCase):
   
    def test_get_id_student(self):
    
        test1 = Student (1,"John", "Snow")
        test2 = Student (2,"el", "cineva")
        test3 = Student (3,"ea", "altcineva")

        self.assertEqual(test1.get_id_student(),1)
        self.assertEqual(test2.get_id_student(),2)
        self.assertEqual(test3.get_id_student(),3)

    def test_get_nume_student(self):

        test1 = Student (1,"John", "Snow")
        test2 = Student (2,"el", "cineva")
        test3 = Student (3,"ea", "altcineva")

        self.assertEqual(test1.get_nume_student(),"John")
        self.assertEqual(test2.get_nume_student(),"el")
        self.assertEqual(test3.get_nume_student(),"ea")

    def test_get_prenume_student(self):

        test1 = Student (1,"John", "Snow")
        test2 = Student (2,"el", "cineva")
        test3 = Student (3,"ea", "altcineva")

        self.assertEqual(test1.get_prenume_student(),"Snow")
        self.assertEqual(test2.get_prenume_student(),"cineva")
        self.assertEqual(test3.get_prenume_student(),"altcineva")

    def test_get_nume_complet_student(self):
        test1 = Student (1,"John", "Snow")
        test2 = Student (2,"el", "cineva")
        test3 = Student (3,"ea", "altcineva")

        self.assertEqual(test1.get_nume_complet_student(),"John Snow")
        self.assertEqual(test2.get_nume_complet_student(),"el cineva")
        self.assertEqual(test3.get_nume_complet_student(),"ea altcineva")

    def test_get_id_disciplina(self):
        test1=disciplina(1,"matematica","Marian",None)
        test2=disciplina(2,"romana","Ana",None)
        test3=disciplina(3,"istorie","Ion",None)

        self.assertEqual(test1.get_id_disciplina(), 1)
        self.assertEqual(test2.get_id_disciplina(), 2)
        self.assertEqual(test3.get_id_disciplina(), 3)

    def test_get_nume_disciplina(self):
        test1=disciplina(1,"matematica","Marian",None)
        test2=disciplina(2,"romana","Ana",None)
        test3=disciplina(3,"istorie","Ion",None)

        self.assertEqual(test1.get_nume_disciplina(),"matematica")
        self.assertEqual(test2.get_nume_disciplina(),"romana")
        self.assertEqual(test3.get_nume_disciplina(),"istorie")

    def test_get_profesor(self):
        test1=disciplina(1,"matematica","Marian",None)
        test2=disciplina(2,"romana","Ana",None)
        test3=disciplina(3,"istorie","Ion",None)

        self.assertEqual(test1.get_profesor(),"Marian")
        self.assertEqual(test2.get_profesor(),"Ana")
        self.assertEqual(test3.get_profesor(),"Ion")

    def test_generare_random(self):
        random.seed(0)

        test1=repository_studenti
        student1=Student
        student1=test1.generare_random(test1,1)

        test2=repository_studenti
        student2=Student
        student2=test2.generare_random(test2,2)

        test3=repository_studenti
        student3=Student
        student3=test3.generare_random(test3,3)

        self.assertEqual(student1.get_id_student(),1)
        self.assertEqual(student1.get_nume_student(),"WAcqGFz")
        self.assertEqual(student1.get_prenume_student(),"EwLnG")

        self.assertEqual(student2.get_id_student(),2)
        self.assertEqual(student2.get_nume_student(),"siW")
        self.assertEqual(student2.get_prenume_student(),"NZ")

        self.assertEqual(student3.get_id_student(),3)
        self.assertEqual(student3.get_nume_student(),"ITZMj")
        self.assertEqual(student3.get_prenume_student(),"gUeRv")

    def test_adaugare_repository(self):
    
        val=validator_studenti()

        test1=repository_studenti(val)
        student=Student(1,"Alex", "Mateiu")
        test1.adaugare(student)

        test2=repository_studenti(val)
        student=Student(1,"Alex", "Mateiu")
        test2.adaugare(student)
        student=Student(1,"ceva", "cineva")
        test2.adaugare(student)

        self.assertEqual( test1.size(),1)
        self.assertEqual( test2.size(),2)

    def test_stergere_repository(self):

        val=validator_studenti()

        test1=repository_studenti(val)
        student=Student(1,"Alex", "Mateiu")
        test1.adaugare(student)
        list1=[student]

        test2=repository_studenti(val)
        student1=Student(1,"Alex", "Mateiu")
        test2.adaugare(student1)
        student2=Student(2,"ceva", "cineva")
        test2.adaugare(student2)
        list2=[student1,student2]

        test1.stergere(1,list1)
        test2.stergere(2,list2)

        self.assertEqual( test1.size(),0)
        self.assertEqual( test2.size(),1)
        
    def test_adaugare_note(self):
        val=valideaza_nota()

        test1=repository_note(val)
        nota=note(1,9,1,1)
        test1.adaugare(nota)

        test2=repository_note(val)
        nota=note(1,9,1,2)
        test2.adaugare(nota)
        nota=note(1,10,2,2)
        test2.adaugare(nota)

        self.assertEqual(test1.size(),1)
        self.assertEqual( test2.size(),2)
    
    def test_modificare_repository(self):

        val=validator_studenti() # avem nevoie de niste valori in repository 

        test1=repository_studenti(val)  
        student=Student(1,"Alex", "Mateiu")
        test1.adaugare(student)
        list1=[student]

        test2=repository_studenti(val)
        student1=Student(1,"Alex", "Mateiu")
        test2.adaugare(student1)
        student2=Student(2,"ceva", "cineva")
        test2.adaugare(student2)  # de asta am facut toate lucrurile acestea intre comentarii
        list2=[student1,student2]

        test1.modificare(1,"Berindeie","Paul",list1)
        test2.modificare(2,"Gabi","Mircea",list2)

        self.assertEqual(test1.lista[0].get_id_student(),1)
        self.assertEqual(test1.lista[0].get_nume_student(),"Berindeie")
        self.assertEqual(test1.lista[0].get_prenume_student(),"Paul")

        self.assertEqual(test2.lista[1].get_id_student(),2)
        self.assertEqual(test2.lista[1].get_nume_student(),"Gabi")
        self.assertEqual(test2.lista[1].get_prenume_student(),"Mircea")

    def test_size_repository(self):
        val=validator_studenti() # avem nevoie de niste valori in repository 

        test1=repository_studenti(val)  
        student=Student(1,"Alex", "Mateiu")
        test1.adaugare(student)

        test2=repository_studenti(val)
        student=Student(1,"Alex", "Mateiu")
        test2.adaugare(student)
        student=Student(2,"ceva", "cineva")
        test2.adaugare(student)  # de asta am facut toate lucrurile acestea intre comentarii

        self.assertEqual(test1.size(),1)
        self.assertEqual(test2.size(),2)

    def test_verificare_existenta_id_repsitory(self):
        val=validator_studenti() # avem nevoie de niste valori in repository 

        test1=repository_studenti(val)  
        student=Student(1,"Alex", "Mateiu")
        test1.adaugare(student)

        test2=repository_studenti(val)
        student=Student(1,"Alex", "Mateiu")
        test2.adaugare(student)
        student=Student(2,"ceva", "cineva")
        test2.adaugare(student)  # de asta am facut toate lucrurile acestea intre comentarii

        self.assertEqual( test1.verificare_existenta_id(2),0)
        self.assertEqual( test1.verificare_existenta_id(1),1)
        self.assertEqual( test2.verificare_existenta_id(2),1)
        self.assertEqual( test2.verificare_existenta_id(3),0)
        
if __name__=="__main__":
    os.system('cls' if os.name=='nt' else "clear")
    unittest.main()
