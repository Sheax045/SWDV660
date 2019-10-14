def getTextFile():
    fileName = input("Enter the text file name: ")
    textFile = open( fileName, 'r' )
    return fileName, textFile

def outputCountResults( fileName, lineCount, wordCount, charCount, nonArtWordCount ):
    print()
    print( "******* {} *******".format( fileName ))
    print( "Total Lines: {}".format( lineCount ))
    print( "Total Chars: {}".format( charCount ))
    print( "Total Words: {}".format( wordCount ))
    print( "Total Non-Article Words: {}".format( nonArtWordCount))
    
def countNonArtWords(line):
    nonArtWordCount = 0
    words = line.split()
    if len(words) == 0:
        nonArtWordCount = nonArtWordCount + 0
    else:
        for word in range (len(words)):
            if words[word] not in ("A", "a", "An", "an", "AN", "aN", "The", "the", "THE", "tHe", "thE", "THe", "ThE", "tHE"):
                nonArtWordCount = nonArtWordCount + 1
            else:
                nonArtWordCount = nonArtWordCount + 0
                
    return nonArtWordCount

def countCharacters(line):
    charCount = 0
    for c in line:
        if not c.isspace():
            charCount = charCount + 1
    return charCount
    
def countWords( line ):
    words = line.split()
    return len( words )

def countDocStats( docFile ):
    lineCount = 0
    totalCharacters = 0
    totalWords = 0
    totalNonArtWords = 0
    for line in docFile:
        lineCount = lineCount + 1
        totalCharacters = totalCharacters + countCharacters( line )
        totalWords = totalWords + countWords( line )
        totalNonArtWords = totalNonArtWords + countNonArtWords( line )
    return lineCount, totalCharacters, totalWords, totalNonArtWords

def main():
    fileName, textFile = getTextFile()
    lineCount, totalCharacters, totalWords, nonArtWordCount = countDocStats( textFile )
    outputCountResults( fileName, lineCount, totalWords, totalCharacters, nonArtWordCount )
    
main()
