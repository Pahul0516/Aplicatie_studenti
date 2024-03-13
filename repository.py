import random
from entitati import *

class repository_studenti:
    def __init__(self, validare):
        self.lista=[]
        self.validare=validare   
    
    def adaugare(self, student):

        """
            functia primeste ca parametru un student
            are rolul de a adauga studentul in lista
        """
        self.validare.valideaza(student)
        self.lista.append(student)

    def generare_random(self, id):
        """
            functia primeste un id de tip int
            functia generaza random un unme si un prenume bazat pe un sir de caractere care contine toate literele alfabetului
            numle si prenumele pot sa aiba intre 1 si 10 caractere 
        """

        sir_litere="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXQZ"
        lungime = [1,2,3,4,5,6,7,9,10]
        nume=prenume=""
        for i in range(0,random.choice(lungime)):
            nume = nume+ random.choice(sir_litere)

        for i in range(0,random.choice(lungime)):
            prenume=prenume+random.choice(sir_litere)

        st=Student(id,nume,prenume)
        return st

    def stergere(self, id, lista):

        """
            functia primeste un id al unui student 
            id-ul este de tip intreg 
            functia sterge studentul din lista
        """
        for ele in lista:
            if ele.id_student==id:
                self.lista.remove(ele)


    def stergere_recursiv(self, id, lista):

        """
            functia primeste un id al unui student 
            id-ul este de tip intreg 
            functia sterge studentul din lista

        """
        # FUNCTIA E RECURSIVA
        if lista==[]:
            return
        else:
            ele=lista[0]
            if ele.id_student==id:
                self.lista.remove(ele)
            self.stergere_recursiv(id,lista[1:])


    def modificare(self, id, nume, prenume,lista):
        """
            functia primeste un id,nume si prenume al unui student 
            id-ul este de tip intreg 
            prenume - string
            nume - string
            functia modifica un student pe baza id-ului dat
        """

        for ele in lista:
            if ele.id_student==id:
                ele.set_nume_student(nume)
                ele.set_prenume_student(prenume)


    def modificare_recursiva(self, id, nume, prenume,lista):
        """
            functia primeste un id,nume si prenume al unui student 
            id-ul este de tip intreg 
            prenume - string
            nume - string
            functia modifica un student pe baza id-ului dat
        """
          # FUNCTIA E RECURSIVA
        if lista==[]:
            return
        else:
            ele=lista[0]
            if ele.id_student==id:
                ele.set_nume_student(nume)
                ele.set_prenume_student(prenume)
            self.modificare_recursiva(id, nume, prenume,lista[1:])
    

    def asignare(self,id_stud,nota):
        lista=self.lista
        for ele in lista:
            if ele.get_id_student()==id_stud:
                ele.lista_note.append(nota)

    def size(self):

        "functia returneaza lungimea listeai unde sunt strocati studentii"
        return len(self.lista)
    
    def verificare_existenta_id(self, id):

        """
            functia primeste un id
            functia verifica daca exista un student cu id-ul dat
        """
        for ele in self.lista:
            if ele.id_student==id:
                return 1
        return 0

class repository_discipline:
    def __init__(self, validare):
        self.lista=[]
        self.validare=validare
    
    def adaugare(self, item):
        """
            functia primeste ca parametru o disciplina
            are rolul de a adauga disciplina in lista
        """
        self.validare.valideaza(item)
        self.lista.append(item)

    def generare_random(self, id):
        """
            functia primeste un id de tip int
            functia generaza random un unme si un prenume bazat pe un sir de caractere care contine toate literele alfabetului
            numle si prenumele pot sa aiba intre 1 si 10 caractere 
        """

        sir_litere="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXQZ"
        lungime = [1,2,3,4,5,6,7,9,10]
        nume_dis=nume_prof=""
        for i in range(0,random.choice(lungime)):
            nume_dis = nume_dis+ random.choice(sir_litere)

        for i in range(0,random.choice(lungime)):
            nume_prof=nume_prof+random.choice(sir_litere)

        st=disciplina(id,nume_dis,nume_prof,None)
        return st
    
    def stergere(self, id):
        """
            functia primeste un id al unei discipline 
            id-ul este de tip intreg 
            functia sterge disciplina din lista
        """
        for ele in self.lista:
            if ele.id_disciplina==id:
                self.lista.remove(ele)

    def modificare(self, id, nume_dis, nume_prof):
        """
            functia primeste un id,nume disciplina si nume profesor al unui student 
            id-ul este de tip intreg 
            nume disciplina - string
            nume profesor - string
            functia modifica o disciplina pe baza id-ului dat
        """
        for ele in self.lista:
            if ele.id_disciplina==id:
                ele.set_nume_disciplina(nume_dis)
                ele.set_profesor(nume_prof)

    def get_all(self):
        """
            functia returneaza toatre disciplinele
        """
        return self.lista



    def size(self):
        "functia returneaza lungimea listeai unde sunt stocate disciplinele"
        return len(self.lista)
    
    def verificare_existenta_id(self, id):
        """
            functia primeste un id
            functia verifica daca exista o disciplina cu id-ul dat
        """
        for ele in self.lista:
            if ele.id_disciplina==id:
               return 1
        return 0
    
class repository_note:
    def __init__(self, validare):
        self.lista=[]
        self.validare=validare

    def adaugare(self,item):
        """
            functia are rolul de a de a adauga nota in repository
        """
        self.lista.append(item)

    def size(self):
        return len(self.lista)


class repository_studenti_fisier:
    def __init__(self,repo):
        self.repo=repo

    def salvare(self):
        f = open("studenti.txt","w")
        lista = self.repo.lista
        for ele in lista:
            f.write(str(ele.get_id_student()))
            f.write(" ")
            f.write(str(ele.get_nume_student()))
            f.write(" ")
            f.write(str(ele.get_prenume_student()))
            f.write("\n")

        f.close()

    def incarcare(self):
        f = open("adaugare_studenti.txt","r")
        matrice=[]
        while(True):
            lista=f.readline()
            if lista=='':
                break
            lista=lista.split()
            matrice.append(lista)

        return matrice

class repository_discipline_fisier:
    def __init__(self,repo):
        self.repo=repo

    def salvare(self):
        f = open("discipline.txt","w")
        lista = self.repo.lista
        for ele in lista:
            f.write(str(ele.get_id_disciplina()))
            f.write(" ")
            f.write(str(ele.get_nume_disciplina()))
            f.write(" ")
            f.write(str(ele.get_profesor()))
            f.write("\n")

        f.close()

    def incarcare(self):
        f = open("adaugare_discipline.txt","r")
        matrice=[]
        while(True):
            lista=f.readline()
            if lista=='':
                break
            lista=lista.split()
            matrice.append(lista)
        
        return matrice

class repository_note_fisier:
    def __init__(self,repo):
        self.repo=repo


    def salvare(self):
        f = open("note.txt","w")
        lista = self.repo.lista
        for ele in lista:
            f.write(str(ele.get_id_nota()))
            f.write(" ")
            f.write(str(ele.get_nota()))
            f.write(" ")
            f.write(str(ele.get_id_student()))
            f.write(" ")
            f.write(str(ele.get_id_disciplina()))
            f.write("\n")

        f.close()

    def incarcare(self):

        f = open("adaugare_note.txt","r")
        matrice=[]
        while(True):
            lista=f.readline()
            if lista=='':
                break
            lista=lista.split()
            matrice.append(lista)

        return matrice
