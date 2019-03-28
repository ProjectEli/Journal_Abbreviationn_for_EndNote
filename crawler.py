import urllib.request

alphabets = '0-9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
print(alphabets)

resultstr = ''
for alphabet in alphabets:
    data = urllib.request.urlopen("https://images.webofknowledge.com/images/help/WOS/{}_abrvjt.html".format(alphabet))
    raw = data.read().decode('utf8')
    pairstrlist = raw.split('</DL>')[0].split('<DT>')[1:]
    resultlist = []
    for pairstr in pairstrlist:
        tempstr = pairstr.replace('\n<B><DD>','')
        tempstr = tempstr.replace('\n</B>','')
        resultlist.append(tempstr + '\n')
    print(resultlist[:3])
    resultstr = resultstr+ ''.join(resultlist) + '\n'

f = open('JournalAbbrList.txt','w')
f.write(resultstr)
f.close()