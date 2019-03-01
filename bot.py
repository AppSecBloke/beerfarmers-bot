import os
import random

def rline (filename):
	with open(filename) as f:
		lines = f.readlines()
		print(random.choice(lines))
    	
    	
txts = ["users.txt","malware.txt","countries.txt","nouns.txt","animals.txt"]

for x in txts:
	print (rline(x))



msg = "{select_random infosec influencer} + is accused of creating {select_random_malware} & working as a proxy of {Russia or Iran or North_Korea or China} as part of a APT group "
