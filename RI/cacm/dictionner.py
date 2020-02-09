import math
import sys
import operator
import pickle
#add path of the project folder on your laptop here 
sys.path.append('C:/Users/Moi/Desktop/RI')
try:
	stopwords = open("common_words" ,"r", encoding='utf-8')
	cacm= open("cacm.all" ,"r", encoding='utf-8')
	mot_vide = stopwords.read()
except:
	stopwords = open("cacm/common_words" ,"r", encoding='utf-8')
	mot_vide = stopwords.read()
	cacm= open("cacm/cacm.all" ,"r", encoding='utf-8')





FD = dict() # Num de document -> {( Mot,  fréquence ) ... }

Dinv1 = dict() # ( Mot, Num de document ) -> fréquence
Dinv2 = dict() # Mot ->  [( Num de document, fréquence )... ]

FDpond = dict() # Num de document -> {( Mot,  pond ) ... }
Dinvpond2 = dict() # Mot ->  {( Num de document, pond )... }

All_texts = dict()
ALL_titles = dict()

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

		if ( i == si-1):
			if(tampon.isalpha()):
				if tampon not in mot_vide:
					if(tampon in retdect.keys()):
						retdect[tampon] = retdect[tampon] + 1
					else:
						retdect[tampon] = 1
	return retdect

def Extract_text():
	AT = list()
	AR = list()
	s = str()
	c = cacm.read().split('\n')
	i = 0

	while i<len(c):
		if (i == len(c)):
			break

		if (c[i].startswith('.I')):
			indice = c[i].split()[1]

		if (c[i] == '.T' ):
			while True:
				i += 1
				if (not c[i].startswith('.')):
					s = s +' '+ c[i]
				else:
					break
			AT.append((indice, s.lower() ))
			s = str()

		if(c[i] == '.W'):
			while True:
				i += 1
				if (not c[i].startswith('.')):
					s = s +' '+ c[i]
				else:
					break

			AR.append((indice, s.lower() ))
			s = str()

		i += 1
	return dict(AT), dict(AR)

def call_Termsv(doc_id, Fd):
	print(doc_id)
	if str(doc_id) in Fd.keys():
		return Fd[str(doc_id)].items()
	return None

def call_docsv(term, dinv2):
	if term in dinv2.keys():
		return dinv2[term]
	return None


def call_Terms(doc_id):
	if str(doc_id) in FD.keys():
		return FD[str(doc_id)].items()
	return None

def call_docs(term):
	if term in Dinv2.keys():
		return Dinv2[term]
	return None

def pond(ti,dj):
	docs = sorted(call_docs(ti), key = operator.itemgetter(1), reverse= True)

	for i in docs:
		if int(i[0]) == dj:
			term_freq = i[1]
	
	terms = call_Terms(dj)
	max_freq = max([ i[1] for i in terms ])
	c = (term_freq / max_freq)*math.log10( len(FD.keys()) / len(docs) + 1 ) 
	return c 

def Full_Dict():
	titles, texts = Extract_text()
	stack = str()

	for i in titles.keys():
		if i in texts.keys():
			stack = titles[i] +' '+ texts[i]
		else:
			stack = titles[i]

		FD[i] = words(stack)
		stack = str()
	#print(FD.items())

def Dict_Inv():
	for i in FD.keys():
		for mot in FD[i]:
			Dinv1[(mot , i)] = FD[i][mot]
			if mot not in Dinv2.keys():
				Dinv2[mot] = list()
				Dinv2[mot].append( (i,FD[i][mot]))
			else:
				Dinv2[mot].append( (i,FD[i][mot]))

def Dict_Inv_Pond():
	l = list()

	for i in Dinv2.keys():
		for j in Dinv2[i]:
			l.append( (j[0], pond(i, int(j[0])) ))
			if j[0] not in FDpond.keys():
				FDpond[ j[0] ] = list()
				FDpond[ j[0] ].append( (i, pond(i, int(j[0]))) )
			else:
				FDpond[ j[0] ].append( (i, pond(i, int(j[0]))) )

		Dinvpond2[i] = l
		l = list()

def call_Terms_Pond(doc_id):
	if str(doc_id) in FDpond.keys():
		return FDpond[str(doc_id)]
	return None

def call_docs_Pond(term):
	if term in Dinvpond2.keys():
		return Dinvpond2[term]
	return None

if __name__ == '__main__':
	
	#ALL_titles, All_texts = Extract_text()
	#Full_Dict()
	#Dict_Inv()
	#Dict_Inv_Pond()
	
	
	
	"""
	with open('Full_Dict.pickle', 'wb') as handle:
		pickle.dump(FD, handle, protocol=pickle.HIGHEST_PROTOCOL)
	
	with open('Dict_Inv1.pickle', 'wb') as handle:
		pickle.dump(Dinv1, handle, protocol=pickle.HIGHEST_PROTOCOL)

	with open('Dict_Inv2.pickle', 'wb') as handle:
		pickle.dump(Dinv2, handle, protocol=pickle.HIGHEST_PROTOCOL)

	with open('Dict_Inv1_Pond.pickle', 'wb') as handle:
		pickle.dump(FDpond, handle, protocol=pickle.HIGHEST_PROTOCOL)

	with open('Dict_Inv2_Pond.pickle', 'wb') as handle:
		pickle.dump(Dinvpond2, handle, protocol=pickle.HIGHEST_PROTOCOL)

	with open('ALL_titles.pickle', 'wb') as handle:
		pickle.dump(ALL_titles, handle, protocol=pickle.HIGHEST_PROTOCOL)

	with open('All_texts.pickle', 'wb') as handle:
		pickle.dump(All_texts, handle, protocol=pickle.HIGHEST_PROTOCOL)

	
	"""
	with open('Full_Dict.pickle', 'rb') as handle:
		FD = pickle.load(handle)
	
	with open('Dict_Inv1.pickle', 'rb') as handle:
		Dinv1 = pickle.load(handle)

	with open('Dict_Inv2.pickle', 'rb') as handle:
		Dinv2 = pickle.load(handle)

	with open('Dict_Inv1_Pond.pickle', 'rb') as handle:
		FDpond = pickle.load(handle)

	with open('Dict_Inv2_Pond.pickle', 'rb') as handle:
		Dinvpond2 = pickle.load(handle)

	with open('ALL_titles.pickle', 'rb') as handle:
		ALL_titles =pickle.load(handle) 

	with open('All_texts.pickle', 'rb') as handle:
		All_texts = pickle.load(handle)
	
	print(FDpond["3204"])
	print(Dinvpond2["monica"])


	import time
	i = 0
	lis = list()
	lis2 = list()
	while (i < 10):
		s = time.clock()
		e = FDpond["3204"]
		lis.append(time.clock() - s)
		i += 1
		s = time.clock()
		e = Dinvpond2["monica"]
		lis2.append(time.clock() - s)





	print( sum(lis) / 10   )	
	print( sum(lis2) / 10   )
	
	




