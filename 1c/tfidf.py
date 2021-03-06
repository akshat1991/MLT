# Akshat Harit
# GtID 903090915


import fileinput,re
import numpy as np
np.set_printoptions(threshold=np.nan)
def text_process(word):
  word=re.sub(r'[\r\t\n]', ' ', word)
  word=re.sub(r'[^a-z ]', '', word.lower())
  return word

# Read the file
set1=set()
number_of_files=-1 # Initialize to -1 so as to start array indice from zero
for filew in fileinput.input():
  number_of_files+=1
  print number_of_files

  for words in filew.split():
    word=text_process(words)
    if (word !=''):
      set1.add(word)
#print "Unique Words are" + str(len(set1))
#print set1
#Make numpy matrix for file and words
word_dict=dict()
words_matrix=np.zeros( (number_of_files+1,len(set1) ))
hash_word=0
file_dict=dict()
word_dict_reverse=dict()
number_of_files=-1
for filew in fileinput.input():
  number_of_files+=1
  for words in filew.split():
    word=text_process(words)
    if (word ==''):
      continue
    elif(word not in word_dict):
      word_dict[word]=hash_word
      word_dict_reverse[hash_word]=word
      hash_word+=1
    
    file_dict[fileinput.filename()]=number_of_files
    words_matrix[file_dict[fileinput.filename()],word_dict[word]]+=1
    if(words=="resulted"):
      print words_matrix

#print words_matrix

#Compute idf
wc=words_matrix.copy()
wc=wc.transpose()
#print wc
wc[wc>=1]=1
dc=wc.sum(axis=1)

idf=np.log(float(number_of_files+1)/dc)


#Compute tf and tfidf  
tf=np.zeros((number_of_files+1,len(set1)))
tf=tf.transpose()
tfidf=tf.copy()
wc=words_matrix.copy()
wc=wc.transpose()
for j in range(len(tf[0,:])): # j is files
  for i in range(len(tf[:,0])): 
    hash_word=0
    # i is words
    #print "WC= "+str(wc[i,j])+"Max in the row"+ str(max(wc[:,j]))+" "+word_dict_reverse[i] 
    #tf[i,j]=float(wc[i,j])/max(wc[:,j])
    #tfidf[i,j]=tf[i,j]*idf[i]
    #if(max(wc[:,j])==0):
       #print word_dict_reverse[i]
       #print wc[:,j]


#Printing file list in order
file_list=[0 for col in range(len(file_dict))]
for k,v in file_dict.items(): 
  file_list[v]=k


#Actual printing loop

print 'term, '+ ','.join(file_list)
printV=''
for k, v in word_dict.items():
  printV=k
  for i in range(len(file_list)):
    printV+=','+str(tfidf[v,i])
  print printV
  printV=''
