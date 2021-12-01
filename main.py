import psycopg2
import matplotlib.pyplot as plt

query_1 = ''' 
CREATE VIEW FoodTypeName as 
SELECT DISTINCT(ft.food_type_name),COUNT(f.food_name) FROM food f  JOIN food_types ft ON f.food_type_id = ft.food_type_id   GROUP BY ft.food_type_name
'''

query_2 = '''
CREATE VIEW CaloriesAndFoodName as
SELECT f.food_name, SUM(Cals_per100grams) AS sum_of_calories  FROM food f  JOIN energy_values_of_food e  ON f.food_id = e.food_id
GROUP BY f.food_name
'''

query_3 = '''
CREATE VIEW FoodTypeNameToCalories as 
SELECT ft.food_type_name,e.Cals_per100grams FROM food f  JOIN food_types ft ON f.food_type_id = ft.food_type_id JOIN energy_values_of_food e ON  f.food_id = e.food_id  '''

connection = psycopg2.connect(database="dbname", user="student", password="student", host="localhost", port=5432)



with connection:

    cursor = connection.cursor()
    cursor.execute('DROP VIEW IF EXISTS FoodTypeName')
    cursor.execute(query_1)
    cursor.execute('SELECT * FROM FoodTypeName')
    record1 = cursor.fetchall()

    cursor.execute('DROP VIEW IF EXISTS CaloriesAndFoodName')
    cursor.execute(query_2)
    cursor.execute('SELECT * FROM CaloriesAndFoodName')
    record2 = cursor.fetchall()

    cursor.execute('DROP VIEW IF EXISTS FoodTypeNameToCalories')
    cursor.execute(query_3)
    cursor.execute('SELECT * FROM FoodTypeNameToCalories')
    record3 = cursor.fetchall()

    helpingArr = {}
    for i in range(len(record1)):
        helpingArr[record1[i][0]] = record1[i][1]

    plt.bar(helpingArr.keys(), helpingArr.values(), width=0.5)
    plt.xlabel('Типи їжі')
    plt.ylabel('Кількість')
    plt.show()

    helpingArr = {
        'Applesauce': record2[0][1],
        'Baked Potato': record2[1][1],
        'Acai': record2[2][1],
        'Canned Blueberries': record2[3][1],
        'Canned Blackberries': record2[4][1],
        'Canned Cherries': record2[5][1],
        'Apple': record2[6][1],
        'Canned Apricots': record2[7][1],

    }

    fig, ax = plt.subplots()
    ax.pie(helpingArr.values(), labels=helpingArr.keys(), autopct='%1.1f%%', shadow=True, rotatelabels=True)
    plt.show()

    helpingArr = {}
    for i in range(len(record3)):
        helpingArr[record3[i][0]] = record3[i][1]

    fig, ax = plt.subplots()
    ax.plot(helpingArr.keys(), helpingArr.values(), )

    plt.xlabel('Type of Food')
    plt.ylabel('Number of Cal')
    plt.show()