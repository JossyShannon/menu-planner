import numpy as np
import sqlite3
import pandas as pd

def meal_plan():
    connection = sqlite3.connect('frontend/database/staging.db')

    cursor = connection.cursor()

    choices = {
        'BREAKFAST': np.random.randint(5),
        'LUNCH': np.random.randint(5),
        'SNACK': np.random.randint(5),
        'DINNER': np.random.randint(5)
               }

    totals = {'calories': 0,
              'protein': 0,
              'fat': 0,
              'carbs': 0,
              'fibre': 0}

    df = pd.DataFrame()

    sql = f"""
    SELECT * FROM 'BREAKFAST' WHERE [index] = {np.random.randint(5)}
    UNION ALL
    SELECT * FROM 'LUNCH' WHERE [index] = {np.random.randint(5)}
    UNION ALL
    SELECT * FROM 'SNACK' WHERE [index] = {np.random.randint(5)}
    UNION ALL
    SELECT * FROM 'DINNER' WHERE [index] = {np.random.randint(5)}
"""

    result = cursor.execute(sql)

    plan = pd.DataFrame(result.fetchall())

        #for row in result:
        #    plan[table] = row
        #    totals['calories'] += int(row[2])
        #    totals['protein'] += int(row[3])
        #    totals['fat'] += int(row[4])
        #    totals['carbs'] += int(row[5])
        #    totals['fibre'] += int(row[6])

    return totals, plan
