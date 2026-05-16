"""
2. feladat - Logikai / szemantikai hibas kod javitasa (5 pont)
TODO:
- A kod fut, de pontosan 5 logikai hibat tartalmaz a feladatok megoldasaban.
- Javitsd ugy, hogy az eredmenyek helyesek legyenek.
- Minden javitas 1 pont.
Feladat:
- Egy vegremenyet statisztikai feldolgozasa.
- Minden vegzett tanulohoz tartozik: nev, szuletesi_ev, atlagpontszam, nyelv.
- Szamold ki:
  1. az atlagos szuletesi evet,
  2. az ossz atlagpontszam,
  3. a nyelvek gyakorisagat,
  4. a legmagasabb atlagpontszammal rendelkezo tanulonak a nevet,
  5. akik a 100-as atlagpontszamnak megfelelnek.

Elvart eredmenyek:
- Atlagos szuletesi ev: 2004
- Atlagos pontszam: 91.0
- Nyelvek gyakorisaga: {'angol': 3, 'nemet': 2}
- Legjobb tanulonak az atlaga: 100
- 100-as tanulok: ['Janos', 'Laszlo']
"""

tanulok = [
    {"nev": "Peter", "szuletesi_ev": 2003, "atlagpontszam": 78, "nyelv": "angol"},
    {"nev": "Maria", "szuletesi_ev": 2005, "atlagpontszam": 85, "nyelv": "angol"},
    {"nev": "Janos", "szuletesi_ev": 2004, "atlagpontszam": 100, "nyelv": "nemet"},
    {"nev": "Anna", "szuletesi_ev": 2004, "atlagpontszam": 92, "nyelv": "angol"},
    {"nev": "Laszlo", "szuletesi_ev": 2005, "atlagpontszam": 100, "nyelv": "nemet"},
]

def atlagos_szuletesi_ev(tanulok_lista):
    if not tanulok_lista:
        return 0
    osszeg = 0
    for tanulo in tanulok_lista:
        osszeg += tanulo["szuletesi_ev"]
    return osszeg // len(tanulok_lista)

def atlagos_pontszam(tanulok_lista):
    if not tanulok_lista:
        return 0.0
    osszeg = 0
    for tanulo in tanulok_lista:
        osszeg += tanulo["atlagpontszam"]
    return osszeg / len(tanulok_lista)

def nyelvek_gyakorisaga(tanulok_lista):
    gyakorisag = {}
    for tanulo in tanulok_lista:
        nyelv = tanulo["nyelv"]
        if nyelv in gyakorisag:
            gyakorisag[nyelv] += 1
        else:
            gyakorisag[nyelv] = 1
    return gyakorisag

def legjobb_tanulo(tanulok_lista):
    if not tanulok_lista:
        return None
    legjobb = tanulok_lista[0]
    for tanulo in tanulok_lista[1:]:
        if tanulo["atlagpontszam"] > legjobb["atlagpontszam"]:
            legjobb = tanulo
    return legjobb["atlagpontszam"]

def szazas_tanulok(tanulok_lista):
    eredmeny = []
    for tanulo in tanulok_lista:
        if tanulo["atlagpontszam"] == 100:
            eredmeny.append(tanulo["nev"])
    return eredmeny

if __name__ == "__main__":
    print("Atlagos szuletesi ev:", atlagos_szuletesi_ev(tanulok))
    print("Atlagos pontszam:", atlagos_pontszam(tanulok))
    print("Nyelvek gyakorisaga:", nyelvek_gyakorisaga(tanulok))
    print("Legjobb tanulo atlaga:", legjobb_tanulo(tanulok))
    print("100-as tanulok:", szazas_tanulok(tanulok))

