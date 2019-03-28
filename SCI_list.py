from bs4 import BeautifulSoup

pagelist = range(1,9) # 1~8

for page in pagelist:
    f = open('SCI_20190329/p{}.html'.format(page))
    dat = f.read()
    f.close()

    soup = BeautifulSoup(dat,'html.parser')
    vals = soup.find_all('strong')[1:]
    journallist = []
    for val in vals:
        journallist.append(val.text.split('. ')[1])

    f2 = open('SCI_20190329/p{}.txt'.format(page),'w')
    f2.write('\n'.join(journallist))
    f2.close()