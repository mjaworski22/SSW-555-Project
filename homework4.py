
class Gedcom():
    def __init__(self, filename, startYear,endYear):
        self.filename = filename + ".txt"
        self.startYear = startYear
        self.endYear = endYear
    def print(self):
        f = open(self.filename,"r")
        for lines in f:
            temp = lines.split(" ",2)
            temp[-1] = temp[-1][:-1]
            print ("--> " + lines, end = '')
            if temp[1] in ("NOTE","NAME","SEX","FAMC","FAMS","HUSB","WIFE","CHIL","DATE"):
                print ("<-- {}|{}|Y|{}".format(temp[0],temp[1],temp[2]))
            elif temp[1] in ("BIRT","DEAT","MARR","DIV"):
                print ("<-- {}|{}|Y".format(temp[0],temp[1]))
            elif temp[2] in ("INDI","FAM"):
                print ("<-- {}|{}|Y|{}".format(temp[0],temp[2],temp[1]))
            else:
                print ("<-- {}|{}|N|{}".format(temp[0],temp[1],temp[2]))
        return None
    #first sprint for searching people were born in a given time frame
    def searchByYears(self):
        "The method shows how many people was born between the startyear and endyear"
        f = open(self.filename,'r')
        result = 0
        for lines in f:
            temp = lines.split(" ")
            temp[-1] = temp[-1][:-1]
            #print (temp)
            if temp[1] == "DATE":
                if int(temp[4]) >= self.startYear and int(temp[4]) <= self.endYear:
                    print("I have fund someone was born {} {} {}".format(temp[2],temp[3],temp[4]))
                    result += 1
        print("there are {} people was borned from {} to {}".format(result,self.startYear,self.endYear))
        return result

def main():
    f = Gedcom("test GEDCOM file",1950,1960)
    f.searchByYears()

if __name__ == "__main__":
    main()