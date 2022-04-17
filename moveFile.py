import os
import shutil
import csv
from pathlib import Path
from os.path import exists

def readCSV(fileName):
  records = []
  with open(fileName, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          records.append(row)
  return records

images = readCSV('ImageFamily.csv')
print(images)


# iterate files
for image in images:
    imageName = image['Barcode'] + '.jpg'
    familyName =image['Family'] 
    print(imageName)
#construct full file path
    image_folder = Path(r'C:\\', 'NSCF', 'ImageMove')
    print(image_folder)
    family_folder = Path(r"C:\\", 'NSCF', 'ImageMove', 'Families', familyName)
    print(family_folder)
    source = os.path.join(image_folder, imageName)
    if exists(source):
        print("source is:", source)
        destination = os.path.join(family_folder, imageName)
        print("destination is:", destination)

    #test if family folder exists - if not create and then move
        if not os.path.exists(family_folder):
            os.mkdir(family_folder)
    #move file
        shutil.move(source, destination) 
    print('Moved:', image['Barcode'])
