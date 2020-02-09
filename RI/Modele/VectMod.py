import sys
sys.path.append('C:/Users/Moi/Desktop/RI')
import pickle
from math import *
from operator import itemgetter

class VectMod:
	def __init__(self, FD, Dinv1, Dinv2, FDpond, Dinvpond2, path):
		self.FD  =  FD # Num de document -> {( Mot,  fréquence ) ... }
		self.Dinv1  =  Dinv1 # ( Mot, Num de document ) -> fréquence
		self.Dinv2  =  Dinv2 # Mot ->  [( Num de document, fréquence )... ]
		self.Dinvpond1  =  FDpond # Num de document -> {( Mot,  pond ) ... }
		self.Dinvpond2  =  Dinvpond2 # Mot ->  {( Num de document, pond )... }
		self.mot_vide = mot_vide = open(path ,"r", encoding='utf-8').read()

	def foundvect(self, req):
		l = len(req)
		req = req.lower()
		vec = list()
		nreq = list()
		s = str()
		for w in req:
			if w.isalpha():
				s = s+w
			else:
				if s not in self.mot_vide:
					nreq.append(s)
				s = str()
		for k in self.FD.keys():
			liste = self.FD[k].keys()
			#print(liste)
			v= str()
			for i in nreq:
				if i in liste:
					v+= str( self.FD[k][i] ) + " "
				else:
					v+= "0 "
			#print(v)
			v = v.split()
			vec.append(v)
			#print(k+' le vecteur de la requête: '+str(v))
		return vec

	def vecpond(self, req):
		l = len(req)
		req = req.lower()
		vecp = list()
		nreq = list()
		s = str()
		for w in req:
			if w.isalpha():
				s = s+w
			else:
				if s not in self.mot_vide:
					nreq.append(s)
				s = str()
		for k in self.Dinvpond1.keys():
			listep=str()
			l = dict(self.Dinvpond1[k])
			for y in nreq:
				if y in l.keys():
					listep += str(l[y]) + " "	
				else:
					listep += "0 "
			listep = listep.split()
			#print(k+' le vecteur pondérer de la requête: '+str(listep))
			vecp.append(listep)
		return vecp

	def InnerProd(self, s):
		VN = self.foundvect(s)
		VP = self.vecpond(s)
		inn = list()
		for k in range(0,len(VN)):
			som = float()
			#print(k,VN[k])
			for i in range(0,len(VN[k])):
				som+= float(VN[k][i]) * float(VP[k][i])
			inn.append((k+1, som))
		return sorted(inn, key = itemgetter(1), reverse= True)

	def COEFD(self,s ):
		VN = self.foundvect(s)
		VP = self.vecpond(s)
		coef = list()
		for k in range(0,len(VN)):
			som = float()
			s1 = float()
			s2 = float()
			co = float()
			for i in range(0,len(VN[k])):
				som+= float(VN[k][i] )* float(VP[k][i])
				s1+= float(VN[k][i] )* float(VN[k][i])
				s2+= float(VP[k][i] )* float(VP[k][i])
			try:
				co = ( 2*som )/( s1+s2 )
				coef.append((k+1, co))
			except Exception as e:
				coef.append((k+1, 0.0))
			
		return sorted(coef, key = itemgetter(1), reverse= True)

	def cosinusM(self, s):
		VN = self.foundvect(s)
		VP = self.vecpond(s)
		cosin = list()
		for k in range(0,len(VN)):
			som = float()
			s1 = float()
			s2 = float()
			cos = float()
			for i in range(0,len(VN[k])):
				som+= float(VN[k][i] )* float(VP[k][i])
				s1+= float(VN[k][i] )* float(VN[k][i])
				s2+= float(VP[k][i] )* float(VP[k][i])
			try:
				cos = som/sqrt( s1*s2 )
				# if( cos > 0):
				# 	print(k,cos , som ,  sqrt( s1*s2 ) , s1*s2 )
				cosin.append((k+1, cos))
			except Exception as e:
				cosin.append((k+1, 0.0))
		return sorted(cosin, key = itemgetter(1), reverse= True)

	def jaccardM(self, s):
		VN = self.foundvect(s)
		VP = self.vecpond(s)
		jac = list()
		for k in range(0,len(VN)):
			som = float()
			s1 = float()
			s2 = float()
			j = float()
			for i in range(0,len(VN[k])):
				som+= float(VN[k][i] )* float(VP[k][i])
				s1+= float(VN[k][i] )* float(VN[k][i])
				s2+= float(VP[k][i] )* float(VP[k][i])
			try:
				j = som/( ( s1+s2 )-som )
				jac.append((k+1, j))
			except Exception as e:
				jac.append((k+1, 0))
		return sorted(jac, key = itemgetter(1), reverse= True)

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

	b  =  VectMod( FD, Dinv1, Dinv2, Dinvpond1, Dinvpond2, "../cacm/common_words")
	s = "I am interested in articles written either by Prieve or Udo Pooch"
	print(b.jaccardM(s))


