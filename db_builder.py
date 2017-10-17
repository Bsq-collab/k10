'''
Bayan Berri 
Softdev 1 pd7
k09-- no treble
2017-10-16
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

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

db.commit() #save changes
db.close()  #close database
