from sklearn.feature_extraction.text import CountVectorizer
from scipy import linalg,array,dot,mat,spatial
from math import *
from pprint import pprint
import numpy as np
import scipy

mean= ['Shipment of gold damage in and fire'
       ,'Delivery of silver arrived in and silver truck'
       ,'Shipment of gold arrived in and truck'
       ]
vectorizer = CountVectorizer(min_df=0,stop_words=None,ngram_range=(2, 4))
X = vectorizer.fit_transform(mean)
print ";*;"*50
print X
print ";*;"*50
analyze = vectorizer.build_analyzer()


print mean
print "*"*20
print vectorizer.get_feature_names()
print "*"*20
matrix = X.toarray()
print matrix

q=vectorizer.transform(['gold silver truck']).toarray()
print "q *"*20
qtr= zip(*q)
qt = np.matrix(qtr)
print qt

M,N = matrix.shape
U,s,Vh = linalg.svd(matrix)
Sig = linalg.diagsvd(s,M,N)
U, Vh = U, Vh
print "u."*20
print U # -> is Vh
print "S."*20
print Sig
print "Vh."*20
print Vh # -> is U
#ur=U.dot(Sig.dot(Vh))

print "experimento "
Uk= np.matrix(Vh)
#Sigk=np.matrix([[ 1/4.0989,0., 0., 0., 0., 0., 0., 0., 0., 0.,0. ], [ 0., 1/2.3616,  0., 0., 0., 0., 0., 0., 0., 0.,0. ],[ 0.,0.,1/1.27197841,0.,0.,0.,0.,0.,0.,0.,0. ]])
Sig=np.matrix(Sig)
Sigk=Sig.getI()
Sigk= Sigk.T
print type(qt)
print qt.shape
print type(Uk)
print Uk.shape
print type(Sigk)
print Sigk.shape
#qr=(qt)dot(Uk)dot(Sk)exp-1
print ":"*20
qr=Sigk.dot(Uk)
print qr.shape
print "R"*20
r=qr.dot(qt)
print "el vector q=",r.tolist()

print "::"*20
print U[0][:2]
qqr=zip(*r.tolist())
print qqr[0][:2]
print "d1: ",1-scipy.spatial.distance.cosine(U[0][:2], qqr[0][:2])
print "d2: ",1-scipy.spatial.distance.cosine(U[1][:2], qqr[0][:2])
print "d3: ",1-scipy.spatial.distance.cosine(U[2][:2], qqr[0][:2])

