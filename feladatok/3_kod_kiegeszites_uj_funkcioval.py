"""
3. feladat - Meglevo program kiegeszitese uj funkcionalitassal (5 pont)
TODO:
Egeszitsd ki a szamfeldolgozo programot az alabbi 5 fuggvennyel (1 fuggveny = 1 pont):
1. szamjegyek_szama(szam)
   - Szamolja meg, hany szamjegy van az adott szamban (pozitiv szamokra).
   - Pl.: szamjegyek_szama(12345) -> 5
2. szamjegyek_osszege(szam)
   - Adja vissza az adott szam szamjegyeinek az osszegét.
   - Pl.: szamjegyek_osszege(123) -> 6
   - Tipp: Hasznalj rekurziot vagy ciklust.
3. faktorial(n)
   - Szamolja ki az n! erteket (n * (n-1) * (n-2) * ... * 1).
   - Pl.: faktorial(5) -> 120
   - Tipp: Hasznalj rekurziot.
4. van_szamjegy(szam, szamjegy)
   - Hatarrozza meg, hogy egy adott szamjegy szerepel-e a szamban.
   - Pl.: van_szamjegy(12345, 3) -> True
   - Tipp: Szovegge alakitva lehet egyszerubb.
5. szamok_szurese(szamok_lista, minimum, maximum)
   - Adja vissza azoknak a szamoknak a listaját, amelyek a minumum es maximum kozotti intervallumban vannak.
   - Pl.: szamok_szurese([1, 5, 10, 15, 20], 6, 18) -> [10, 15]
Kovetelmenyek:
- A program logikajat ne ird at feleslegesen.
- Hasznalj fuggvenyeket, ciklust, feltetelt es rekurziot.
"""

def szamjegyek_szama(szam):
    # TODO: valositsd meg
    return len(str(szam))

def szamjegyek_osszege(szam):
    # TODO: valositsd meg
    osszeg = 0
    for szamjegy in str(szam):
        osszeg += int(szamjegy)
    return osszeg

def faktorial(n):
    # TODO: valositsd meg (rekurzio javasolt)
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def van_szamjegy(szam, szamjegy):
    # TODO: valositsd meg
    return str(szamjegy) in str(szam)

def szamok_szurese(szamok_lista, minimum, maximum):
    # TODO: valositsd meg
    eredmeny = []
    for szam in szamok_lista:
        if minimum <= szam <= maximum:
            eredmeny.append(szam)
    return eredmeny

if __name__ == "__main__":
    # Tesztek az alabbi fuggvenyekre:
    print("Szamjegyek szama - 12345:", szamjegyek_szama(12345))
    print("Szamjegyek osszege - 123:", szamjegyek_osszege(123))
    print("Faktorial - 5:", faktorial(5))
    print("Van szamjegy 3 a 12345-ben:", van_szamjegy(12345, 3))
    print("Van szamjegy 6 a 12345-ben:", van_szamjegy(12345, 6))
    szamok = [1, 5, 10, 15, 20, 25]
    print(f"Szurt szamok [{1}, {5}, {10}, {15}, {20}, {25}] (6-18 kozott):", szamok_szurese(szamok, 6, 18))

    # Elvart eredmenyek:

    # Szamjegyek szama - 12345: 5
    # Szamjegyek osszege - 123: 6
    # Faktorial - 5: 120
    # Van szamjegy 3 a 12345-ben: True
    # Van szamjegy 6 a 12345-ben: False
    # Szurt szamok [1, 5, 10, 15, 20, 25] (6-18 kozott): [10, 15]

