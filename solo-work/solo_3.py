class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie_studenta = imie
        self.nazwisko_studenta = nazwisko
        self.numer_indeksu = numer_indeksu
        self.indeks_studenta = []
    
    def __str__(self):
        return self.imie_studenta + " " + self.nazwisko_studenta + " " + str(self.numer_indeksu)

    def dodaj_ocene(self, ocena):
        self.indeks_studenta.append(ocena)

    def srednia_ocen(self):
        if len(self.indeks_studenta) == 0:
            return "Srednia ocen wynosi: 0"
        else:
            srednia = sum(self.indeks_studenta) / len(self.indeks_studenta)
            return "Srednia ocen wynosi: " + str(srednia)

student_wiktoria = Student("Wiktoria","Marcinkowska","121569")

student_wiktoria.dodaj_ocene(5.0)
student_wiktoria.dodaj_ocene(2.0)
student_wiktoria.dodaj_ocene(3.0)
student_wiktoria.dodaj_ocene(4.0)

print(student_wiktoria.indeks_studenta)
print(student_wiktoria.srednia_ocen())
