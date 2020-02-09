import os
import math

dir = os.listdir('Documents')

stopwords = open("stopwords.txt" ,"r", encoding='utf-8')
mot_vide = stopwords.read()
All_dicts = list()
Full_dict = dict()
Full_dict_Pond = dict()

def words(text):
	si = len(text)
	retdect = dict()
	tampon = str()
	for i in range(0,si):
		if text[i].isalpha():
			tampon = tampon + text[i]
		else:
			if tampon not in mot_vide:
				if(tampon in retdect.keys()):
					retdect[tampon] = retdect[tampon] + 1
				else:
					retdect[tampon] = 1
			tampon = str()	
	return retdect

def FA_FIF():
	AD = list()
	FD = dict()
	for i in dir:
		file = open("Documents/"+i, "r", encoding='utf-8')
		id = ''.join(c for c in i if c.isdigit())
		text = file.read().lower()

		i_dict = words(text)

		AD.append(i_dict)
		for k in i_dict.keys():
			FD[(k , id)] = i_dict[k]
	return AD,FD

def call_Terms(doc_id):
	ret = [(i[0], Full_dict[i]) for i in Full_dict.keys() if int(i[1]) == doc_id ]
	return ret

def call_docs(term):
	ret = [(i[1], Full_dict[i]) for i in Full_dict.keys() if i[0] == term ]
	return ret

def pond(ti,dj):
	docs = call_docs(ti)
	for i in docs:

		if i[0] == dj:
			term_freq = i[1]
	
	max_freq = max( [ i[1] for i in call_Terms( int(dj) ) ] )
	print(term_freq, max_freq, len(dir), len(docs))
	c = (term_freq / max_freq)*math.log( len(dir)/len(docs) + 1 ) 
	return c 

def FIFP(FD):
	FDP = dict()
	j = int()
	for i in FD.keys():
		print(i)
		c = pond(i[0], i[1])
		print(j,"----",c )
		FDP[i] = c
		j = j + 1
	return FDP

def call_Terms_Pond(doc_id):
	ret = [(i[0], Full_dict_Pond[i]) for i in Full_dict_Pond.keys() if int(i[1]) == doc_id ]
	return ret

def call_docs_Pond(term):
	ret = [(i[1], Full_dict_Pond[i]) for i in Full_dict_Pond.keys() if i[0] == term ]
	return ret

if __name__ == '__main__':
	
	All_dicts,Full_dict = FA_FIF()
	#print(All_dicts)
	#print(Full_dict)
	Full_dict_Pond = FIFP(Full_dict)
	#print(pond('définir',0))
	#print(Full_dict_Pond)
	


	'''
	#print(All_dicts)
	#print(Full_dict)
	#print(call_Terms(0))
	#print(call_docs('définir'))
	#print(pond('définir',0))	
	
	
import pickle

a = {'hello': 'world'}

with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)

print a == b*/

'''




