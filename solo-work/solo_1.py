# zadanie 1.1

hello = "Hello"
student = "Wiktoria"
print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imię: ")
print("Hello {}!".format(student))

# zadanie 1.3
studenci = ["Marta", "Jola", "Ania", "Ola", "Stella"]
liczba_studentow = len(studenci)
print("Liczba studentów:", liczba_studentow)

# zadanie 1.4
studenci = ["Marta", "Jola", "Ania", "Ola", "Stella"]

for i in studenci:
    print("Hello, " + i + "!")

# zadanie 1.5

liczba = 6
potega = 8

wynik = liczba ** potega

print("Wynik wynosi: {}".format(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"

liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Jolanta Krawczyk", "Anna Beznazwiska", "Marta Ztrzemeszna", "Stella Winx", "Aleksandra Sześć"]

studenci_sorted = sorted(studenci)

print("Alfabetyczna lista studentow wynosi: ")
for i in studenci_sorted:
    print(i)

# zadanie 1.8

studenci = ["Jolanta Krawczyk", "Anna Beznazwiska", "Marta Ztrzemeszna", "Stella Winx", "Aleksandra Sześć"]

studenci_sorted_n = sorted(studenci, key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentow (nazwisko): ")
for i in studenci_sorted_n:
    print(i)

# zadanie 1.9

studenci = ["Jolanta Krawczyk", "Anna Beznazwiska", "Marta Ztrzemeszna", "Stella Winx", "Aleksandra Sześć", "Marta Nadiowa", "Kacper Nierudy", "Manuela Ichtroje", "Adrian Bugs", "Magdalena Konkursowiczka", "Wiktoria Nieborak", "Paulina Urzędas", "Szymon Naprawcertyfikat"]

liczba_n = sum(1 for student in studenci if student.split()[-1].startswith('N'))

print("Liczba studentów z nazwiskiem na literę N wynosi: ", liczba_n)

# zadanie 1.10

# zbadaj kazdy wykres, czy dla wyznaczonych punktów istnieje funkcja liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

# sprawdź czy istnieje funkcja liniowa łącząca punkty
def liniowosc_check(punkty):
    # sprawdź, czy ilość punktów się zgadza
    if len(punkty) < 2:
        return False
    # sprawdź różnice między punktami
    roznice = [(punkty[i+1][1] - punkty[i][1]) / (punkty[i+1][0] - punkty[i][0]) for i in range(len(punkty)-1)]
    # gdy różnice są takie same, to funkcja liniowa istnieje
    if all(roznice[0] == r for r in roznice):
        return True
    else:
        return False

# sprawdź wykresy
wykres_1_funkcja_liniowa = liniowosc_check(wykres_1)
wykres_2_funkcja_liniowa = liniowosc_check(wykres_2)
wykres_3_funkcja_liniowa = liniowosc_check(wykres_3)

# wyświetl rezultat
if wykres_1_funkcja_liniowa:
    print("Dla punktów w wykres_1 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_1 nie można wyznaczyć funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktów w wykres_2 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_2 nie można wyznaczyć funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktów w wykres_3 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_3 nie można wyznaczyć funkcji liniowej.")