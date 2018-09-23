#basics of python

#file system
import math

import csv


f = open("C:\Users\pravin\PycharmProjects\APIframework\DATA\Export_Automation_1532581100.csv", "r")

def read_file_line_by_line():
    for line in f:
        print line


def read_file_at_atime():
    data = f.read()

    print data


# read_file_at_atime()


def read_file_close_file():
    try:
        # Open a file
        fo = open("C:/Users/pravin/PycharmProjects/APIframework/DATA/foo.txt", "r")
        print "Name of the file: ", fo.name
        data = fo.read()
        print data
    except:
        # Close opend file
        fo.close()

def direct_read_close():
    # Open a file
    fo = open("C:/Users/pravin/PycharmProjects/APIframework/DATA/foo.txt", "r")
    print "Name of the file: ", fo.name
    data = fo.read()
    print data

    # Close opend file
    fo.close()

def withopenkeywordfileopen():
    #No need to close it will take care
    #e is a file object
    with open("C:/Users/pravin/PycharmProjects/APIframework/DATA/foo.txt", "r") as e:
        for line in e:

            # print line  #Actual result

            line_strip = line.strip() #it will remove whitespace in begining and end of file
            # print line_strip

            line_replace = line.replace('"','-')
            # print line_replace

            line_trim = line.strip() #removing whitespaces \n then splitting delimetere as comma
            line_split = line_trim.split(",")
            # print line_split

            # print line_split[0].strip('"') #further we can remove quotes


def advancefilecalculation():
    total = 0
    with open("C:/Users/pravin/PycharmProjects/APIframework/DATA/foo.txt","r") as f:
        headers = next(f) # skip a single line of input
        for line in f:
            line = line.strip()
            line_split=line.split(",")
            line_split[0] = line_split[0].strip('"')  # cleaning or sanitizing data
            line_split[0] = int(line_split[0])
            total += line_split[0]   #calculation on file


            print line_split

        print total

def advancefilecalculationcsv():
    total = 0
    #C:\Users\pravins\Downloads\Export_Automation_1532581100.csv
    with open("C:/Users/pravin/PycharmProjects/APIframework/DATA/foo.csv","r") as f:
        rows = csv.reader(f)

        headers = next(rows) # skip a single line of input
        for row in rows:
            row[0] = row[0].strip("\t")
            total += int(row[0])




             #calculation on file



            print row
        print total



advancefilecalculationcsv()





















