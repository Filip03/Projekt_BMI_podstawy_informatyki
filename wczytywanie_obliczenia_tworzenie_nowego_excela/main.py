import pandas as pd

df = pd.read_excel(r"dane_do_BMI.xlsx")

names = df[['Imie:']]
surnames = df[['Nazwisko:']]
height = df[['Wzrost:']]
mass = df[['Waga:']]
category = []
waga_ciala = []
choroby = []
kolor = []

x = 0
y = 1
amount_of_people = len(names)

df.insert(4, 'BMI:', df['Waga:'] / ((df['Wzrost:'] / 100) ** 2))

lista = df['BMI:'].tolist()

while x<amount_of_people:
    if lista[x] < 16:
        category.append(str("wygłodzenie"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    elif 16 <= lista[x] < 17:
        category.append(str("wychudzenie"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    elif 17 <= lista[x] < 18.5:
        category.append(str("niedowaga"))
        choroby.append(str('minimalne'))
    elif 18.5 <= lista[x] < 25:
        category.append(str("pożadana masa ciała"))
        choroby.append(str('średnie'))
    elif 25 <= lista[x] < 30:
        category.append(str("nadwaga"))
        choroby.append(str('wysokie'))
    elif 30 <= lista[x] < 35:
        category.append(str("otyłosc | stopnia"))
        choroby.append(str('bardzo wysokie'))
    elif 35 <= lista[x] < 40:
        category.append(str("otyłosc || stopnia"))
        choroby.append(str('ekstremalny poziom ryzyka'))
    elif 40 <= lista[x]:
        category.append(str("otyłość ||| stopnia"))
        choroby.append(str('minimalne, ale zwiększony poziom wystąpienia innych problemów zdrowotnych'))
    else:
        category.append("bład")
    x += 1

df.insert(5, 'Kategoria:', category)
df.insert(6, 'Ryzyko:', choroby)

df.to_excel('Obliczone_BMI.xlsx', index=False)
