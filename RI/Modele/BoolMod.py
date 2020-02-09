import sys
sys.path.append('C:/Users/Moi/Desktop/RI')
import pickle

operators = ['OR', 'AND', 'NOT']


class Basic:
	def __init__(self, FD, Dinv1, Dinv2, FDpond,Dinvpond2):
		self.FD  =  FD # Num de document -> {( Mot,  fréquence ) ... }
		self.Dinv1  =  Dinv1 # ( Mot, Num de document ) -> fréquence
		self.Dinv2  =  Dinv2 # Mot ->  [( Num de document, fréquence )... ]
		self.FDpond  =  FDpond # Num de document -> {( Mot,  pond ) ... }
		self.Dinvpond2  =  Dinvpond2 # Mot ->  {( Num de document, pond )... }

	def TreatReq(self, request, words):
		newreq = request.split(' ')
		reqbol = ''
		for i in newreq :
			if i not in operators:
				if i.lower() in words:
					reqbol+= '1'+' '
				else:
					if i == '(' or i  ==  ')':
						reqbol+=  i +' '
					else:
						reqbol+= '0'+' '
			else:
				if i == 'AND':
					reqbol+= '*'+' '
				if i == 'OR':
					reqbol+= '+'+' '
				if i == 'NOT':
					reqbol+= '-'
		return reqbol

	def found(self, reqbol, words):
		reqbol  =  self.TreatReq(reqbol, words).split(' ')
		reqev = ''
		for c in reqbol:
			if c == '-1':
				reqev+= '0'+' '
			else:
				if c == '-0':
					reqev+= '1'+' '
				else:
					reqev+= c+' '
		try:
			if eval(reqev) >= 1:
				return True
			else:
				return False
		except:
			return None

	def Answer(self, request):
		ret  =  list() #returned variable
		for i in self.FD.keys():
			l  =  [ele for ele in self.FD[i]]
			check  =  self.found(request , l)

			if check == True:
				ret.append(i)

			if check == None:
				return 0 

		return ret

if __name__  ==  '__main__':
	req1 = 'NOT optimization AND system AND performance'

	with open('../cacm/Full_Dict.pickle', 'rb') as handle:
		FD = pickle.load(handle)

	with open('../cacm/Dict_Inv1.pickle', 'rb') as handle:
		Dinv1 = pickle.load(handle)

	with open('../cacm/Dict_Inv2.pickle', 'rb') as handle:
		Dinv2 = pickle.load(handle)

	with open('../cacm/Dict_Inv1_Pond.pickle', 'rb') as handle:
		Dinvpond1 = pickle.load(handle)

	with open('../cacm/Dict_Inv2_Pond.pickle', 'rb') as handle:
		Dinvpond2 = pickle.load(handle)

	b  =  Basic( FD, Dinv1, Dinv2, Dinvpond1, Dinvpond2 )
	import time 
	lis = list()
	for i in range(0,10):
		s = time.clock()
		e = b.Answer(req1)
		lis.append(time.clock() - s)

	print(sum( lis) / len(lis))




	