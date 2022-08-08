from bs4 import BeautifulSoup
import re

html = """"""

soup = BeautifulSoup(html, 'html.parser')
value = soup.findAll("td", {"class": "text-right"})
value2 = soup.findAll("a", {"rel": "nofollow"})

#for y in value2:
#    manifest = re.findall("[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]", str(y))
#    print(manifest[0])

valueCount = 0

for x in value:
    date = re.findall("[\.0-9]", str(x))
    manifestDate = str(x).replace('<td class="text-right">', "").replace(' UTC</td>', "")
    manifest = re.findall("[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]", str(value2[valueCount]))
    manifestVersion = manifest[0]
    valueCount = valueCount + 1
    data = {
        "date": f"{manifestDate}",
        "manifest": f"{manifestVersion}"
    }
    with open(r'C:\Users\danie\Desktop\manifest.json', 'a') as f:
        f.write(f"""{data},
""")
