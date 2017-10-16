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
        print each
        add= "INSERT INTO "+ tbln + " VALUES ('" + each[col1] + "'," + each[col2] + "," + each[col3] + ")"
        c.execute(add)
        


populate(peeps,'peeps', 'name','age','id')
populate(courses,'courses', 'code','mark','id')

#==========================================================
###Do Now-- prediction: prints the table with name, ppl id, mark
q= "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id=courses.id"

foo= c.execute(q)
print foo #>sqlite3.cursor object at 0xfioadjkngreds>
#print foo.fetchall()#prints list of all values
for items in foo:
    print items
    

def avg(stdid):
    ctr=0
    tot=0
    q= "SELECT mark FROM courses WHERE courses.id =" + str(stdid) +";"
    g= c.execute(q)
    
    for items in g:
        tot+=items[0]
        ctr+=1
    return tot/ctr

def display():
    q= "SELECT name, id FROM peeps"
    data= c.execute(q)
    for each in data:
        print "Name: "+ each[0] + "\n ID: "+ str(each[1])+ "\nAverage: " + str(avg(each[1]))

display();


db.commit() #save changes
db.close()  #close database




