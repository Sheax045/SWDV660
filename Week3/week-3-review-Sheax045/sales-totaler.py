inputFile = input("Enter sales file name: ")
inputSales = open(inputFile, "r")
outputFileName = input("Enter name for total sales file: ")
salesData = inputSales.readlines()

for i in range(len(salesData)):
    
    splitData = salesData[i].split("$")
    #print(splitData[1:3])
    sumData = float(splitData[1]) + float(splitData[2])
    outputFile = open( outputFileName, "a" )
    print( finalData, file=outputFile )
    outputFile.close()   #print(sumData)
    totalData = splitData[1:] + [str(sumData)]
    
   
    
    chars = []
    
    for num in range(len(totalData)):
        stripData1 = str(totalData[num].strip())
        chars.append(stripData1)
        
    finalData = ("${0:>8} ${1:>8} ${2:>8}".format(chars[0], chars[1], chars[2]))
    
    print(finalData)

        
    outputFile = open( outputFileName, "a" )
    print( finalData, file=outputFile )
    outputFile.close()       
  
    
