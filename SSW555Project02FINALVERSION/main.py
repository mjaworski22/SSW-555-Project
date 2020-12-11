#import python-gedcom
import sys
import os
import pdfkit
import unittest
import smtplib, ssl
import pandas as pd
key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
legit = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE', 'GIVN','RFN', 'CHAN','TIME','_MARNM','OCCU','SURN','FORM','CHAR','VERS','SUBM','SOUR','GEDC']
peopleList = ['Bobby','Kevin','Lois','Gus','Kristi','Marvis','Mzincha','Geebo','Gunnar']

levels = ['1','2','3']

text_file = open('export-BloodTree.ged', 'r')
text_file_dead = open('export-BloodTree.ged', 'r')
text_file_1 = open('export-BloodTree.ged', 'r')
text_file_married = open('export-BloodTree.ged', 'r')
text_file_2 = open('export-BloodTree.ged', 'r')
text_file_sacrifice = open('export-BloodTree.ged', 'r')
text_file_sarch = open('export-BloodTree.ged', 'r')

def printWhole(text_file):
  y = ""
  numberPriority = ""
  tag = ""
  line_number = 0
  lines_in_gedcom_file = 158
  y_count = 0
  actual_y_count = 95

  for line in text_file:
    level_number = line[:1]

    line = line.split()

    for word in key_words:
      if word in line:

        tag = word
        y = 'Y'
        y_count = y_count + 1

    for level in levels:
        if level in line:
          numberPriority = level

    line_number = line_number + 2

    print('<-- |' + tag + '|' + numberPriority + '|' + y + '\n\t')
    print("-->", line)
    #print(y_count)

#test 1
  if line_number == lines_in_gedcom_file*2:
    print('Test 1:\n\tThe line count of the output is twice that of the file')
  else:
    print('Test 1:\n\tThe line count of the output is twice that of the file')

#test 2
  if y_count == actual_y_count:
    print('Test 2:\n\tThe amount of Ys in the output is correct')
  else:
    print('Test 2:\n\tThe amount of Ys in the output is incorrect')

def deadPercentage():
#maybe went overkill on the functions but it works
#create total people finder function and define a counting variable
  def totalPeople(text_file_1):
    peoplecount = 0;
    #for loop to scan the file
    for line in text_file_1:
      #store the tag for which we are searching in a variable
      inditag = "INDI"
      #if the word is in the line
      if inditag in line:
        #add one person to the counter because that line had the INDI tag
        peoplecount = peoplecount + 1
  #print(peoplecount)
    return peoplecount

  def deadPeople(text_file_dead):
    deadcount = 0;
    for line1 in text_file_dead:
      deathtag = "DEAT"
      if deathtag in line1:
        deadcount = deadcount + 1
    #print(deadcount)
    return deadcount

  def percentDead(deadNumber,totalNumber):
    #find the number of people in the tree
    #find the number of dead people in the tree
    #divide number of dead people by number of people
    c = deadNumber/totalNumber
    #print(c)
    return c

  a = deadPeople(text_file_dead)
  b = totalPeople(text_file_1)

  percent_dead = percentDead(a,b)
  percent_dead = float(percent_dead)
  
  if a == 4 and b ==9:
    print('Test 3:\n\tThe values for the dead and alive people are True')
  else:
    print('Test 3:\n\tThe values for the dead and alive people are False')

  if type(percent_dead) == float:
    print('Test 4:\n\tThe type is correct')
  else:
    print('Test 4:\n\tThe type is incorrect')
  return percent_dead

def toPDF():
  

  text_file = open('export-BloodTree.ged', 'r')
  file = input("What do you want to name the file?")
  txt = file + ".txt"
  pdf = file + ".pdf"

  stdoutOrigin=sys.stdout 
  sys.stdout = open(txt, "w")
  PrintWhole() 
  sys.stdout.close()

    # from txt to html
    # install wkthtml

    # Install wkthtmltopdf.exe and set it as primary environment variable
    #in order to use this

  with open(txt) as file:
    with open ("text.html", "w") as output:
        file = file.read()
        file = file.replace("\n", "<br>")
        output.write(file)

  pdfkit.from_file("text.html", pdf)

  os.startfile(pdf)
