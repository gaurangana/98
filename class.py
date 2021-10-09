def countWordsFromFile():
    fileName= input("enter the file name")
    numberOfWords= 0

    file= open(fileName,'r')
    for line in file :
        words=line.split(',')
        print(words) 
        numberOfWords+= len(words)
    print(numberOfWords)
 

countWordsFromFile()