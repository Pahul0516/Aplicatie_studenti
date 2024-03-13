import os
from entitati import *
from repository import *

class Consola():

    def __init__(self,studenti_controler,disciplina_controler,nota_controler,legatura):
        self.studenti_controler=studenti_controler
        self.disciplina_controler=disciplina_controler
        self.nota_controler=nota_controler
        self.legatura=legatura


    def adaugare_student(self):
        """
            functia are roulu de a adauga un student
        """
        id = int(input("Va rog sa introduceti id-ul studentului: "))
        nume = input("Va rog sa introduceti numele studentului: ")
        prenume = input("Va rog sa introduceti prenumele studentului: ")
        self.studenti_controler.adaugare_student(id,nume,prenume)
    
    def adaugare_student_random(self):
        """
            functia are roulu de a adauga un student random
        """
        id= int(input("Va rog sa introduceti id-ul studentului pe care doriti sa il introduceti random: "))
        self.studenti_controler.adaugare_student_random(id)
 
    def afisare_studenti(self):
        """
            functia are rolul de a afisa studentii
        """
        for ele1 in self.studenti_controler.repository.lista:
            print("\n",ele1.id_student, ele1.nume_student, ele1.prenume_student,"\n")
            discipline=self.disciplina_controler.repository.get_all()
            for ele2 in discipline:
                note=self.legatura.get_total_note_student_disciplina(ele1.id_student,ele2.id_disciplina)
                if note==[]:
                    print("elevul nu are note la disciplina",ele2.nume_disciplina)
                else:
                    print(ele2.nume_disciplina,"-",note)
            print("\n")

    def stergere_student_dupa_id(self):
        """
            functia are rolul de a sterge studenti dupa id
        """
        id=int(input("Va rog sa introduceti id-ul studentului pe care doriti sa il stergeti: "))
        self.studenti_controler.stergere_student(id)

    def modificare_studenti_dupa_id(self):
        """
            functia are rolul de a modifica studenti dupa id
        """
        id=int(input("Va rog sa introduceti id-ul studentului pe care doriti sa il modificati: "))
        nume = input("Va rog sa introduceti numele studentului pe care doriti sa il modificati: ")
        prenume = input("Va rog sa introduceti prenumele studentuluipe care doriti sa il modificati: ")
        self.studenti_controler.modificare_student(id,nume, prenume)

    def asignare_nota_student(self):
       pass

    def adaugare_disciplina(self):
        """
            functia are rolul de a adauga o disciplina
        """
        id = int(input("Va rog sa introduceti id-ul disciplinei: "))
        nume_dis = input("Va rog sa introduceti numele disciplinei: ")
        nume_prof = input("Va rog sa introduceti numele profesorului: ")
        self.disciplina_controler.adaugare_disciplina(id,nume_dis,nume_prof)

    def adaugare_disciplina_random(self):
        id= int(input("Va rog sa introduceti id-ul disciplinei pe care doriti sa o introduceti random: "))
        self.disciplina_controler.adaugare_disciplina_random(id)

    def afisare_discipline(self):
        """
            functia are rolul de a afisa o disciplina
        """
        for ele in self.disciplina_controler.repository.lista:
            print("\n", ele.id_disciplina, ele.nume_disciplina, ele.profesor, "\n")

    def stergere_disciplina_dupa_id(self):
        """
            functia are rolul de a sterge o disciplina dupa un id dat de utilizator
        """
        id=int(input("Va rog sa introduceti id-ul disciplinei pe care doriti sa o stergeti: "))
        self.disciplina_controler.stergere_disciplina(id)

    def modificare_disciplina_dupa_id(self):
        """
            functia are rolul de a modiifica o disciplina dupa un id dat de utilizator
        """
        id=int(input("Va rog sa introduceti id-ul disciplinei pe care doriti sa o modificati: "))
        nume_dis = input("Va rog sa introduceti numele disciplinei pe care doriti sa o modificati: ")
        nume_prof = input("Va rog sa introduceti prenumele profesorului disciplinei care doriti sa o modificati: ")
        self.disciplina_controler.modificare_disciplina(id,nume_dis, nume_prof)

    def adaugare_nota(self):
        """
            functia are roulu de a adauga o nota unei materii si unui elev
        """
        id=int(input("Va rog sa introduceti id-ul notei: "))
        nota=int(input("Va rog sa introduceti nota: "))
        id_stu=int(input("Va rog sa introduceti id-ul elevului: "))
        id_dis=int(input("Va rog sa introduceti id-ul disciplinei: "))
        self.nota_controler.adaugare(id,nota,id_stu,id_dis)
    
    def sortare_dupa_disciplina_data(self):
        """
            functia are rolul de a sorta elevii dupa nume si nota
        """
        disciplina=input("Introduceti disciplina la care doriti sortarea: ")
        legatura=note_Dto(self.studenti_controler,self.nota_controler,self.disciplina_controler)
        dictionar=legatura.sortare_dupa_disciplina(disciplina)
        keys_list = list(dictionar.keys())
        for ele in keys_list:
            print(ele, ": ", end="")
            lista_note = dictionar[ele]
            for nota in lista_note:
                print(nota, " ", end="")
            print("\n")
        print("\n")

    def sortare_20(self):
        
        print ("\n")
        legatura=note_Dto(self.studenti_controler,self.nota_controler,self.disciplina_controler)
        dictionar=legatura.sortar_20()
        keys_list = list(dictionar.keys())
        for ele in keys_list:
            print (ele, dictionar[ele],"\n")
      
    def salvare_date_fisier(self):
        repo_studenti_fis=repository_studenti_fisier(self.studenti_controler.repository)
        repo_disciplina_fis=repository_discipline_fisier(self.disciplina_controler.repository)
        repo_note_fis=repository_note_fisier(self.nota_controler.repository)
        repo_studenti_fis.salvare()
        repo_disciplina_fis.salvare()
        repo_note_fis.salvare()

        print("\n Datele au fost incarcate cu succes in fisiere. \n")

    def incarcare_date_din_fisier(self):

        repo_studenti_fis=repository_studenti_fisier(self.studenti_controler.repository)
        repo_disciplina_fis=repository_discipline_fisier(self.disciplina_controler.repository)
        repo_note_fis=repository_note_fisier(self.nota_controler.repository)

        lista_stu=repo_studenti_fis.incarcare()

        while(lista_stu):

            ele=lista_stu[0]

            id = int(ele[0])
            nume = ele[1]
            prenume = ele[2]
            self.studenti_controler.adaugare_student(id,nume,prenume)
            lista_stu=lista_stu[1:]

        lista_dis=repo_disciplina_fis.incarcare()

        while(lista_dis):

            ele=lista_dis[0]

            id = int(ele[0])
            nume_dis = ele[1]
            nume_prof = ele[2]
            self.disciplina_controler.adaugare_disciplina(id,nume_dis,nume_prof)
            lista_dis=lista_dis[1:]

        lista_note=repo_note_fis.incarcare()

        while(lista_note):

            ele=lista_note[0]

            id=int(ele[0])
            nota=int(ele[1])
            id_stu=int(ele[2])
            id_dis=int(ele[3])
            self.nota_controler.adaugare(id,nota,id_stu,id_dis)
            lista_note=lista_note[1:]

        print("\n Datele au fost incarcate cu succes \n")


    def afisare_optiuni(self):
        """
            functia are rolul de a afisa optiunile disponibile
        """
        print("1.Adaugare_student\n"
              "2.Afisare_student\n"
              "3.Stergere_student_dupa_id\n"
              "4.Modificare_studenti_dupa_id\n"
              "5.Adaugare_disciplina\n"
              "6.Afisare_disciplina\n"
              "7.Stergere_disciplina_dupa_id\n"
              "8.Modificare_disciplina_dupa_id\n"
              "9.Adaugare_student_random\n"
              "10.Adaugare_disciplina_random\n"
              "11.Adaugare_nota\n"
              "12.Sortare_dupa_nume\n"
              "13.Sortare_20%\n"
              "14.Salvare_date_fisier\n"
              "15.Incarcare_date_din_fisier")


    def run(self):
        """
            functia ia input-urile utilizatorului si le executa in functie de cerinta
        """
        optiuni={1:self.adaugare_student,
                 2:self.afisare_studenti,
                 3:self.stergere_student_dupa_id,
                 4:self.modificare_studenti_dupa_id,
                 5:self.adaugare_disciplina,
                 6:self.afisare_discipline,
                 7:self.stergere_disciplina_dupa_id,
                 8:self.modificare_disciplina_dupa_id,
                 9:self.adaugare_student_random,
                 10:self.adaugare_disciplina_random,
                 11:self.adaugare_nota,
                 12:self.sortare_dupa_disciplina_data,
                 13:self.sortare_20,
                 14:self.salvare_date_fisier,
                 15:self.incarcare_date_din_fisier
                 }

        while True:
            self.afisare_optiuni()
            try:
                operatie=int(input("Te rog sa introdici o optiune "))
            except ValueError:
                print("optiunea nu este buna")


            if operatie==111:
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                try:
                    optiuni[operatie]()
                except ValueError as er:
                    print(er)
                except KeyError:
                    pass