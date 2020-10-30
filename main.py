"""
Authors: Edward and Billy 
Sprint 1 and Sprint 2 Implementation
"""

text_file = open('Guowei-Project02.ged', 'r')

def gedcom_reader_func_guowei(text_file):
  temp = ""
  for lines in text_file:
    temp = lines.split(" ", 2)
    temp[-1] = temp[-1][:-1]
    print("--> " + lines, end='')
    if temp[1] in ("NOTE", "NAME", "SEX", "FAMC", "FAMS", "HUSB", "WIFE", "CHIL", "DATE"):
      print("<-- {}|{}|Y|{}".format(temp[0], temp[1], temp[2]))
    elif temp[1] in ("BIRT", "DEAT", "MARR", "DIV"):
      print("<-- {}|{}|Y".format(temp[0], temp[1]))
    elif temp[2] in ("INDI", "FAM"):
      print("<-- {}|{}|Y|{}".format(temp[0], temp[1], temp[2]))
    else:
      print("<-- {}|{}|N|{}".format(temp[0], temp[1], temp[2]))
  return None

##User Story 1
##Estimate Manhours- 2
##Author:
##This is user story to add functionality to print all males in a genealogy (Sprint 1)
def males_in_family(text_file):
  print(text_file)
  for line in text_file:
    print(line)
    if line[1] == "NAME":
      name = line[2:]
    if line[1] == "SEX":
      if line[2] == "M":
        print(name)

##User Story 2
##Estimate Manhours- 2
##Author:
##This user story prints all the females of a family.
def females_in_family(text_file3):
  text_file = text_file3
  for line in text_file:
    if line[1] == "NAME":
      name = line[2:]
    if line[1] == "SEX":
      if line[2] == "F":
        print(name)

##User Story 3
##Estimate Manhours- 2
##Author: W_K
##This user story returns total deaths in the family
def total_deaths(text_file3):
  text_file = text_file3
  deathcount = 0
  for line in text_file:
    if line[1] == "DEAT":
      deathcount += 1
  print("The total number of deceased family members: " + str(deathcount))

##User Story 4
##Estimate Manhours- .25
##Author: ELH (copied from above)
##This user story returns total marriages in the family
def total_married(text_file3):
  text_file = text_file3
  married = 0
  for line in text_file:
    if line[1] == "MARR":
      married += 1
  print("The total number of married family members: " + str(married))
##User Story 20
##Estimate Manhours- .25
##Author: ELH (copied from above)
##This user story returns total marriages in the family
##Will print all the children of a family tree, may need to be separate function.
def total_children(text_file3):
  text_file = text_file3
  total_children = 0
  for line in text_file:
    if line[1] == "CHIL":
      total_children += 1
      print(line[2])
  print("The total number of children in this family: " + str(total_children))

##Main Function, add functions to execute below
if __name__ == "__main__":
  gedcom_reader_func_guowei(text_file)
  males_in_family(text_file)
  females_in_family(text_file)
  total_deaths(text_file)
  total_married(text_file)
  total_children(text_file)

##User Story 6
##User Story 7
##Total number of deaths in the family
##User Story 8
##Host database via MySQL or Sqlite
##One source for transforming gedcom data into sql db format
##Django Web Server
##https://sarviktaat.wordpress.com/2015/10/26/sql-and-gedcom/
##User Story 9
##User Story to Reference Individuals by Family
##To be Implemented in Sprint 2
##User Story 10
##Who is the longest living relative of a family?
##To be Implemented in Sprint 2




