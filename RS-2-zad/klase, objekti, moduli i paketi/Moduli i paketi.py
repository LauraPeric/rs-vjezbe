'''
U main.py datoteci učitajte modul proizvodi.py iz paketa shop i pozovite pozovite funkciju
dodaj_proizvod za svaki element iz sljedeće liste:
proizvodi = [
 {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
 {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
 {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
 {"naziv": "Miš", "cijena": 100, "kolicina": 100}]
U main.py datoteci učitajte modul narudzbe.py iz paketa shop i pozovite funkciju napravi_narudzbu s
listom proizvoda iz prethodnog zadatka'''


from proizvodi import Proizvod, dodaj_proizvod, Proizvodi
from narudzbe import napravi_narudzbu


proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]


for proizvod_info in proizvodi:
    proizvod = Proizvod(proizvod_info["naziv"], proizvod_info["cijena"], proizvod_info["kolicina"])
    dodaj_proizvod(proizvod)

narudzba_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 1}
]

narudzba = napravi_narudzbu(narudzba_proizvodi)
if narudzba:
    print(narudzba.ispis_narudzbe())

 