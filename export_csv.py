import csv
import psycopg2


OUTPUT_FILE_T = 'student01_DB_{}.csv'

TABLES = [
    'food',
    'food_types',
    'energy_values_of_food',
]

conn = psycopg2.connect(database="dbname", user="student", password="student", host="localhost", port=5432)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])

 
