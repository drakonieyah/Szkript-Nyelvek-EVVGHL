#Random név és faktoriális 

##Leírás
A program véletlenszerű neveket és faktoriálisok értékét generálja egy grafikus felületen. Ezeket az adatokat feldolgozza és tárolja.

##Használt modulok:
1. **data_utils_TB.py** (Saját modul):
   - `CustomHandler_TB`: Egy osztály amely tárolja és lekéri az adatokat.
   - `process_data_TB`: Adatok feldolgozásához használt függvény (visszaadja minden elem hosszát).

2. **imported_module.py** (Tanult modul):
   - `factorial(n)`: Egy rekurzív függvény ami megadja egy szám faktoriálisát.

3. **random** (Bemutatandó modul):
   - `choice`: Véletlenszerűen választ egy elemet a listából.
   - `randint`: Véletlenszerűen generál egy számot.
   - `shuffle`: Véletlenszerűen megkever egy listát.

##Osztályok:
- `CustomHandler_TB`: Az adatok tárolását és gyűjtését valósítja meg.

##Esemény kezelés
- Gombok segítségével tudunk véletlenszerű neveket, illetve faktoriálisokat generálni, valamint gomb lenyomással lépünk ki a programból.

##Indítás:
1. Futtasd a `main.py` fájlt.
2. Gombok lenyomásával véletlenszerű adatokat és faktoriálisokat generálhatsz.
