#Team BerrYe
#Bayan Berri, Helen Ye
#SoftDev1 pd7
#hw10: Average
#2017-10-16
import sqlite3
import csv

f= "discobandit.db"

db= sqlite3.connect(f)
c=db.cursor()

#==============~~~using csv module~~~=================
ppls= open("peeps.csv")
peeps= csv.DictReader(ppls)

crses= open("courses.csv")
courses= csv.DictReader(crses)

#==========================================================

#~~~~~~~~~~~~~~~~~~creating tables~~~~~~~~~~~~~~~~~~~             
command= "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

command= "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

#~~~~~~~~~~~~~~~~~~populating tables~~~~~~~~~~~~~~~~~~~
def populate(dictionary, tbln, col1,col2,col3):
    for each in dictionary:
        add= "INSERT INTO "+ tbln + " VALUES ('" + each[col1] + "'," + each[col2] + "," + each[col3] + ")"
        c.execute(add)

populate(peeps,'peeps', 'name','age','id')
populate(courses,'courses', 'code','mark','id')

#==========================================================
###Do Now-- prediction: prints the table with name, ppl id, mark
q= "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id=courses.id"

foo= c.execute(q)
# print foo #>sqlite3.cursor object at 0xfioadjkngreds>
#print foo.fetchall()#prints list of all values

# Fxn will take the cursor returned from the query in the database

def lookup(student):
    q= "SELECT name, peeps.id,mark FROM peeps, courses WHERE peeps.id = "+studentID
    return c.execute(q)
    

def avg(studentID):
    ctr=0
    total=0
    for each in lookup(studentID):
        total+= each[2]
        ctr+=1
    return float(total)/ctr

def display(studentID):
    for each in lookup(studentID):
        print "Name: " + str(each[0]) + "\nID: " + str(each[1]) + "\nAverage: " + \
            str(int(100.0 * total/ctr)/100.0)

command = "CREATE TABLE peeps_avg(Peeps INTEGER, Average INTEGER)"
c.execute(command)

def populate2():
    cursor= "SELECT id FROM peeps"
    for each in cursor:
        add= "INSERT INTO peeps_avg VALUES ('" + each[0] + "'," + avg(each[0]) ")"
        c.execute(add)
populate2()

def update_average(studentID,newVal):
    q= "UPDATE peeps_csv SET Average="+newVal+"WHERE id= "+studentID
    c.execute(q)

def add_row(course, mark, studentID):
    q = "INSERT INTO courses VALUES (" + course + "," + mark + "," + studentID
    c.execute(q)

def averages(cursor):
    # Start from the first student
    student = 1
    # Initialize
    total = 0
    ctr = 0
    for each in cursor:

        while each[1]== student:
            total+=each[2]
            ctr+=1
        float(total)/ctr
        student+=1
        # If the student remains the same, just add to their mark total
        # and increment the counter
        if each[1] == student:
            total += each[2]
            ctr+=1

        # Otherwise, when the student changes, print the old student's info
        # and start calculating the next student's info
        else:
            print "Name: " + str(each[0]) + ", ID: " + str(each[1]) + ", avg: " + \
                  str(int(100.0 * total/ctr)/100.0)
            total = each[2]
            ctr = 1
            student = each[1]

averages(foo)

db.commit() #save changes
db.close()  #close database
