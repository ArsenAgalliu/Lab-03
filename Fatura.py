cmimi = float(input("Cmimi (Lek): "))
sasia = int(input("Sasia (copë): "))

if sasia < 0:
    print("Sasia e pavlefshme")
    exit()

karta = input("Ke kartë studenti? (po/jo): ")

nenshuma = cmimi * sasia
zbritje = 0

if karta.lower() == "po":
    zbritje = nenshuma * 0.10

tvsh = (nenshuma - zbritje) * 0.15
totali = nenshuma - zbritje + tvsh

print("------------------------------")
print(f"Nën-total: {round(nenshuma, 2)} Lek")
print(f"Zbritja: 10% (Vlera: {round(zbritje, 2)} Lek)")
print(f"TVSH (15%): {round(tvsh, 2)} Lek")
print(f"Totali për pagesë: {round(totali, 2)} Lek")
