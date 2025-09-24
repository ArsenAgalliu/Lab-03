def llogarit_cmimin_perfundimtar(diametri, cmimi_fillestar):
    if diametri >= 30:
        cmimi_perfundimtar = int(cmimi_fillestar * 1.10)
    else:
        cmimi_perfundimtar = cmimi_fillestar
    print(f"Cmimi perfundimtar: {cmimi_perfundimtar}Lek")

llogarit_cmimin_perfundimtar(28, 600)
llogarit_cmimin_perfundimtar(30, 600)
llogarit_cmimin_perfundimtar(35, 700)