import os
import shutil
import csv
from pathlib import Path

def readCSV(fileName):
  records = []
  with open(fileName, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          records.append(row)
  return records

images = readCSV('ImageFamily.csv')
print(images)

image_folder = str(Path('C:', '/', 'NSCF', 'ImageMove'))
print(image_folder)
family_folder = "C:\NSCF\Families"
#family_folder = str(Path('C:', '/', 'NSCF', 'Families'))
print(family_folder)


# iterate files
for image in images:
    imageName = image['Barcode'] + '.jpg'
    familyName =image['Family'] 
    print(imageName)
#construct full file path
    source = image_folder + '/' + imageName
    #destination = os.path.join(family_folder, familyName)
    destination = family_folder + '/' + familyName
    print(destination)

#test if family folder exists - if not create and then move
    # if not os.path.exists(destination):
    #     os.mkdir(destination)
#move file
    shutil.move(source, destination) 
    print('Moved:', image['Barcode'])

#example code
# path = os.path.join(parent_dir, new_dir)
# if not os.path.exists(path):
#    os.mkdir(path)
# # check if file exist in destination
# if os.path.exists(dst_folder + file_name):
#     # Split name and extension
#     data = os.path.splitext(file_name)
#     only_name = data[0]
#     extension = data[1]
#     # Adding the new name
#     new_base = only_name + '_new' + extension
#     # construct full file path
#     new_name = os.path.join(dst_folder, new_base)
#     # move file
#     shutil.move(src_folder + file_name, new_name)
# else:
#     shutil.move(src_folder + file_name, dst_folder + file_name)