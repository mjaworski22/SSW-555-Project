"""
Authors: Edward and Billy 
Sprint 1 and Sprint 2 Implementation
"""
text_file = open('Edward-Project02.ged', 'r')
text_file2 = open('Matt-Project02.ged', 'r')
text_file3 = open('Guowei-Project02.ged', 'r')

def gedcom_reader_func_matt(text_file):
  pass

def gedcom_reader_func_edward(text_file):
  pass

def gedcom_reader_func_guowei(text_file3):
  text_file3 = text_file
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
      print("<-- {}|{}|Y|{}".format(temp[0], temp[2], temp[1]))
    else:
      print("<-- {}|{}|N|{}".format(temp[0], temp[1], temp[2]))
  return None
##User Story 1
##Estimate Manhours- 2
##Author:
##This is user story to add functionality to print all males in a genealogy (Sprint 1)
def males_in_family(text_file):
  for line in text_file:
    if line[1] == "NAME":
      name = line[2]
    while line[2] != "M" or line[2] != "F":
      if line[2] == "M":
        print(name)
##User Story 2
##Estimate Manhours- 2
##Author:
##This user story prints all the females of a family.
def females_in_family(text_file):
  for line in text_file:
    if line[1] == "NAME":
      name = line[2]
    while line[2] != "M" or "F":
      if line[2] == "F":
        print(name)
    
##User Story 3
##Estimate Manhours- 2
##Author: W_K
##This user story returns total deaths in the family
def total_deaths(text_file):
  deathcount = 0
  for line in text_file:
    if line[1] == "DEAT":
      deathcount += 1
  print("The total number of deceased family members: " + deathcount)
##User Story 4
##Estimate Manhours- .25
##Author: ELH (copied from above)
##This user story returns total marriages in the family
def total_married(text_file):
  married = 0
  for line in text_file:
    if line[1] == "MARR":
      married += 1
  print("The total number of married family members: " + married)
##Will print all the children of a family tree, may need to be separate function.
  if line[1] == "CHIL":
      name = line
##Main Function, add functions to execute below
if __name__ == "__main__":
  gedcom_reader_func_guowei(text_file3)
  ##gedcom_reader_func_edward(text_file)
  ##gedcom_reader_func_matt(text_file)
  ##males_in_family(text_file)
  ##females_in_family(text_file)
  ##total_death(text_file)
  ##total_married(text_file)


##Total number of deaths in the family
##Host database via MySQL or Sqlite
##User Story 9
##User Story to Reference Individuals by Family
##To be Implemented in Sprint 2
##User Story 10
##Who is the longest living relative of a family?
##To be Implemented in Sprint 2




