import pandas as pd

amount_of_people = int(input('podaj liczbę osób ilu chcesz sprawdzić BMI '))
if amount_of_people <= 0:
    exit()

units = str(input("wybierz jednostki 'm'-metryczne, 'i'-imperialne "))

i = 0
names = []
surnames = []
mass = []
height = []
BMI = []
category = []
choroby = []

while i < amount_of_people:
    if units != 'm' and units != 'i':
        print('nie wybrałeś jednostek')
        exit()
    names.append(str(input('podaj imie ')))
    surnames.append(str(input('podaj nazwisko ')))
    if units == 'm':
        mass.append(float(input("podaj mase w kilogramach ")))
        height.append(float(input("podaj wzrost w centymetrach ")))
    elif units == 'i':
        mass_i = float(input("podaj mase w funtach "))
        height_i = float(input("podaj wzrost w calach "))
        mass.append(mass_i * 0.45359237)
        height.append(height_i * 2.54)
    BMI.append(mass[i] / ((height[i] / 100) ** 2))
    # klasyfikacja masy ciała dorosłych na podstawie BMI
    if BMI[i] < 16:
        category.append(str("wygłodzenie"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    elif 16 <= BMI[i] < 17:
        category.append(str("wychudzenie"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    elif 17 <= BMI[i] < 18.5:
        category.append(str("niedowaga"))
        choroby.append(str('minimalne'))
    elif 18.5 <= BMI[i] < 25:
        category.append(str("pożadana masa ciała"))
        choroby.append(str('średnie'))
    elif 25 <= BMI[i] < 30:
        category.append(str("nadwaga"))
        choroby.append(str('wysokie'))
    elif 30 <= BMI[i] < 35:
        category.append(str("otyłosc | stopnia"))
        choroby.append(str('bardzo wysokie'))
    elif 35 <= BMI[i] < 40:
        category.append(str("otyłosc || stopnia"))
        choroby.append(str('ekstremalny poziom ryzyka'))
    elif 40 <= BMI[i]:
        category.append(str("otyłość ||| stopnia"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    else:
        category.append("bład")
    i += 1

df = pd.read_excel(r'Dane.xlsx')
df.insert(0, 'Imie:', names)
df.insert(1, 'Nazwisko:', surnames)
df.insert(2, 'Wzrost:', height)
df.insert(3, 'Waga:', mass)
df.insert(4, 'BMI:', BMI)
df.insert(5, 'Kategoria:', category)
df.insert(6, 'Ryzyko:', choroby)
df.to_excel('Projekt_BMI_Obliczenia.xlsx', index=False)
print(df)
