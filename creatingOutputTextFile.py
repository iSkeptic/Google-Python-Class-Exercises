def main():
    fileName = "output.txt"
    outFile = open(fileName, 'w')

    firstName = "aaaa"
    lastName = "bbbbb"
    ID = 12345

    allStrings = firstName  + " " + lastName + " " + str(ID)

    outFile.write(allStrings)
    outFile.close()

if __name__ == '__main__':
    main()
