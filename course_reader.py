#joey weate
import csv
import sqlite3

def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU') as file:
        reader = csv.reader(file);
        for row in reader:
            print(row);
            conn = sqlite3.connect(db_name);
            with conn:
                cur = conn.cursor();
                
                sql_cmd = "insert into db_name values(?,?,?,?,?,?,?)";
                cur.execute(sql_cmd, (row[0], row[1],row[2],row[3],row[4],row[5],row[6])); # value of dept used for the first ?, and courseNum for the 2nd


load_course_database('course1.db','seas-courses-5years.csv');