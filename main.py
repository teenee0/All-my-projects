import csv
import xlwings as xw
import numpy as np
import pandas as pd

data = pd.read_csv('recipes_sample.csv')
data = data.drop(['contributor_id', 'n_steps'], axis=1)



data1 = pd.read_csv('reviews_sample.csv')


len = data.shape[0]
len2 = data1.shape[0]
new_data = data.loc[np.random.randint(0,len,int(len*0.05))]
new_data2 = data1.loc[np.random.randint(0,len2,int(len2*0.05))]
salary_sheets = {'Рецепты': new_data, 'Отзывы': new_data2}
writer = pd.ExcelWriter('recipes.xlsx',engine='xlsxwriter')

for sheet_name in salary_sheets.keys():
    salary_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name,index=False)
writer.save()
wb = xw.Book('recipes.xlsx')
sht = wb.sheets['Рецепты']
sht2 = wb.sheets['Отзывы']
new_data["seconds_assign"] = new_data["minutes"]*30
sht.range('G1').options(index=False).value = new_data["seconds_assign"]
frml = xw.Range('H2:H1501').formula = '=C2*30'
sht.range("H1").value = "seconds_formula"
sht.range('A1:I1').api.Font.Bold = True
for i in range(2,1502):
    if int(sht.range((i, 3)).value)< 5:
        sht.range((i, 3)).color = (42, 254, 44)
    elif 10 > int(sht.range((i, 3)).value) >= 5:
        sht.range((i, 3)).color = (239, 255, 99)
    elif int(sht.range((i, 3)).value) >= 10:
        sht.range((i, 3)).color = (255, 99, 99)

def validate():
    recipe_id = sht['B:B'][1:].value
    for i, el in enumerate(sht2['A2'].expand().value):
        if el[2] not in recipe_id or not el[4] in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]:
            st = f'A{i+1}' + ':' + f'F{i+1}'
            sht2.range(st).color = (255, 0, 0)


validate()