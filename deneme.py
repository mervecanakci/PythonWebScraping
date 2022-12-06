import requests #!pip install requests
from bs4 import BeautifulSoup #!pip install beautifulsoup4

karray=[]
headers = []
def get_soup(TARGET_URL):
    page = requests.get(TARGET_URL)
    soup = BeautifulSoup(page.text, 'html.parser')

    for k in soup.find_all("table",attrs={'class':'bordertlrb'}):
        m=(k.text).rstrip("\n")
        karray.append(m)

    return soup

URL = 'http://www.informatik.uni-bremen.de/rev_lib/realizations.php?lib=1'

href=[]

def get2_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    for k in soup.find_all("a"):
        href.append(k)

file_href=[] #tabloda file sütunu altında olan linkleri tutuyor
#pic_href=[]     #tabloda pic sütunu altında olan linkleri tutacak
ref_href=[]     #tabloda ref sütünu altında olan linkelri tutuyor
realizes_href=[]    #tabloda realizes sütunu altında olan linkleri tutuyor

get2_soup(URL)
for hr in href:
    if hr['href'].startswith("doc") and hr['href'].endswith(".real") :      #başı doc olup sonu .real ile bitenler i alıp file içine atıyorum çünkü file ı diğerlerinden ayıran özelliği bu
        index = "http://www.informatik.uni-bremen.de/rev_lib/" + hr['href']
        file_href.append(index)
for hr in href:
    if hr['href'].startswith("function"):       #başı function olanlar özgün özellik
        index = "http://www.informatik.uni-bremen.de/rev_lib/" + hr['href']
        realizes_href.append(index)
for hr in href:
    if hr['href'].startswith("paper"):          #başı paper olanlar özgün özellik
        index = "http://www.informatik.uni-bremen.de/rev_lib/" + hr['href']
        ref_href.append(index)

"""for hr in href:
    if hr['href'].endswith(".jpg"):         #sonu .jpg olanlar özgün özellik
        index = "http://www.informatik.uni-bremen.de/rev_lib/" + hr['href']
        pic_href.append(index)"""

print(file_href)
#print(pic_href)
print(ref_href)
print(realizes_href)


soup = get_soup(URL)
dkarray=[]
last=[]
dkarray =karray[0].split("\n")

for dk in dkarray:
    if not dk =='':
        last.append(dk)
    else:
        last.append(' ')

inside=[]
outside=[]

for i in range(15):
    last.pop(0)

sorgu = ""
for k in range(len(last)):
    if(k+8)%15==0:
        print(file_href[int(k/15)],end = " , ")
    elif(k+7)%15==0:
        try:
         print(realizes_href[int(k/15)],end = " , ")
        except:
            pass

    elif last[k] == ' ':
        print("X",end = " , ")
    else:
        print(last[k],end = " , ")

    if (k+1)%15 == 0 :
        print("\n")
        #satir bitti

print("asd")
print(last)

i=-1
k=-1

for ll in last:
    i = i + 1
    #print(ll)

for n in outside:
 print(n)
print(outside)

"""
import xlsxwriter

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

row = 0

for col, data in enumerate(outside):
    worksheet.write_column(row, col, data)

workbook.close()
"""