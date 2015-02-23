#joey weate
import csv, sqlite3

def load_course_database(db_name, csv_filename):
    with open('csv_filename', 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: