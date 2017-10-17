#Team BerrYe
#Bayan Berri, Helen Ye
#SoftDev1 pd7
#hw10: Average
#2017-10-16

import sqlite3
import csv

# Assumes db_builder has been run and db already exists
f= "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

#==========================================================
###Do Now-- prediction: prints the table with name, ppl id, mark
q= "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id=courses.id"

foo= c.execute(q)
# print foo #>sqlite3.cursor object at 0xfioadjkngreds>
#print foo.fetchall()#prints list of all values

# Take in a student's id and return their name and grades
def lookup(studentID):
    q= "SELECT name, mark FROM peeps, courses WHERE courses.id=peeps.id AND peeps.id="+str(studentID)
    return c.execute(q)

# Take the average of the student's grades
def avg(studentID):
    ctr=0
    total=0
    student_courses = lookup(studentID)
    for each in student_courses:
        total+=each[1]
        ctr+=1
    return float(total)/ctr

# Show a student's name, id, and average
def display(studentID):
    for each in lookup(studentID):
        print "Name: " + str(each[0]) + "\nID: " + str(studentID) + "\nAverage: " + \
                str(avg(studentID))

# Given a new average and a student, change the value in the peeps_avg table
def update_average(studentID,new_val):
    q= "UPDATE peeps_avg SET Average="+str(new_val)+" WHERE Peeps= "+ str(studentID)
    c.execute(q)

# Add a course given a row of a cursor
def add_course(row):
    q = 'INSERT INTO courses VALUES ("' + row['code'] + '",' + row['mark'] + "," + row['id'] + ")"
    c.execute(q)

# Check if a course already is in the database, if not, add it and
# update student averages
def add_new_courses(filename):
    f = open(filename, 'rU')
    reader = csv.DictReader(f)
    for row in reader:
        command = 'SELECT * FROM courses WHERE code="' + row['code'] + '" AND mark=' + \
                row['mark'] + " AND id=" + row['id']
        q = c.execute(command).fetchall()
        if len(q) == 0:
            add_course(row)
            update_average(row['id'], avg(row['id']))
    f.close()

# Create the new table
command = "CREATE TABLE peeps_avg(Peeps INTEGER, Average INTEGER)"
c.execute(command)

# Populate the new table
def populate2():
    cursor= c.execute("SELECT id FROM peeps")
    for each in cursor.fetchall():
        add = "INSERT INTO peeps_avg VALUES ('" + str(each[0]) + "'," + \
                str(avg(each[0])) + ")"
        c.execute(add)

populate2()

# Students who will take more courses after the modified csv file
display(1)
display(3)

add_new_courses('updated_courses.csv')

# Check averages after adding the new classes
display(1)
display(3)

db.commit() #save changes
db.close()  #close database
