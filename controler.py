from entitati import *

class Student_controler():

    def __init__(self, repository):
        self.repository=repository

    def adaugare_student(self,id,nume,prenume):
        """
            are 3 parametrii:
                id - int
                nume - char
                prenume - char
            are rolul de a crea un student si de a-l adauga intr-o lista
        """
        student=Student(id,nume,prenume)
        if self.repository.verificare_existenta_id(id)==0:
            self.repository.adaugare(student)
        else:
            raise ValueError("\nExista un student cu id-ul dat\n")
    
    def adaugare_student_random(self,id):
        """
            are 1 parametru:
                id - int
            are rolul de a crea un student random si de a-l adauga intr-o lista
        """
        if self.repository.verificare_existenta_id(id)==0:
            self.repository.adaugare(self.repository.generare_random(id))
        else:
            raise ValueError("\nExista un student cu id-ul dat\n")

    def stergere_student(self, id):
        """
            are 1 parametru:
                id - int
            are rolul de a sterge un student dupa id
        """
        self.repository.stergere_recursiv(id,self.repository.lista)

    def modificare_student(self,id,nume,prenume):
        """
            are 1 parametru:
                id - int
            are rolul de a modifica un student dupa id
        """
        self.repository.modificare_recursiva(id,nume,prenume,self.repository.lista)

class Disciplina_controler():

    def __init__(self, repository):
        self.repository=repository

    def adaugare_disciplina(self,id,nume_dis,nume_prof):
        """
            are 3 parametrii:
                id - int
                nume_dis - char
                nume_prof - char
            are rolul de a crea o disciplina si de a o adauga intr-o lista
        """
        dis=disciplina(id,nume_dis,nume_prof,None)
        if self.repository.verificare_existenta_id(id)==0:
             self.repository.adaugare(dis)

    def adaugare_disciplina_random(self,id):
        """
            are 1 parametru:
                id - int
            are rolul de a crea o disciplina random si de a o adauga intr-o lista
        """
        if self.repository.verificare_existenta_id(id)==0:
            self.repository.adaugare(self.repository.generare_random(id))
        else:
            raise ValueError("\nExista o disciplina cu id-ul dat\n") 

    def stergere_disciplina(self, id):
        """
            are 1 parametru:
                id - int
            are rolul de a sterge o disciplina dupa id
        """
        self.repository.stergere(id)

    def modificare_disciplina(self,id,nume_dis,nume_prof):
        """
            are 1 parametru:
                id - int
            are rolul de a modifica o disciplian dupa id
        """
        self.repository.modificare(id,nume_dis,nume_prof)

class Nota_controler():
    def __init__(self,repository):
        self.repository=repository

    def adaugare(self, id, nota,id_stu,id_dis):
        """
            functia are rolul de a asigna o nota unui elev si unei disicpline
        """
        nota=note(id,nota,id_stu,id_dis)
        self.repository.adaugare(nota)