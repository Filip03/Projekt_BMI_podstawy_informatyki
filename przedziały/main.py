bmi = []
category = []
choroby = []

amount_of_people = int(input('podaj liczbę osób ilu chcesz sprawdzić BMI '))
z = 1


while z < (amount_of_people + 1):
    bmi.append(int(input("podaj bmi osoby ")))
    z += 1


x = 0




while x < amount_of_people:
    if bmi[x] < 16:
        category.append(str("wygłodzenie"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    elif 16 <= bmi[x] < 17:
        category.append(str("wychudzenie"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    elif 17 <= bmi[x] < 18.5:
        category.append(str("niedowaga"))
        choroby.append(str('minimalne'))
    elif 18.5 <= bmi[x] < 25:
        category.append(str("pożadana masa ciała"))
        choroby.append(str('średnie'))
    elif 25 <= bmi[x] < 30:
        category.append(str("nadwaga"))
        choroby.append(str('wysokie'))
    elif 30 <= bmi[x] < 35:
        category.append(str("otyłosc | stopnia"))
        choroby.append(str('bardzo wysokie'))
    elif 35 <= bmi[x] < 40:
        category.append(str("otyłosc || stopnia"))
        choroby.append(str('ekstremalny poziom ryzyka'))
    elif 40 <= bmi[x]:
        category.append(str("otyłość ||| stopnia"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    else:
        category.append("bład")
    x += 1

print(category,choroby)