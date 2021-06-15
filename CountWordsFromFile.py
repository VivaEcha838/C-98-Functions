def readFilesAndCountWords():
    filename = input("Enter the file name: ")
    file = open(filename, "r")
    numberOfWords = 0

    for line in file:
        words = line.split()
        print(words)
        numberOfWords = numberOfWords + len(words)
    print("Number of Words in the file: ", numberOfWords)

    
readFilesAndCountWords()