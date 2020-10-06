import python-gedcom
import sys
import os
import pdfkit
key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']


levels = ['1','2','3']

text_file = open('export-BloodTree.ged', 'r')
text_file_dead = open('export-BloodTree.ged', 'r')


def printWhole(text_file):
  y = ""
  numberPriority = ""
  tag = ""

  for line in text_file:
    level_number = line[:1]

    line = line.split()

    for word in key_words:
      if word in line:

        tag = word
        y = 'Y'

    for level in levels:
        if level in line:
          numberPriority = level

    print('<-- |' + tag + '|' + numberPriority + '|' + y)
    print("-->", line)


def deadPercentage():
#maybe went overkill on the functions but it works
#create total people finder function and define a counting variable
  def totalPeople(text_file):
    peoplecount = 0;
    #for loop to scan the file
    for line in text_file:
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
    c = totalNumber/deadNumber
    print(c)

  a = deadPeople(text_file_dead)
  b = totalPeople(text_file)

  percentDead(a,b)

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
