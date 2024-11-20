'''Modul proizvodi.py :
definirajte klasu Proizvod s atributima naziv , cijena i kolicina . Dodajte metodu ispis koja će
ispisivati sve atribute proizvoda.
u listu proizvodi dodajte 2 objekta klase Proizvod s proizvoljnim vrijednostima atributa.
definirajte funkciju dodaj_proizvod van definicije klase koja će dodavati novi Proizvod u listu
proizvodi .
U main.py datoteci učitajte modul proizvodi.py iz paketa shop i pozovite pozovite funkciju
dodaj_proizvod za svaki element iz sljedeće liste:
proizvodi = [
 {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
 {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
 {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
 {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]'''

class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        return f"naziv: {self.naziv}, cijena: {self.cijena} €, količina: {self.kolicina}"
        

# Početna lista proizvoda s objektima klase Proizvod
Proizvodi = [
    Proizvod("Laptop", 5000, 10),
    Proizvod("Monitor", 1000, 20)
]

def dodaj_proizvod(proizvod):
    Proizvodi.append(proizvod)
