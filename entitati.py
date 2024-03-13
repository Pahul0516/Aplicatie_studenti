from statistics import mean

def buuble_sort(list,n, key=lambda x:x, reverse=False):
 
     # algoritm de baza care sorteaza o lista primita
     # primul parametru este lista
     # al doilea este lungimea listei
          """
               algoritm care primeste o lista si o sorteaza in ordine crescatoare
               i = 1+1+...+n
               j = 1+1+..+n-1
               T(n)=1+1+1+...+n+1+1+...+n-1
               Complexitatea in cazul mediu si cel mai rau este O(n^2)
          """
          for i in range(0,n):
               for j in range (0,n-1):
                    if key(list[j])>key(list[j+1]):
                         aux=list[j]
                         list[j]=list[j+1]
                         list[j+1]=aux

          if reverse==True:
               list.reverse()
          return list

def Insertion_sort(list,n):

    """ insertion sort, e o metoda de baza a algoritmului shell sort"""

    for i in range (1,n):
        for j in range(i,0,-1):
            if (list[j-1]>list[j]):
                aux=list[j-1]
                list[j-1]=list[j]
                list[j]=aux
            else:
                break

    return list

def Shell_sort(list,n):
    """ 
        este o generalizare a insertion sort
        este o optimizarea a insertion sort
        trebuie sa ne folosim de un asa numit "gap"
        gap = n/2
    """
    gap=int(n/2)

    while gap!=0:
        for i in range(gap,n):
            for j in range(i,0,-gap):
                if (list[j-gap]>list[j] and j-gap>=0):
                    aux=list[j-gap]
                    list[j-gap]=list[j]
                    list[j]=aux
        gap=int(gap/2)

    return list


class Student:
     def __init__(self, id_student, nume_student, prenume_student):
          self.id_student=id_student
          self.nume_student=nume_student
          self.prenume_student=prenume_student

     def get_id_student(self):
          """
               functia are roul sa returneze id-ul unui student
          """
          return self.id_student

     def get_nume_student(self):
          """
               functia are roul sa returneze numele unui student
          """
          return self.nume_student

     def get_prenume_student(self):
         """
               functia are roul sa returneze prenumele unui student
          """
         return self.prenume_student

     def get_nume_complet_student(self):
         """
               functia are roul sa returneze numele complet (nume+prenume) al unui student
          """
         return "{} {}".format(self.nume_student, self.prenume_student)

     def set_id_student(self, value):
         """
               functia are roul sa schimbe id-ul unui student
          """
         self.id_student=value

     def set_nume_student(self,value):
          """
               functia are roul sa schimbe numele unui student
          """
          self.nume_student=value

     def set_prenume_student(self,value):
          """
               functia are roul sa schimbe prenumele unui student
          """
          self.prenume_student=value

class disciplina:
     def __init__(self, id_disciplina, nume_disciplina, profesor,note):
          self.id_disciplina=id_disciplina
          self.nume_disciplina=nume_disciplina
          self.profesor=profesor

     def get_id_disciplina(self):
          """
               functia are roul sa returneze id-ul unei discipline
          """
          return self.id_disciplina

     def get_nume_disciplina(self):
          """
               functia are roul sa returneze numele unei discipline
          """
          return self.nume_disciplina

     def get_profesor(self):
          """
               functia are roul sa returneze prenumele unei discipline
          """
          return self.profesor

     def set_id_disciplina(self,value):
          """
               functia are roul sa schimbe id-ul unei discipline
          """
          self.id_disciplina=value

     def set_nume_disciplina(self, value):
          """
               functia are roul sa schimbe numele unei discipline
          """
          self.nume_disciplina=value

     def set_profesor(self, value):
          """
               functia are roul sa schimbe prenumele unei discipline
          """
          self.profesor=value

