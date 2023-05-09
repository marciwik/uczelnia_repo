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