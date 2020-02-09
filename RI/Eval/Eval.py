import sys
sys.path.append('C:/Users/Moi/Desktop/RI')
import pickle
try:
	qrels = open("qrels.text" ,"r", encoding='utf-8')
	content = qrels.read()
	queries = open("query.text" ,"r", encoding='utf-8')
	content_q = queries.read()
except:
	qrels = open("Eval/qrels.text" ,"r", encoding='utf-8')
	content = qrels.read()
	queries = open("Eval/query.text" ,"r", encoding='utf-8')
	content_q = queries.read()

content = content.split("\n")
content = [ i.split(" ") for i in content ]
content_pairs = [ (i[0], i[1])  for i in content ]

content_q = content_q.split("\n")

def getanswers( l):
	ideals = dict()
	for i in l:
		if i[0] in ideals.keys():
			ideals[i[0]].append( str(int(i[1])) )
		else:
			ideals[i[0]] = list()
			ideals[i[0]].append( str(int(i[1])) )

	return ideals

def getqsts( l):
	ideals = dict()
	size = len(l)
	i = 0
	while i < size:
		if l[i].startswith(".I"):
			iD = l[i][2:].lstrip()
		if l[i].startswith(".W"):
			i += 1
			s = str()
			while i < size:
				if not ( l[i].startswith(".N") or l[i].startswith(".A")  ):
					s = s + " " +l[i]
					i += 1
				else:
					ideals[iD] = s[1:]
					break
		i += 1
	return ideals

class Eval:
	def __init__(self, Vecmod):
		self.ideals = getanswers(content_pairs)
		self.questions = getqsts(content_q)
		self.Vecmod = Vecmod

	def intersection(self, lst1, lst2): 
		lst3 = [value for value in lst1 if value in lst2]
		return lst3

	def rap_pre(self, qid, rep, size):
		liste = [ str(rep[r][0]) for r in range(0, size) if rep[r][1] > 0 ]
		L = len(rep)
		x =  self.ideals[str(qid)]
		print(sorted([r[0] for r in rep]))
		print(x)
		i = len(self.intersection(liste, x))
		D = len( x )
		if L == 0:
			pre = 0
		else:
			pre = (i / L)
		return (i / D), pre 

if __name__  ==  '__main__':
	with open('../cacm/Full_Dict.pickle', 'rb') as handle:
		FD = pickle.load(handle)
	
	with open('../cacm/Dict_Inv1.pickle', 'rb') as handle:
		Dinv1 = pickle.load(handle)

	with open('../cacm/Dict_Inv2.pickle', 'rb') as handle:
		Dinv2 = pickle.load(handle)

	with open('../cacm/Dict_Inv1_Pond.pickle', 'rb') as handle:
		FDpond = pickle.load(handle)

	with open('../cacm/Dict_Inv2_Pond.pickle', 'rb') as handle:
		Dinvpond2 = pickle.load(handle)

