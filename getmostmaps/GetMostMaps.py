class GetMostMaps(object):
    def __init__(self):
        #file containing the read counts made by the script countReadsPerTranscript
        self.path = "/home/rutgero/Desktop/referenceReadsCountedFull.txt"
        #The new file to store the reads in
        self.newPath = "/home/rutgero/Desktop/100_referenceReadsCounted.txt"
    #calculates the percentage of reads on a certain location and saves the line
    # if the percentage is above a certain point. It also checks if there are more than 500 reads in total for that reference.
    def selectMostMaps(self):
        totalCount = 0
        filterCount = 0
        file = open(self.newPath,"w")
        #a header is created.
        file.write("Reference\tTotalReads\tStartLoc\tLocationReads\tSequence")
        for line in open(self.path):
            totalCount += 1
            splitted = line.split("\t")
            #it is checked if the percentage of reads on a location is higher than 17 and if the reference
            # contains more than 500 reads in total
            if float(splitted[3])/float(splitted[1])*100 > 17 and int(splitted[1]) > 500:
                file.write(line)
                filterCount += 1
        print(totalCount, filterCount)

a = GetMostMaps()
a.selectMostMaps()