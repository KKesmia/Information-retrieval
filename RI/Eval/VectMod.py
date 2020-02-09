import sys
sys.path.append('C:/Users/Moi/Desktop/RI')
import pickle
from math import *


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
		vec = list()
		nreq = str()
		req = req.split(' ')
		for w in req:
			if w not in self.mot_vide:
				nreq+= w+' '
				req = nreq.split()		
		for k in self.FD.keys():
			liste = self.FD[k].keys()
			v= str()
			for i in req:
				if i in liste:				
					v+= str( self.FD[k][i] ) + " "
				else:
					v+= "0 "
			v = v.split()
			vec.append(v)
			#print(k+' le vecteur de la requête: '+str(v))
		return vec

	def vecpond(self, req):
		l = len(req)
		vecp = list()
		nreq = str()
		req = req.split(' ')
		for w in req:
			if w not in self.mot_vide:
				nreq += w+' '
				req = nreq.split()
		for k in self.Dinvpond1.keys():
			l = self.Dinvpond1[k]
			#print(l)
			listep=str()
			#print(k)
			for y in req:	
				v = False
				for i in self.Dinvpond1[k]:
					if y == i[0]:
						v = True
						listep += str(i[1])+' '	
				if v == False:
					listep += '0 '
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
			inn.append((k, som))
		return inn

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
				coef.append((k, co))
			except Exception as e:
				coef.append((k, 0.0))
			
		return coef

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
				cosin.append((k, cos))
			except Exception as e:
				cosin.append((k, 0.0))
		return cosin

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
				jac.append((k, j))
			except Exception as e:
				jac.append((k, 0))

		return jac

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
	s = "alphabetical are fond a languages mistakes format shadow"
	#print(b.jaccardM(s))


