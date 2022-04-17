import csv
import shutil
import os
source = "Mixed"
destination = "Sorted"
with open('Mixed_Families.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    header = []
    header = next(readCSV)
    rows = []
    for row in readCSV:
        filename = row[0] + ".jpg"
        image = os.path.join(source, filename)
        target = row[1]
        destDir = os.path.join(destination, target)
        if not os.path.exists(destDir):
            os.makedirs(destDir)
        #if os.path.exists(destDir):
        try:
            destFile = os.path.join(destDir, filename)
            shutil.copyfile(image, destFile)
        except Exception as e:
            print(e)