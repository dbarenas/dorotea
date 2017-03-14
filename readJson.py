from sklearn.feature_extraction.text import CountVectorizer
from scipy import linalg,array,dot,mat,spatial
from math import *
from pprint import pprint
import numpy as np
import scipy
import json

f = open('/Users/dbarenaserevalue/workflow/dataprocessing/res100', 'rb')
dataset=[]
countLines=-1
for i in f.readlines():
	countLines=countLines+1
	doc=[]
	seg=(i.split('lines'))
	id= seg[0].split("'id': '")[1].split("', '")[0]
	topic= seg[0].split("'id': '")[1].split("'news_topics':")[1].split("'codes': ['")[1].split("']},")[0].replace("'","")
	print id,topic
	if countLines == 7:
		break


b8cfc9185d93f4bc577fabb650f7f2b5 BBVACUSSERQ
906ddd8c2412e35969c53a4dab29ddd6 CORPORATE_CRIME
3dadc8a1b2ece6badc498ee33d8bd8d3 CORPORATE_CRIME
f8dc80284c82d3457281726d15e251c9 WORKFORCE
7964c2d4145743e7c7a4c265ef6f8135 DIVERSITY, WORKFORCE

00b16eeea76515a7e42ca32ebc954ae2 WORKFORCE

9a6d65866b4266dd6b7e4a24220a9355 CORPORATE_CRIME
b43417a413411ad41e5576af46a6e713 CORPORATE_CRIME
[Finished in 0.6s]