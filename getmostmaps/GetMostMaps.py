class GetMostMaps(object):
    def __init__(self):
        self.path = "/home/rutgero/Desktop/referenceReadsCountedFull.txt"
        self.newPath = "/home/rutgero/Desktop/100_referenceReadsCounted.txt"

    def selectMostMaps(self):
        totalCount = 0
        filterCount = 0
        file = open(self.newPath,"w")
        file.write("Reference\tTotalReads\tStartLoc\tLocationReads\tSequence")
        for line in open(self.path):
            totalCount += 1
            splitted = line.split("\t")
            if float(splitted[3])/float(splitted[1])*100 > 17 and int(splitted[1]) > 500:
                file.write(line)
                filterCount += 1
        print(totalCount, filterCount)

a = GetMostMaps()
a.selectMostMaps()