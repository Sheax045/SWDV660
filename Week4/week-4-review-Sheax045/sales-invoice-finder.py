salesInfoFile = open("sales_data.csv", "r")
firstLine = salesInfoFile.readline()
idOrLNameInput = input("Search by invoice id (id) or customer last name (lname)? ")

while (idOrLNameInput != 'id' and idOrLNameInput != 'lname'):
    print("ERROR: You must enter either 'id' for invoice id or 'lname' for customer last name search")
    idOrLNameInput = input("Search by invoice id (id) or customer last name (lname)? ")

searchTermInput = input("Enter your search term: ")

lineSum = 0

if idOrLNameInput == 'id':
    for line in salesInfoFile:
        salesData = line.split(',')
        idSearch = salesData[0]
        if searchTermInput == idSearch:
            print(line.strip())
            lineSum += 1
else:    
    for line in salesInfoFile:
        salesData = line.split(',')
        lNameSearch = salesData[2]
        if searchTermInput == lNameSearch:
            print(line.strip())
            lineSum += 1
            
print("{0} records found.".format(lineSum))
