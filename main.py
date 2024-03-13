import os
from ui import *
from repository import *
from validator import *
from controler import *
from teste import *

class app():


    def main(self): 
        """
            funcita are rolul de a initializa 2 variabile de tip controler
            functia are rolul de a rula consola
        """
        studenti_repository=repository_studenti(validator_studenti())
        studenti_controler=Student_controler(studenti_repository)
    
        disciplina_repository=repository_discipline(valideaza_disciplina())
        disciplina_controler=Disciplina_controler(disciplina_repository)

        note_repository=repository_note(valideaza_nota())
        nota_controler=Nota_controler(note_repository)

        legatura=note_Dto(studenti_repository,note_repository,disciplina_repository)

        con = Consola(studenti_controler,disciplina_controler,nota_controler, legatura)
        con.run()

os.system('cls' if os.name == 'nt' else 'clear')

# rulare_teste()

app=app()
app.main()



    