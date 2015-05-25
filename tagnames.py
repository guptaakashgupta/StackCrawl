import json
import re

count=0
jsonFile=open('stackoverflowTags.json','r')
for line in jsonFile:
	if re.search('"name"', line):
		words=line.split(':')
		tag=words[1].split('"')
		#count=count+1
		with open('tags.txt','a') as outfile:
			outfile.write(tag[1])
			outfile.write('\n')
