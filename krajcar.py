fajl=open("adatok.txt","w",encoding="utf-8")
def atvalto():
    print("------------------------------------------")
    krajcar = int(input("Add meg a Forint mennyiséged: "))
    print("------------------------------------------")
    k = krajcar*100
    kr = krajcar*60
    print(f"Konvenciós forint szerint Neked {kr} db krajcárod van!")
    print(f"Osztrák forint szerint Neked {k} db krajcárod van!")
    fajl.write(f"Konvenciós forint szerint Neked {kr} db krajcárod van!\n")
    fajl.write(f"Osztrák forint szerint Neked {k} db krajcárod van!\n")
atvalto()
fajl.close()