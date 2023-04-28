fajl=open("adatok.txt","w",encoding="utf-8")
def atvalto():
    print("------------------------------------------")
    krajcar = int(input("Add meg a Forint mennyiséged: "))
    print("------------------------------------------")
    k = krajcar*100
    kr = krajcar*60

    kuw = round(k/110700,4)
    bhd = round(k/90000,4)
    omr = round(k/88100,4)
    jod = round(k/47800,4)
    gbp = round(k/42300,4)
    gip = round(k/41700,4)
    kyd = round(k/40800,4)
    chf = round(k/37900,4)
    eur = round(k/37300,4)
    usd = round(k/34000,4)

    print(f"Konvenciós forint szerint Neked {kr} db krajcárod van!")
    print(f"Osztrák forint szerint Neked {k} db krajcárod van!")
    fajl.write(f"Konvenciós forint szerint Neked {kr} db krajcárod van!\n")
    fajl.write(f"Osztrák forint szerint Neked {k} db krajcárod van!\n")

    print("------------------------------------------------")
    print("-----------Top 10 Valuta-----------")
    print(f"Neked {kuw} db Kuwaiti dínárod van!")
    print(f"Neked {bhd} db Bahreini dínárod van!")
    print(f"Neked {omr} db Ománi rialod van!")
    print(f"Neked {jod} db Jordániai dínárod van!")
    print(f"Neked {gbp} db Angol fontod van!")
    print(f"Neked {gip} db Gibraltári fontod van!")
    print(f"Neked {kyd} db Kajmán-Szigeteki dollárod van!")
    print(f"Neked {chf} db Svájci frankod van!")
    print(f"Neked {eur} db Euród van!")
    print(f"Neked {usd} db Dollárod van!")

atvalto()


fajl.close()