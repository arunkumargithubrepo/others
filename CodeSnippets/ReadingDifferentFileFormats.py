import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import zipfile
from bs4 import BeautifulSoup

path = r"home/arun/Documents/Datasets/"

# To read CSV
csvData = pd.read_csv(path+"national-population.csv")
print(csvData)

# To read txt
txtData = pd.read_table(path+"faculty_salary_small.txt")
print(txtData)

# To read Excel
excelData = pd.read_excel(path+"netflix_titles.xlsx")
print(excelData)

# To read json
jsonData = pd.read_json(path+"total-population-all-ages-including-armed-forces-overseas_metadata.json")
print(jsonData)

# To compress & Zip files
with zipfile.ZipFile("faculty.zip", 'w', compression=zipfile.ZIP_DEFLATED) as writeZip:
    writeZip.write(path+"faculty_salary_small.txt")
    writeZip.write(path+"faculty_salary.txt")

# # To extract zip files
with zipfile.ZipFile("faculty.zip", 'r') as extractZip:
    extractZip.extractall(".")

# To read zip files
with zipfile.ZipFile("faculty.zip", 'r') as readZip:
    print(readZip.namelist())  # Displays all files in the zip recursively
    print(readZip.read(path+'faculty_salary.txt'))

# To read XML file
with open(path+"ebay.xml", 'r') as xmlFile:
    xmlData = xmlFile.read()

xmlParser = BeautifulSoup(xmlData, "xml")
xmlParserData = xmlParser.find_all('bidder_name')  # find a specific tag
for data in xmlParserData:
    print(data.get_text())
