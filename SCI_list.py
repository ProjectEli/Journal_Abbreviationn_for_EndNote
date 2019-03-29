from bs4 import BeautifulSoup
import re

pagelist = range(1,9) # 1~8

for page in pagelist:
    f = open('SCI_20190329/p{}.html'.format(page))
    dat = f.read()
    f.close()

    # collect ISSN because of multiple search result in CAS webpage
    issnlist = re.findall(r'<br>ISSN:.*<br>',dat)
    issnlist_reduced = []
    for issnval in issnlist:
        templist = issnval.split('<br>')
        tempstr = templist[1].split('ISSN: ')[1]
        if tempstr == '****-****':
            issnlist_reduced.append(templist[2].split('E-ISSN: ')[1])
        else:
            issnlist_reduced.append(tempstr)

    f2 = open('SCI_20190329/p{}.txt'.format(page),'w')
    f2.write('\n'.join(issnlist_reduced))
    f2.close()