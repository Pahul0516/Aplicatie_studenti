class validator_studenti():

    def valideaza(self,student):
        """
            functia primeste ca parametru un obiect de tip student
            functia are rolul de a verifica daca datele studentului sunt corecte+
        """
        errors=[]
        if student.id_student<=0:
            errors.append("Id-ul studentului trebuie sa fie pozitiv si mai mare ca 0")
        if not student.nume_student:
            errors.append("Studentul trebuie sa contina un nume")
        if not student.prenume_student:
            errors.append("Studentul trebuie sa contina un prenume")
        
        if len(errors)!=0:
            raise ValueError(errors)

class valideaza_disciplina():
        
    def valideaza(self, disciplina):
        """
            functia primeste ca parametru un obiect de tip disciplina
            functia are rolul de a verifica daca datele disciplinei sunt corecte
        """
        errors=[]
        if disciplina.id_disciplina<=0:
            errors.append("Id-ul disciplinei trebuie sa fie intreg si pozitiv")
        if not disciplina.nume_disciplina:
            errors.append("Disciplina trebuie sa contina un nume")
        if not disciplina.nume_disciplina:
            errors.append("Disciplina trebuie sa contina un profesor")
        if len(errors)!=0:
            raise ValueError(errors)

class valideaza_nota():
    def valideaza(self, nota):
        errors=[]
        if nota.id_nota<=0:
            errors.append("Id-ul notei trebuie sa fie intreg si pozitiv")
        if nota.id_student<=0:
            errors.append("Id-ul studentului trebuie sa fie intreg si pozitiv")
        if nota.id_disciplina<=0:
            errors.append("Id-ul disciplinei trebuie sa fie intreg si pozitiv")
        if nota.nota<=0:
            errors.append("Nota trebuie sa fie intrega si pozitiv")

        if len(errors)!=0:
            raise ValueError(errors)

