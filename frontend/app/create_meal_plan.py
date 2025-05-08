import numpy as np
import sqlite3

def meal_plan(connection):
    cursor = connection.cursor()

    choices = {'LUNCH': np.random.randint(5),
           'SNACK': np.random.randint(5),
           'DINNER': np.random.randint(5)}

    totals = {'calories': 0,
              'protein': 0,
              'fat': 0,
              'carbs': 0,
              'fibre': 0}

    for table, index in choices.items():
        sql = f"""SELECT * FROM {table} WHERE [index] = {index}"""

        result = cursor.execute(sql)
        for row in result:
            totals['calories'] += row[2]
            totals['protein'] += row[3]
            totals['carbs'] += row[4]
            totals['fat'] += row[5]
            totals['fibre'] += row[6]

    print(totals)

if __name__ == '__main__':
    con = sqlite3.connect('../database/staging.db')

    meal_plan(con)