class note:
     def __init__(self, id_nota, nota, id_student, id_disciplina):
          self.id_nota=id_nota
          self.nota=nota
          self.id_student=id_student
          self.id_disciplina=id_disciplina

     def get_id_nota(self):
          """
               functia are rolul de a obtine id-ul unei note
          """
          return self.id_nota

     def get_nota(self):
          """
               functia are rolul de a obtine o nota
          """
          return self.nota

     def get_id_student(self):
          return self.id_student

     def get_id_disciplina(self):
          return self.id_disciplina

     def set_id_nota(self,id):
          """
               functia are rolul de a modifica id-ul unei note
          """
          self.id_nota=id

     def set_nota(self,nota):
          """
               functia are rolul de a modifica o nota
          """
          self.nota=nota

     def set_id_student(self, id):
          """
               functia modifica id-ul studentului
          """
          self.id_student=id

     def set_id_disciplina(self,id):
          """
               functia modifica id-ul disciplinei
          """
          self.id_student=id

class note_Dto:
     def __init__(self,studenti,note,disicipline):
          self.studenti = studenti
          self.note = note
          self.disicipline = disicipline
     
     def get_total_note_student_disciplina(self, id_stu,id_dis):

          """
               functia primeste 2 parametrii numere intregi 
               functia returneaza o lista cu note in functie de id-ul disciplinei si al studentului
          """
          lista_note = []
          for ele in self.note.lista:
               if ele.id_student == id_stu and ele.id_disciplina==id_dis:
                    lista_note.append(ele.nota)
          return lista_note
     
     def sortare_dupa_disciplina(self, dis):


          """
               functia primeste un parametru
               returneaza un dictionar sortat cu toti elvii si toate notele la disciplina data
          """
          dictionar={}
          lista_id_studenti=[]
          lista_nume_studenti=[]
          id_disciplina=-1

          for ele in self.disicipline.repository.lista:
              if ele.nume_disciplina==dis:
                    id_disciplina=ele.id_disciplina
                    break

          for ele in self.note.repository.lista:
               if id_disciplina==ele.id_disciplina and ele.id_student not in lista_id_studenti:
                    lista_id_studenti.append(ele.id_student)

          for id in lista_id_studenti:
               for ele in self.studenti.repository.lista:
                    if ele.id_student==id:
                         lista_nume_studenti.append(ele.get_nume_complet_student())
          # Aici pentru sortari
          sorted_pairs = buuble_sort(list(zip(lista_nume_studenti, lista_id_studenti)),len(lista_nume_studenti),key=lambda x:x.get_nume_disciplina())
          sorted_nume, sorted_id = zip(*sorted_pairs)
          for i in range (0,len(sorted_id)):
               lista_note=[]
               for ele in self.note.repository.lista:
                    if ele.id_student==sorted_id[i] and ele.id_disciplina==id_disciplina:
                         lista_note.append(ele.nota)
               lista_note.sort()
               dictionar[sorted_nume[i]]=lista_note
          return dictionar
     
     def sortar_20(self):

          """
               functia nu primeste niciun parametru
               are rolul de a sorta studentii dupa media notelor la toate disciplinele
          """
          lista_studenti=[]
          lista_id_studenti=[]
          lista_medie_note=[]
          dictionar={}

          for ele in self.studenti.repository.lista:
               lista_studenti.append(ele.nume_student)
               lista_id_studenti.append(ele.id_student)

          for id in lista_id_studenti:
               suma=0
               n=0
               medie=0
               for ele in self.note.repository.lista:
                    if ele.id_student==id:
                         suma+=ele.nota
                         n+=1
               medie = mean(lista_medie_note) if n == 0 else suma / n
               lista_medie_note.append(medie)
          
          sorted_pairs = sorted(zip(lista_medie_note, lista_studenti), key=lambda x: x[0], reverse=True)
          sorted_medie, sorted_name = zip(*sorted_pairs)
          n=int(len(sorted_medie)*(1/5)) 
          for i in range(0,n):
               dictionar[sorted_name[i]]=sorted_medie[i]
          return dictionar








