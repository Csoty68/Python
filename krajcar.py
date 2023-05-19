#---------------------1. Program---------------------

fajl=open("adatok.txt","a",encoding="utf-8")

def atvalto():
    print("------------------------------------------")
    krajcar = int(input("Add meg a Forint mennyiséged: "))
    print("------------------------------------------")
    k = krajcar*100

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

    print(f"Forint szerint Neked {k} db krajcárod van!")
    fajl.write(f"\n{krajcar}FT \t {k}KR")

    print("------------------------------------------------")
    print("-----------Top 10 Valuta-----------")
    print(f"Neked {kuw} db Kuwaiti dínárod van!")
    fajl.write(f"\t{kuw}KD\t")
    print(f"Neked {bhd} db Bahreini dínárod van!")
    fajl.write(f"\t{bhd}BD\t")
    print(f"Neked {omr} db Ománi rialod van!")
    fajl.write(f"\t{omr}RO\t")
    print(f"Neked {jod} db Jordániai dínárod van!")
    fajl.write(f"\t{jod}JD\t")
    print(f"Neked {gbp} db Angol fontod van!")
    fajl.write(f"\t{gbp}GBP\t")
    print(f"Neked {gip} db Gibraltári fontod van!")
    fajl.write(f"\t{gip}GIP\t")
    print(f"Neked {kyd} db Kajmán-Szigeteki dollárod van!")
    fajl.write(f"\t{kyd}KYD\t")
    print(f"Neked {chf} db Svájci frankod van!")
    fajl.write(f"\t{chf}CHF\t")
    print(f"Neked {eur} db Euród van!")
    fajl.write(f"\t{eur}EUR\t")
    print(f"Neked {usd} db Dollárod van!")
    fajl.write(f"\t{usd}USD\t")
    print("------------------------------------------------")

atvalto()

fajl.close()

