try:
    pikezimi_str = input("Shkruani pikëzimin (0–100): ")
    pikezimi = int(pikezimi_str)

    if pikezimi < 0 or pikezimi > 100:
        print('Vlerë e pavlefshme')
    elif pikezimi >= 90:
        print('Shkëlqyeshëm')
    elif pikezimi >= 75:
        print('Shumë mirë')
    elif pikezimi >= 60:
        print('Mirë')
    elif pikezimi >= 40:
        print('Mjaftueshëm')
    else:
        print('Dobët')

except ValueError:
    print("Ju lutem shkruani një numër të vlefshëm për pikëzimin.")