import sqlite3
import mdpd
from sqlalchemy import Integer, String

from meals import dinner, lunch, snack


con = sqlite3.connect('staging.db')

def create_tables(connection):
    """
    Creates the tables in the database
    :param connection: 
    :return: 
    """
    cur = connection.cursor()

    meals = ['LUNCH', 'SNACK', 'DINNER']

    for meal in meals:
        recipies = f"""
            CREATE TABLE {meal}
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            protein INTEGER,
            fat INTEGER,
            carbs INTEGER,
            fibres INTEGER,
            ingredients TEXT,
            method TEXT)
        """

        cur.execute(recipies.format(meal))
        print("Created table {}".format(meal))

    meal_plan = """
    CREATE TABLE MEAL_PLANS
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME,
    meal_type TEXT,
    recipe_id INTEGER)"""

    cur.execute(meal_plan)
    print("Created table MEAL_PLANS")

def drop_tables(tables, connection):
    cur = connection.cursor()

    for table in tables:
        sql = f"""DROP TABLE {table}"""

        cur.execute(sql)
        print("Dropped table {}".format(table))


def load_tables(connection):
    data = {'DINNER': dinner, 'LUNCH': lunch, 'SNACK': snack}

    for table, meals in data.items():
        meals = meals.replace('**', '')
        df = mdpd.from_md(meals)

        df.to_sql(table, con=connection, if_exists='replace', index=True)


if __name__ == "__main__":
    tables = ['LUNCH', 'SNACK', 'DINNER', 'MEAL_PLANS']
    drop_tables(tables, con)
    create_tables(con)
    load_tables(con)