f1 = open('CASplus_Core_Journal_raw_20190328.txt',encoding='utf-8-sig') # read without UTF8 BOM
rawlist = f1.read().split('\n')

resultlist = []
for k in range(int(len(rawlist)/2)):
    resultlist.append(rawlist[2*k+1].split('\t')[0] + '\t' + rawlist[2*k] + '\n')
resultstr = ''.join(resultlist)
print(resultstr[:400])

f = open('CASplus_Core_Journal_20190328.txt','w')
f.write(resultstr)
f.close()