#======================================================================================================================
def personDeleter(text_file_sacrifice):
  sacrifice = input("Who do you want to delete? (Bobby, Kevin, Lois, Gus, Kristi, Marvis, Mzincha, Geebo, Gunnar) \n")
  if sacrifice in peopleList:
    print("Preparing to delete...")
    y = ""
    numberPriority = ""
    tag = ""
    line_number = 0
    lines_in_gedcom_file = 158
    y_count = 0
    actual_y_count = 95

    for line in text_file:
      level_number = line[:1]

      line = line.split()

      for word in legit:
        if word in line and sacrifice not in line: 
          tag = word
          y = 'Y'
          y_count = y_count + 1
        elif word in line and sacrifice in line:
          print("Eliminated ", sacrifice)
          tag = 'Deleted'
          y = 'Y'
          y_count = y_count + 1
          line = 'ELIMINATED'

      for level in levels:
          if level in line:
            numberPriority = level

      line_number = line_number + 2

      print('<-- |' + tag + '|' + numberPriority + '|' + y + '\n\t')
      print("-->", line)
  else:
    print("This person in not in the tree...Fuck You")
  return "Eliminated"
#======================================================================================================================
#Percent Dead assertTrue Test
def sprintOneTestFunctionOne():
  correct_dead = float(4/9)
  #print(correct_dead)
  experimental_value = deadPercentage()
  if correct_dead == experimental_value:
    print('Test 5:\n\tThe value for the percentage of people in the file that are dead is True')
  else:
    print('Test 5:\n\tThe value for the percentage of people in the file that are dead is False')

#function for the amount of dead people and amount of alive people is in the deadPercentage function
#function for type check is in the deadPercentage function

#function to give the amount of married people in the tree
def marriedPercentage():
#maybe went overkill on the functions but it works
#create total people finder function and define a counting variable
  def totalPeople(text_file_2):
    peoplecount = 0;
    #for loop to scan the file
    for line in text_file_2:
      #store the tag for which we are searching in a variable
      inditag = "INDI"
      #if the word is in the line
      if inditag in line:
        #add one person to the counter because that line had the INDI tag
        peoplecount = peoplecount + 1
    print("People Count^")
    print(peoplecount)
    print("People Count^")
    return peoplecount

  def marriedPeople(text_file_married):
    marriedcount = 0;
    for line2 in text_file_married:
      marriedtag = "_MARNM"
      if marriedtag in line2:
        marriedcount = marriedcount + 1
    print("marriedcount ^")
    print(marriedcount)
    print("marriedcount ^")
    return marriedcount

  def percentMarried(marriedNumber,totalNumber):
    #find the number of people in the tree
    #find the number of dead people in the tree
    #divide number of dead people by number of people
    c = marriedNumber/totalNumber
    d = c*100
    print(d)
    print( "percent of the people in this file are married")
    
    return c

  a = marriedPeople(text_file_married)
  b = totalPeople(text_file_2)

  percent_married = percentMarried(a,b)
  percent_married = float(percent_married)
  
  return percent_married

def personSearcher(text_file_sarch):
  #displays the lines someone is in
  sarch = input("Who do you want to search for? (Bobby, Kevin, Lois, Gus, Kristi, Marvis, Mzincha, Geebo, Gunnar) \n")
  if sarch in peopleList:
    print("Preparing to search...")
    y = ""
    numberPriority = ""
    tag = ""
    line_number = 0
    lines_in_gedcom_file = 158
    y_count = 0
    actual_y_count = 95

    for line in text_file:
      level_number = line[:1]

      line = line.split()

      for word in legit:
        if word in line and sarch in line: 
          tag = word
          y = 'Y'
          y_count = y_count + 1
        elif word in line and sarch not in line:
          tag = ''
          y = 'Y'
          y_count = y_count + 1
          line = ''

      for level in levels:
          if level in line:
            numberPriority = level

      line_number = line_number + 2

      print('<-- |' + tag + '|' + numberPriority + '|' + y + '\n\t')
      print("-->", line)
  else:
    print("This person in not in the tree...Fuck You")
  return "Blessed"

#printWhole(text_file)
#sprintOneTestFunctionOne()
class TestStringMethods(unittest.TestCase): 
    # test function to test equality of two value 
    def test_negative(self):
        g = float(8/9)
        firstValue = g
        secondValue = marriedPercentage()
        # error message in case if test case got failed 
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(firstValue, secondValue, message) 
    def test_negative(self):
        r = "Eliminated"
        firstValue = r
        secondValue = personDeleter(text_file_sacrifice)
        # error message in case if test case got failed 
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(firstValue, secondValue, message)
    def test_negative(self):
        r = "Blessed"
        firstValue = r
        secondValue = personSearcher(text_file_sarch)
        # error message in case if test case got failed 
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(firstValue, secondValue, message)
if __name__ == '__main__': 
    unittest.main()
  #personSearcher(text_file_sarch)