from sklearn.feature_extraction.text import CountVectorizer
from scipy import linalg,array,dot,mat
from math import *
from pprint import pprint
import numpy as np

Q=np.matrix([[1, 2], [3, 4]])

I=Q.dot(Q.getI())
print "-----"
print I
