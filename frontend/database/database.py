import sqlite3

con = sqlite3.connect('staging.db')

def create_tables(connection):
    """
    Creates the tables in the database
    :param connection: 
    :return: 
    """
    cur = connection.cursor()

    recipies = """
    CREATE TABLE RECIPIE
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    cook_time INTEGER,
    servings INTEGER,
    calories INTEGER,
    protein INTEGER,
    carbs INTEGER,
    fats INTEGER)"""

    ingredients = """
    CREATE TABLE INGREDIENTS
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    name TEXT,
    quantity TEXT,
    unit TEXT)"""

    meal_plan = """
    CREATE TABLE MEAL_PLANS
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME,
    meal_type TEXT,
    recipe_id INTEGER)"""

    tables = [recipies, ingredients, meal_plan]

    for table in tables:
        cur.execute(table)

