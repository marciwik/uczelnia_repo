# określenie klasy dla platform streamingowych
class PlatformaStreamingowa:
    def __init__(self, nazwa, rodzaj, liczba_tytulow, subskrypcja, cena_miesieczna, obslugiwane_urzadzenia, jezyki_dostepne, ulubione_tytuly):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.liczba_tytulow = liczba_tytulow
        self.subskrypcja = subskrypcja
        self.cena_miesieczna = cena_miesieczna
        self.obslugiwane_urzadzenia = obslugiwane_urzadzenia
        self.jezyki_dostepne = jezyki_dostepne
        self.ulubione_tytuly = ulubione_tytuly

# funkcja podająca informacje na temat dane platformy streamingowej    
    def wyswietl_informacje(self):
        print(f"Nazwa platformy: {self.nazwa}")
        print(f"Rodzaj platformy: {self.rodzaj}")
        print(f"Liczba dostępnych tytułów: {self.liczba_tytulow}")
        print(f"Subskrypcja: {'Tak' if self.subskrypcja else 'Nie'}")
        print(f"Cena miesięczna: {self.cena_miesieczna} PLN")
        print(f"Obsługiwane urządzenia: {', '.join(self.obslugiwane_urzadzenia)}")
        print(f"Języki dostępne: {', '.join(self.jezyki_dostepne)}")
        print(f"Ulubione tytuły: {', '.join(self.ulubione_tytuly)}")
        print()

# funkcje umożliwaiające dodawanie ulubionych tytułów i aktualizujące te poprzednio określone 
    def dodaj_ulubiony_tytul(self, tytul):
        self.ulubione_tytuly.append(tytul)
        print(f"Dodano tytuł {tytul} do ulubionych tytułów platformy {self.nazwa}.")
        self.aktualizuj_ulubione_tytuly()
    
    def aktualizuj_ulubione_tytuly(self):
        print(f"Aktualizacja ulubionych tytułów dla platformy {self.nazwa}:")
        print(f"Ulubione tytuły: {', '.join(self.ulubione_tytuly)}")
        print()  

# funkcja porównująca, która subskrypcja jest najtańsza, a która najdroższa
def porownaj_ceny_subskrypcji(platformy):
    najtansza_platforma = min(platformy, key=lambda x: x.cena_miesieczna)
    najdrozsza_platforma = max(platformy, key=lambda x: x.cena_miesieczna)

    print("Najtańsza platforma:")
    print(f"Nazwa platformy: {najtansza_platforma.nazwa}")
    print(f"Cena subskrypcji: {najtansza_platforma.cena_miesieczna} PLN")
    print()

    print("Najdroższa platforma:")
    print(f"Nazwa platformy: {najdrozsza_platforma.nazwa}")
    print(f"Cena subskrypcji: {najdrozsza_platforma.cena_miesieczna} PLN")
    print()

#funkcja wyliczająca roczne wydatki na subskrypcję
def oblicz_wartosc_rocznej_subskrypcji(platformy):
    for platforma in platformy:
        wartosc_roczna = platforma.cena_miesieczna * 12
        print(f"Wartość rocznej subskrypcji dla platformy {platforma.nazwa}: {wartosc_roczna} PLN")

#funkcja wyliczająca CAŁKOWITE roczne wydatki na subskrypcje
def oblicz_roczne_wydatki_na_subskrypcje(platformy):
    wydatki_roczne = 0
    for platforma in platformy:
        if platforma.subskrypcja:
            wydatki_roczne += platforma.cena_miesieczna * 12
    print(f"Całkowite roczne wydatki na subskrypcje: {wydatki_roczne} PLN")
    print()

# określenie platform w oparciu o najpopularniejsze
platforma1 = PlatformaStreamingowa("Netflix", "VOD", 5000, True, 39.99, ["Telewizor", "Smartfon", "Tablet"], ["Polski", "Angielski", "Hiszpański"], ["Stranger Things", "The Crown"])
platforma2 = PlatformaStreamingowa("Amazon Prime Video", "VOD", 3000, True, 29.99, ["Telewizor", "Smartfon", "Tablet", "Komputer"], ["Polski", "Angielski", "Niemiecki"], ["The Marvelous Mrs. Maisel", "Fleabag"])
platforma3 = PlatformaStreamingowa("Disney+", "VOD", 1000, True, 19.99, ["Telewizor", "Smartfon", "Tablet"], ["Polski", "Angielski"], ["The Mandalorian", "WandaVision"])
platforma4 = PlatformaStreamingowa("HBO Max", "VOD", 2000, True, 34.99, ["Telewizor", "Smartfon", "Tablet", "Komputer"], ["Polski", "Angielski"], ["Game of Thrones", "Chernobyl"])
platforma5 = PlatformaStreamingowa("Apple TV+", "VOD", 500, False, 19.99, ["Telewizor", "Smartfon", "Tablet", "Komputer"], ["Polski", "Angielski"], ["Ted Lasso", "The Morning Show"])

# lista platform streamingowych, po której można iterować
platformy = [platforma1, platforma2, platforma3, platforma4, platforma5]

# wyświetlenie informacji o każdej platformie
platforma1.wyswietl_informacje()
platforma2.wyswietl_informacje()
platforma3.wyswietl_informacje()
platforma4.wyswietl_informacje()
platforma5.wyswietl_informacje()

# dodanie nowego ulubionego tytułu dla Amazonu
platforma2.dodaj_ulubiony_tytul("The Boys")

platforma2.wyswietl_informacje()

# dodanie nowego ulubionego tytułu dla Disney+
platforma3.dodaj_ulubiony_tytul("Loki")

platforma3.wyswietl_informacje()

# porównanie cen subskrypcji
porownaj_ceny_subskrypcji(platformy)

# obliczenie wartości rocznej subskrypcji
oblicz_wartosc_rocznej_subskrypcji(platformy)

# obliczenie całkowitych rocznych wydatków na subskrypcje
oblicz_roczne_wydatki_na_subskrypcje(platformy)