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