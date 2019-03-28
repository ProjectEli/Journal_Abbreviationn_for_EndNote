import urllib.request

data = urllib.request.urlopen("https://www.cas.org/support/documentation/references/corejournals")
raw = data.read().decode('utf8')
print(raw[:-400])