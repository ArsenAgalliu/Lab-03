try:
    numri_str = input("Shkruani një numër të plotë: ")
    numri = int(numri_str)

    if numri % 2 == 0:
        print('Çift')
    else:
        print('Tek')

except ValueError:
    print("Ju lutem shkruani një numër të vlefshëm.")