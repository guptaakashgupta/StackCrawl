from StringIO import StringIO
import gzip
import urllib
import json

def getSource(url):
	source=urllib.urlopen(url)
	
	if source.info().get('Content-Encoding') == 'gzip':
		buf = StringIO( source.read())
		f = gzip.GzipFile(fileobj=buf)
		data = f.read()
		return(data)

for i in range(1,9901):
	jsonUrl='https://api.stackexchange.com/2.2/tags?page='+str(i)+'&order=desc&min=1&max=1000000&sort=popular&site=stackoverflow&key=0w*OgBld6nzckn1OlyveNQ(('
	src=getSource(jsonUrl)
	data=json.loads(src)
	
	with open('stackoverflowTags.json','a') as outfile:
		json.dump(data,outfile,sort_keys=True,indent=4,separators=(',',':'))
