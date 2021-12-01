import csv
import psycopg2


INPUT_CSV_FILE = 'calories.csv'

query_delete = '''

DROP TABLE food CASCADE 

'''

query_create = '''
CREATE TABLE food (
    food_id SERIAL PRIMARY KEY  ,
	food_name VARCHAR(80),
	food_weight_in_grams INT,
	food_type_id INT REFERENCES food_types(food_type_id)
);
'''

query = '''
INSERT INTO food (food_name, food_weight_in_grams) VALUES (%s, %s)
'''

conn = psycopg2.connect(database="dbname", user="student", password="student", host="localhost", port=5432)

with conn:
    cur = conn.cursor()
    cur.execute(query_delete)
    cur.execute(query_create)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
                row['per100grams'] = row['per100grams'][:-1]
                if(row['per100grams'][-1] == 'm'):
                    row['per100grams'] = row['per100grams'][:-1]
                values = (row['FoodItem'], row['per100grams'])
                cur.execute(query, values)

    conn.commit()
