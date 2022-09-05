import os
import shutil
import csv
from pathlib import Path
from os.path import exists
import click




@click.command()
@click.option('--file',  
                help='File name with image names and families e.g. ImageFamily.csv.')
@click.option('--source',  
                help='Folder where unsorted images are.')
@click.option('--dest', 
                help='The folder where images would be moved to')


# open csv file and iterate files
def moveFiles(file, source, dest):
    if source == None:
        source = os.getcwd()
    if dest == None:
        dest = os.getcwd()
    if file == None:
        print('File is required')
        return

    records = []
    try:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append(row)
        print(records)
    except Exception as e:
        print('Error reading file')
        print(e)
        return

    images = records

    for image in images:
        if image['Barcode'] != None:
            imageName = image['Barcode'] + '.jpg'
        
        if image['Family'] != None:
            familyName =image['Family'] 

        familyFolder = os.path.join(dest, familyName)
        # print(imageName)
        #construct full file path
        sourceFile = os.path.join(source, imageName)
        if exists(sourceFile):
            print("source is:", sourceFile)
            destination = os.path.join(familyFolder, imageName)
            print("destination is:", destination)

            #test if family folder exists - if not create and then move
            if not os.path.exists(familyFolder):
                os.mkdir(familyFolder)
            #move file
            shutil.move(sourceFile, destination) 
            print('Moved:', image['Barcode'])

        else:
            print("Could not find image", image['Barcode'])
    
# if __name__ == '__main__':
#     moveFiles()

moveFiles('ImageFamily.csv', 'C:/NSCF/ImageMove', 'C:/NSCF/ImageMove/Families')