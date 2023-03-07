import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_can = pd.read_excel(
    "Canada.xlsx",
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True) #Видалення стовпців

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True) #зміна назв деяких стовпців

df_can['Total'] = df_can[[1980,       1981,       1982,
             1983,       1984,       1985,       1986,       1987,       1988,
             1989,       1990,       1991,       1992,       1993,       1994,
             1995,       1996,       1997,       1998,       1999,       2000,
             2001,       2002,       2003,       2004,       2005,       2006,
             2007,       2008,       2009,       2010,       2011,       2012]].sum(axis=1) # Додаваннянового стовпця для підсумку загальної кількість іммігрантів за країнами за весь період 1980-2013 років


df_can.set_index('Country', inplace=True) # Встановлення індексом Country

df_can.columns = list(map(str, df_can.columns)) # Перетворення назв стовпців у з int у string

years = list(map(str, range(1980, 2014))) # Створення змінної для доступу до стовпців

#Створення графіку для 5 країн з найбільшою кількістю емігрантів в Канаду
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True) #Сортування за сопвцем Total

df_top5 = df_can.head() # Зберігання перших 5 рядків

df_top5 = df_top5[years].transpose() # Зміна рядків та стовпців місцями

df_top5.index = df_top5.index.map(int) # Зміна типу даних років на int
df_top5.plot(kind='area', # Тип графіку
             alpha=0.25,  # Зміна прозорості
             stacked=False, # Створення нестекового графіку
             figsize=(20, 10)) # Розмір графіку

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# plt.savefig('1.png')
plt.show()

#Створення графіку для 5 країн з найменшою кількістю емігрантів в Канаду
df_least5 = df_can.tail(5)


df_least5 = df_least5[years].transpose()
df_least5.head()

df_least5.index = df_least5.index.map(int)
df_least5.plot(kind='area', alpha=0.45, figsize=(20, 10))

plt.title('Immigration Trend of 5 Countries with Least Contribution to Immigration')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# plt.savefig('2.png')
plt.show()

# Гісторграма частотного розподілу кількості нових іммігрантів з різних країн до Канади у 2013 році
count, bin_edges = np.histogram(df_can['2013'])

df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)

plt.title('Histogram of Immigration from 195 countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of Immigrants')

# plt.savefig('3.png')
plt.show()

# Відображення розподілу імміграції для Греції, Албанії та Болгарії за 1980-2013 роки з використанням графік, що перекривається, з 15 відсіками і значенням прозорості 0,35
df_cof = df_can.loc[['Greece', 'Albania', 'Bulgaria'], years]

df_cof = df_cof.transpose()

count, bin_edges = np.histogram(df_cof, 15)

df_cof.plot(kind='hist',
            figsize=(10, 6),
            bins=15,
            alpha=0.35,
            xticks=bin_edges,
            color=['blue', 'green', 'yellow']
            )

plt.title('Histogram of Immigration from Greece, Albania, and Bulgaria from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

# plt.savefig('4.png')
plt.show()
#Гістограма, що показує загальну кількість іммігрантів до Канади з Ісландії
df_iceland = df_can.loc['Iceland', years]

df_iceland.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.title('Icelandic immigrants to Canada from 1980 to 2013')

# plt.savefig('5.png')
plt.show()


#Горизонтальна гістограма, що показує загальну кількість іммігрантів до Канади з 15 найбільших країн
df_can.sort_values(by='Total', ascending=True, inplace=True)

df_top15 = df_can['Total'].tail(15)

df_top15.plot(kind='barh', figsize=(12, 12), color='steelblue')
plt.xlabel('Number of Immigrants')
plt.title('Top 15 Countries Contributing to the Immigration to Canada between 1980 - 2013')

for index, value in enumerate(df_top15):
    label = format(int(value), ',')
    plt.annotate(label, xy=(value - 47000, index - 0.10), color='white')

# plt.savefig('6.png')
plt.show()