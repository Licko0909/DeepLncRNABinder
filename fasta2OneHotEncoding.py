import os
import sys
from numpy import array
from numpy import argmax
from keras.utils import to_categorical
import numpy as np
import string
#import diShuffle
def oneHot2Sequence(oneHot):
    #print(oneHot)
    seq=np.zeros(shape=(oneHot.shape[0],),dtype=np.str)
    for i in range(0,oneHot.shape[0]):
        print(np.array_str(oneHot[i,:]))
        if(np.array_str(oneHot[i,:]) =='[1 0 0 0]'):
           seq[i]='A'
        elif(np.array_str(oneHot[i,:]) =='[0 1 0 0]'):
           seq[i]='T'
        elif(np.array_str(oneHot[i,:]) =='[0 0 1 0]'):
           seq[i] ='G'
        elif(np.array_str(oneHot[i,:]) =='[0 0 0 1]'):
           seq[i] ='C'
        else:
           seq[i]='N'
        s=np.array_str(seq)
        s=s.replace('[','')
        s=s.replace(']','')
        s=s.replace(' ','')
        s=s.replace("'","")
    return s

def complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(seq)
    bases = [complement[base] for base in bases]
    return ''.join(bases)

def reverse_complement(s):
        return complement(s[::-1])

MIN_SEQ_LENGTH = 501
def fasta2OneHot(fastafile,classLabel):
  #fastafile=sys.argv[1]
  f=open(fastafile)
  lines=f.read().splitlines()
  i=0
  x = np.zeros(shape=(120000,500,4),dtype=np.int)
  y = np.zeros(shape=(120000,),dtype=np.int)
  c=0
  MAX_LENGTH=0
  while i < len(lines):
    #print(i)
    id = lines[i]
    i=i+1
    seq = lines[i]
    seq= seq.upper()
    if(len(seq) > MAX_LENGTH):
      MAX_LENGTH=len(seq)
    s = seq
    #rev_seq = reverse_complement(seq)
    seq = seq.replace('A','0')
    seq = seq.replace('a','0')
    seq = seq.replace('T','1')
    seq = seq.replace('t','1')
    seq = seq.replace('u','1')
    seq = seq.replace('U','1')
    seq = seq.replace('G','2')
    seq = seq.replace('g','2')
    seq = seq.replace('C','3')
    seq = seq.replace('c','3')

    seq = str(seq)
    
    data = list(seq)
    #print(len(data))
    if ('N' not in data ):
       data = [int(j) for j in data]
       data = array(data)
       d = to_categorical(array(data),num_classes=4)
       if(len(data) >=501):
          mid = round(len(data)/2 + 0.5)
          start = mid - round(MIN_SEQ_LENGTH/2)
          end = mid + round(MIN_SEQ_LENGTH/2)
          d = d[start:end,]
       else:
          pad = 500 - len(seq)
          b=np.zeros(shape=(pad,4))
          d=np.concatenate((d, b), axis=0)
         
       x[c,:,:]=d
       y[c] = classLabel
       c=c+1
    i=i+1
  x=x[0:c,:,:]
  y=y[0:c]
  #print(x.shape)
  #print(y.shape)
  return(x,y)




#files
pos_train_fa = sys.argv[1]
neg_train_fa = sys.argv[2]
(x1,y1) = fasta2OneHot(pos_train_fa,1)
(x2,y2)=fasta2OneHot(neg_train_fa,0)
x_train = np.concatenate((x1,x2))
y_train = np.concatenate((y1,y2))

#print(x1.shape)
#print(y1.shape)

pos_test_fa = sys.argv[3]
neg_test_fa = sys.argv[4]

#neg_test_fa = sys.argv[1]
#neg_test_fa = sys.argv[1]

(x1,y1) = fasta2OneHot(pos_test_fa,1)
(x2,y2) = fasta2OneHot(neg_test_fa,0)
x_test = np.concatenate((x1,x2))
y_test = np.concatenate((y1,y2))




print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

import h5py
hf = h5py.File(sys.argv[5]+".h5", 'w')
hf.create_dataset('x_train', data=x_train)
hf.create_dataset('y_train', data=y_train)
hf.create_dataset('x_test', data=x_test)
hf.create_dataset('y_test', data=y_test)
hf.close()

