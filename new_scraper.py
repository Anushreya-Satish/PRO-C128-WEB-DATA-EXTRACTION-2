from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page_request = requests.get(START_URL)

soup = BeautifulSoup(page_request.text, "html.parser")

table = soup.find_all('table', {"class":"wikitable sortable"})

all_table = len(table)

temp_list = []

table_rows = table[1].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Brown_Dwarf = []
Constellation =[]
Right_ascension = []
Declination =[]
Apparent_magnitude = []
Distance = []
Spectral_type = []
Mass = []
Radius =[]
Discovery_year = []

for i in range(1,len(temp_list)):
    
    Brown_Dwarf.append(temp_list[i][1])
    Constellation.append(temp_list[i][2])
    Right_ascension.append(temp_list[i][3])
    Declination.append(temp_list[i][4])
    Apparent_magnitude.append(temp_list[i][5])
    Distance.append(temp_list[i][6])
    Spectral_type.append(temp_list[i][7])
    Mass.append(temp_list[i][8])
    Radius.append(temp_list[i][9])
    Discovery_year.append(temp_list[i][10])

headers = ['Brown_Dwarf','Constellation','Right_ascension','Declination', 'Apparent_magnitude', 'Distance', 'Spectral_type', 'Mass', 'Radius', 'Discovery_year']  
df2 = pd.DataFrame(list(zip(Brown_Dwarf,Constellation,Right_ascension ,Declination, Apparent_magnitude, Distance, Spectral_type, Mass, Radius, Discovery_year)),columns=headers)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")