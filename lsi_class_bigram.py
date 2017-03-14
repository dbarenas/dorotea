#!/usr/bin/python
# -*- coding: <utf-8> -*-
from sklearn.feature_extraction.text import CountVectorizer
from scipy import linalg,array,dot,mat,spatial
from math import *
from pprint import pprint
import numpy as np
import scipy
import json

from datetime import datetime

tstart = datetime.now()
f = open('/Users/dbarenaserevalue/workflow/dataprocessing/res100', 'rb')
stopwordsFile = open('stopwords.txt', 'rb')
wlist=[]
for linew in stopwordsFile.readlines():
	wlist.append(linew.replace('\n','').decode('utf-8'))

SPANISH_STOPWORDS=frozenset(wlist)
SPANISH_STOPWORDS=[]
#print SPANISH_STOPWORDS

dataset=[]
countLines=0
docIndex=[]

for i in f.readlines():
	countLines=countLines+1
	doc=[]
	seg=(i.split('lines'))
	id= seg[0].split("'id': '")[1].split("', '")[0]
	topic= seg[0].split("'id': '")[1].split("'news_topics':")[1].split("'codes': ['")[1].split("']},")[0].replace("'","")
	dicinfo={'id':id,'topic':topic}
	docIndex.append(dicinfo)
	if len(seg) > 1:
		sw=seg[1].split('word')
		res= sw[0].split(", ''")
		for i in res:
			doc.append( i.replace(',','').replace("'","").replace(': [','').replace(']',''))
		docString= ' '.join(doc)
		dataset.append(docString)

	if countLines == 30:
		break

mean = dataset
tend = datetime.now()


# mean= ['Shipment of gold damage in and fire'
#        ,'Delivery of silver arrived in and silver truck'
#        ,'Shipment of gold arrived in and truck'
#        ]
vectorizer = CountVectorizer(min_df=0,stop_words=SPANISH_STOPWORDS,ngram_range=(2,3))

X = vectorizer.fit_transform(mean)
# print ";*;"*50
# print X
# print ";*;"*50
analyze = vectorizer.build_analyzer()

# print mean
# print "*"*20
# print "*"*20
matrix = X.toarray()
# print matrix

<<<<<<< HEAD
q=vectorizer.transform([u'En dos oficios, la Corte Suprema de Justicia indagó a las secretarías de Senado y Cámara por algunos datos de doce congresistas de diferentes partidos políticos. En un primer escrito, firmado por Nancy Calderón Perilla, “profesional universitaria”, y que llegó a la Secretaría de Senado, el alto tribunal indaga por dos puntos: los “integrantes de las comisiones (…) tercera y sexta durante los periodos 2010-2014 y 2014-2018”. El segundo punto ronda sobre si siete senadores y exsenadores “fueron autores o promovieron debates de control político durante los dos periodos antes mencionados”. Los congresistas por los que se indaga son Bernardo Miguel Elías Vidal, Musa Besaile Fayad y y José David Name, de ‘la U’; Roberto Gerleín Echavarría, del Partido Conservador; Iván Duque Márquez, del Centro Democrático, y Arleth Casado de López, del Partido Liberal. También se indaga por el exsenador del Partido Liberal y actual ministro del Interior, Juan Fernando Cristo Bustos. Por los lados de la Cámara llegó un oficio igual con los nombres de Alfredo Ape Cuello Baute, José Alfredo Gnecco Zuleta y Manuel Guillermo Mora Jaramillo, de ‘la U’; Alejandro Carlos Chacón Camargo, del Partido Liberal, y Ciro Alejandro Ramírez Cortés, del Centro Democrático. Aunque en sus escritos la Corte Suprema no especifica por qué la indagación sobre estos congresistas y excongresistas, algunos de ellos han sido mencionados en diferentes instancias en medio del escándalo de sobornos de la compañía brasilera Odebrecht. Usualmente, el primer paso del alto tribunal para abrir investigaciones sobre los congresistas es que el Congreso les notifique su calidad de aforados, algo que no aparece en ninguna parte de estos dos escritos. Sin embargo, el alto tribunal indica que la información solicitada tiene como propósito obrar “en las diligencias que se adelantan en esta corporación”. Se espera que en los próximos días las secretarías de Senado y Cámara envíen la información solicitada por la Corte Suprema de Justicia. POLÍTICA']) 

# print "q *"*20
qtr= zip(*q)
qt = np.matrix(qtr)
# print qt

M,N = matrix.shape
U,s,Vh = linalg.svd(matrix)
Sig = linalg.diagsvd(s,M,N)
#U, Vh = U, Vh

# print "u."*20
# print U # -> is Vh
# print "S."*20
# print Sig
# print "Vh."*20
# print Vh # -> is U
# ur=U.dot(Sig.dot(Vh))

# print "experimento "
Uk= np.matrix(Vh)
#Sigk=np.matrix([[ 1/4.0989,0., 0., 0., 0., 0., 0., 0., 0., 0.,0. ], [ 0., 1/2.3616,  0., 0., 0., 0., 0., 0., 0., 0.,0. ],[ 0.,0.,1/1.27197841,0.,0.,0.,0.,0.,0.,0.,0. ]])
Sig=np.matrix(Sig)
Sigk=Sig.getI()
Sigk= Sigk.T
# print type(qt)
# print qt.shape
# print type(Uk)
# print Uk.shape
# print type(Sigk)
# print Sigk.shape
#qr=(qt)dot(Uk)dot(Sk)exp-1
# print ":"*20
qr=Sigk.dot(Uk)
# print qr.shape
# print "R"*20
r=qr.dot(qt)
# print "el vector q=",r.tolist()

# print "::"*20
#print U[0][:2]
qqr=zip(*r.tolist())
# print qqr[0][:2]
results=[]
for i in range(len(U)):
	print i,docIndex[i], 1-scipy.spatial.distance.cosine(U[i][:2], qqr[0][:2])

