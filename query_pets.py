#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 10 query data from database"""


import sqlite3 as lite
import sys


try:
    con = lite.connect('pets.db')
    cur = con.cursor()

    while True:
        id_num = raw_input("Enter person ID number: ")
        if int(id_num) == -1:
            print "Exiting . . ."
            sys.exit(1)
        elif int(id_num) < 0:
            print "Invalid number."
            continue
        elif int(id_num) > 0:
            cur.execute("SELECT * FROM person WHERE id=?", id_num)
            person = cur.fetchone()

            if person is None:
                print "Person does not exist. Please enter another ID."
                continue
            else:
                print "Person: ", person
                cur.execute("SELECT pet_id FROM person_pet WHERE person_id=?",
                            id_num)
                find_pet = cur.fetchone()
                cur.execute("SELECT * FROM pet WHERE id=?", find_pet)
                print "Pet: ", cur.fetchone(), '\n'
                continue
    cur.close()
    con.commit()

except lite.Error, e:
    if con:
        con.rollback()
    print "Error: {}".format(e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
