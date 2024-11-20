'''Modul narudzbe.py :
definirajte klasu Narudzba s atributima: proizvodi i ukupna_cijena .
dodajte funkciju napravi_narudzbu van definicije klase koja prima listu proizvoda kao argument i
vraća novu instancu klase Narudzba .
dodajte provjeru u funkciju napravi_narudzbu koja će provjeravati dostupnost proizvoda prije nego
što se napravi narudžba. Ako proizvoda nema na stanju, ispišite poruku "Proizvod {naziv} nije
dostupan!" i ne stvarajte narudžbu.
dodajte provjere u funkciju napravi_narudzbu koja će provjeriti sljedeća 4 uvjeta:
argument proizvodi mora biti lista
svaki element u listi mora biti rječnik
svaki rječnik mora sadržavati ključeve naziv , cijena i kolicina
lista ne smije biti prazna
izračunajte ukupnu cijenu narudžbe koju ćete pohraniti u ukupna_cijena u jednoj liniji koda.
narudžbe pohranite u listu rječnika narudzbe .
u klasu Narudzba dodajte metodu ispis_narudzbe koja će ispisivati nazive svih naručenih proizvoda,
količine te ukupnu cijenu narudžbe.
npr. "Naručeni proizvodi: Laptop x 2, Monitor x 1, Ukupna cijena: 11000 eur".
U main.py datoteci učitajte modul narudzbe.py iz paketa shop i pozovite funkciju napravi_narudzbu s
listom proizvoda iz prethodnog zadatka
'''

class Narudzba:
    def __init__(self, proizvodi):
        self.proizvodi = proizvodi
        self.ukupna_cijena = sum(proizvod["cijena"] * proizvod["kolicina"] for proizvod in proizvodi)

    def ispis_narudzbe(self):
        proizvodi_ispis = ', '.join([f"{proizvod['naziv']} x {proizvod['kolicina']}" for proizvod in self.proizvodi])
        return f"Naručeni proizvodi: {proizvodi_ispis}, Ukupna cijena: {self.ukupna_cijena} EUR"


def napravi_narudzbu(proizvodi):
    if not isinstance(proizvodi, list) or len(proizvodi) == 0:
        print("Pogrešan unos! Lista proizvoda mora biti neprazna.")
        return None
    
    for proizvod in proizvodi:
        if not isinstance(proizvod, dict):
            print("Pogrešan unos! Svaki element liste mora biti rječnik.")
            return None
        if not all(key in proizvod for key in ["naziv", "cijena", "kolicina"]):
            print(f"Proizvod {proizvod} nije valjan mora sadržavati 'naziv', 'cijenu' i 'kolicinu'.")
            return None
        # Provjera dostupnosti proizvoda (pretpostavljamo da proizvodi iz paketa shop su dostupni)
        if proizvod["kolicina"] == 0:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None

    return Narudzba(proizvodi)
