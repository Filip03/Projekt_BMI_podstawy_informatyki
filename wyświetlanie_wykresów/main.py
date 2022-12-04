import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

df = pd.read_excel(r"Obliczone_BMI.xlsx")
df = df.sort_values(by='BMI:')

sns.relplot(x='Waga:',
            y='Wzrost:',
            aspect=2,
            height=8,
            data=df,
            hue='Imie:',
            kind='scatter')

plt.show()
sns.set_theme(style="darkgrid")

f, ax = plt.subplots(figsize=(25, 12))
cols = ['#082E79' if (x < 16) else '#4169E1' if (16 <= x < 17) else '#ACE1AF' if (17 <= x < 18.5)
        else '#CDEBA7' if (18.5 <= x < 25) else '#FFFF99' if (25 <= x < 30) else '#FDE456' if (30 <= x < 35)
        else '#CF2929' if (35 <= x < 40) else '#801818' if (x > 40) else 'orange' for x in df['BMI:']]

sns.barplot(x="BMI:", y="Imie:", data=df, palette=cols, width=1.1)
blue = mpatches.Patch(color='#082E79', label='wygłodzenie')
light_blue = mpatches.Patch(color='#4169E1', label='wychudzenie')
green = mpatches.Patch(color='#ACE1AF', label='niedowaga')
light_green = mpatches.Patch(color='#CDEBA7', label='pożadana masa ciała')
light_yellow = mpatches.Patch(color='#FFFF99', label='nadwaga')
yellow = mpatches.Patch(color='#FDE456', label='otyłosc | stopnia')
light_red = mpatches.Patch(color='#CF2929', label='otyłosc || stopnia')
red = mpatches.Patch(color='#801818', label='otyłość ||| stopnia')
ax.legend(handles=[blue, light_blue, green, light_green, light_yellow, yellow, light_red, red])
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
ax.bar_label(ax.containers[0])






plt.show()
