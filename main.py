"""
Authors: Edward Holcomb and William (Billy) Kingsberry
"""
key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
levels = ['1','2','3']
text_file = open('export-BloodTree.ged', 'r')

def gedcom_reader_func(text_file):
  y = ""
  lerp = ""
  derp = ""
  text_file = text_file
  for line in text_file:
    level_number = line[:1]
    line = line.split()
    for word in key_words:
      if word in line:
        derp = word
        y = "Y"

    for burb in levels:
      if burb in line:
        lerp = burb
    print("<-- |" + derp + "|" + lerp + "|" + y)
    print("-->", line)
##User Story 1
##Estimate Manhours- 2
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
##This user story returns total deaths in the family
def total_counts(text_file):
  deathcount = 0
  for line in text_file:
    if line[1] == "DEAT":
      deathcount += 1
  print("The total number of deceased family members: " + deathcount)
##Will print all the children of a family tree, may need to be separate function.
  if line[1] == "CHIL":
      name = line
##Main Function, add functions to execute below
if __name__ == "__main__":
  gedcom_reader_func(text_file)
  males_in_family(text_file)
  females_in_family(text_file)
  total_counts(text_file)


##Total number of deaths in the family
##Host database via MySQL or Sqlite
##User Story 9
##User Story to Reference Individuals by Family
##To be Implemented in Sprint 2
##User Story 10
##Who is the longest living relative of a family?
##To be Implemented in Sprint 2




