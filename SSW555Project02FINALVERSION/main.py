#import python-gedcom
import sys
import os
import pdfkit
key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']


levels = ['1','2','3']

text_file = open('export-BloodTree.ged', 'r')
text_file_dead = open('export-BloodTree.ged', 'r')
text_file_1 = open('export-BloodTree.ged', 'r')


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

    print('<-- |' + tag + '|' + numberPriority + '|' + y)
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

#Doing some tests for sprint one here
#maybe the test function requirements went right over my head

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

printWhole(text_file)
sprintOneTestFunctionOne()