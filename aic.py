#!/usr/bin/env python
#-*- coding: utf-8 -*-



#funciona

def group_equal(x): #x: lsita de listas
	solu=[] #lista solución
	if len(x)>0: #condición
		count=0 #countador
		comp=[x[0]] #variable con la que se compara los elementos (puesta en el primer elemento a comparar)
		while count<len(x)-1: #Se empieza a comparar todos los elementos de la lista
			breaker=True #Variable para romper
			while breaker==True: 
				if x[count+1]==comp[0]:
					comp.append(x[count+1])
					count+=1
				else:
					breaker=False
				if count==len(x)-1:
					breaker=False
			solu.append(comp)
			if count<len(x)-1:
				comp=[x[count+1]]
			else:
				comp=[]
			count+=1
		if comp!=[]:
			solu.append(comp)				
	return solu

print group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) 
#print '[[1,1],[4,4,4],["hello","hello"],[4]]'
print group_equal([1, 2, 3, 4]) 
#print '[[1], [2], [3], [4]]'
print group_equal([1]) 
#print '[[1]]'
print group_equal([]) 
#print '[]'
#######

print group_equal([5,5,"5",5,5])
#print '[[5,5],["5"],[5,5]]'



#arreglar

"""
def group_equal(li):
	equ=[]
	temp=[]
	if len(li)>0:
		comp=li[0]
		for ele in range(0,len(li)):
			if comp==li[ele]:
				temp.append(comp)
			else:
				comp=li[ele]
				equ.append(temp)
				temp=[]
		temp.append(comp)
		equ.append(temp)
		return equ
print group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) 
print '[[1,1],[4,4,4],["hello","hello"],[4]]'
print group_equal([1, 2, 3, 4]) 
print '[[1], [2], [3], [4]]'
print group_equal([1]) 
print '[[1]]'
print group_equal([]) 
print '[]'
#######
print group_equal([5,5,"5",5,5])
print '[[5,5],["5"],[5,5]]'
"""