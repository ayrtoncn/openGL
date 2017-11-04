from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy as np
import sys
import input as rn
import time

blocking=False
rotasi = False
pertama = True
isMultiple = False
multAnimateFinish = True
NMult = 0
InputList = []
iMult = 0




def getMatrix():
	global pertama
	global defaultM
	if(pertama):
		N = int(input())
		PList = [] # DEFINE EMPTY LIST
		global M
		for i in range(N): # GET POINTS
			X, Y = rn.getPoints()
			PList.append([float(X), float(Y),0.0])
		M = np.matrix(PList)
		
		defaultM=np.copy(M)
		pertama = False
	return M

def animasi():
	global blocking
	global i
	global rotasi
	j=0
	if(not(rotasi)):
		for points in M:
			points[0,0]=points[0,0]+Mtemp[j][0]
			points[0,1]=points[0,1]+Mtemp[j][1]
			j=j+1
	else:
		for points in M:
			X1=points[0,0]
			Y1=points[0,1]
			points[0,0]=(cos(sdtanimasi)*(X1-Xrotasi)-(sin(sdtanimasi))*(Y1-Yrotasi))+Xrotasi
			points[0,1]=(sin(sdtanimasi)*(X1-Xrotasi)+(cos(sdtanimasi))*(Y1-Yrotasi))+Yrotasi
	i=i+1
	
	time.sleep(0.00001)
	if(i==100):
		blocking=False
		rotasi=False
		
def animasiMult():
	global multAnimateFinish
	global i
	global rotasi
	j=0
	if(not(rotasi)):
		for points in M:
			points[0,0]=points[0,0]+Mtemp[j][0]
			points[0,1]=points[0,1]+Mtemp[j][1]
			j=j+1
	else:
		for points in M:
			X1=points[0,0]
			Y1=points[0,1]
			points[0,0]=(cos(sdtanimasi)*(X1-Xrotasi)-(sin(sdtanimasi))*(Y1-Yrotasi))+Xrotasi
			points[0,1]=(sin(sdtanimasi)*(X1-Xrotasi)+(cos(sdtanimasi))*(Y1-Yrotasi))+Yrotasi
	i=i+1
	
	time.sleep(0.00001)
	if(i==100):
		multAnimateFinish=True
		rotasi=False

def translate(X,Y):
	global Mtemp 
	global i
	global blocking
	i=0
	Mtemp=np.copy(M)
	Mtemp.astype(float)
	for points in Mtemp:
		points[0]=X/100.0
		points[1]=Y/100.0
	blocking=True
def dilate(dil):
	global Mtemp 
	global i
	global blocking
	i=0
	j=0
	Mtemp=np.copy(M)
	for points in M:
		Mtemp[j][0]=(points[0,0]*dil-points[0,0])/100.0
		Mtemp[j][1]=(points[0,1]*dil-points[0,1])/100.0
		j=j+1
	blocking=True
def rotate(sdt,X,Y):
	global Mtemp 
	global i
	global blocking
	i=0
	global rotasi
	global sdtanimasi
	global Xrotasi
	global Yrotasi
	sdtanimasi=sdt/100.0
	rotasi=True
	Xrotasi=X
	Yrotasi=Y
	blocking=True
	
def sheer(sumbu,K):
	global Mtemp 
	global i
	global blocking
	i=0
	j=0
	Mtemp=np.copy(M)
	if(sumbu=='x'):
		for points in M:
			Mtemp[j][0]=(points[0,0]+K*points[0,1]-points[0,0])/100.0
			Mtemp[j][1]=0
			j=j+1
	elif(sumbu=='y'):
		for points in M:
			Mtemp[j][0]=0
			Mtemp[j][1]=(points[0,1]+K*points[0,0]-points[0,1])/100.0
			j=j+1
	blocking=True
def reflect(param):
	global Mtemp 
	global i
	global blocking
	i=0
	j=0
	Mtemp=np.copy(M)
	temp=param.split(',')
	if(len(temp)==1):
		if(param=='y=x'):
			for points in M:
				Mtemp[j][0]=(-points[0,1]-points[0,0])/100.0
				Mtemp[j][1]=(-points[0,0]-points[0,1])/100.0
				j=j+1
		elif(param=='y=-x'):
			for points in M:
				Mtemp[j][0]=(points[0,1]-points[0,0])/100.0
				Mtemp[j][1]=(points[0,0]-points[0,1])/100.0
				j=j+1
		elif(param=='x'):
			for points in M:
				Mtemp[j][0]=0
				Mtemp[j][1]=(-points[0,1]-points[0,1])/100.0
				j=j+1
		elif(param=='y'):
			for points in M:
				Mtemp[j][0]=(-points[0,0]-points[0,0])/100.0
				Mtemp[j][1]=0
				j=j+1
	else:
		X=float(temp[0][1:])
		Y=float(temp[1][:len(temp[1])-1])
		sdt=radians(180)
		for points in M:
			X1=points[0,0]
			Y1=points[0,1]
			Mtemp[j][0]=(((cos(sdt)*(X1-X)-(sin(sdt))*(Y1-Y))+X)-points[0,0])/100.0
			Mtemp[j][1]=(((sin(sdt)*(X1-X)+(cos(sdt))*(Y1-Y))+Y)-points[0,1])/100.0
			j=j+1
	blocking=True
def stretch(sumbu,K):
	global Mtemp 
	global i
	global blocking
	i=0
	j=0
	Mtemp=np.copy(M)
	if(sumbu=='x'):
		for points in M:
			Mtemp[j][0]=(K*points[0,0]-points[0,0])/100.0
			Mtemp[j][1]=0
			j=j+1
	elif(sumbu=='y'):
		for points in M:
			Mtemp[j][0]=0
			Mtemp[j][1]=(K*points[0,1]-points[0,1])/100.0
			j=j+1
	blocking=True	
	
def transform():
	global isMultiple
	global multAnimateFinish
	global iMult
	global NMult
	global InputList
	if(not(blocking) and not(isMultiple)):
		if(not(pertama)):
			n=input()
			inpTransfType=n.split(' ')
			if inpTransfType[0] == "translate" :
				X=int(inpTransfType[1])
				Y=int(inpTransfType[2])
				translate(X,Y)	
			elif inpTransfType[0] == "dilate" :
				dil=float(inpTransfType[1])
				dilate(dil)			
			elif inpTransfType[0] == "rotate" :
				sdt=radians(float(inpTransfType[1]))
				X=int(inpTransfType[2])
				Y=int(inpTransfType[3])
				rotate(sdt,X,Y)		
			elif inpTransfType[0] == "reflect" :
				param=inpTransfType[1]
				reflect(param)
				
			elif inpTransfType[0] == "sheer" :
				sumbu=inpTransfType[1]
				K=float(inpTransfType[2])
				sheer(sumbu,K)
				
			elif inpTransfType[0] == "stretch" :
				sumbu=inpTransfType[1]
				K=float(inpTransfType[2])
				stretch(sumbu,K)
			
			elif inpTransfType[0] == 'multiple':
				multAnimateFinish = True
				iMult = 0
				InputList = []
				isMultiple = True
				for i in range(int(inpTransfType[1])):
					multInput = input().split(' ')
					InputList.append(multInput)
				NMult = int(inpTransfType[1])
				
			elif inpTransfType[0]=='reset':
				j=0
				for points in M:
					points[0]=defaultM[j]
					j=j+1
			
			elif inpTransfType[0]=='exit':
				exit()
			
	if(blocking and not(isMultiple)):
		animasi()
	if(isMultiple):
		if(multAnimateFinish):
			transformList(InputList[iMult])
			iMult += 1
			multAnimateFinish = False
		else:
			animasiMult()
		if(iMult == NMult):
			isMultiple = False
	return M
	
def transformList(inputList):
	
	inputType=inputList[0]
	if inputType == "translate" :
		X=int(inputList[1])
		Y=int(inputList[2])
		translate(X,Y)			
	elif inputType == "dilate" :
		dil=float(inputList[1])
		dilate(dil)			
	elif inputType == "rotate" :
		sdt=radians(float(inputList[1]))
		X=int(inputList[2])
		Y=int(inputList[3])
		rotate(sdt,X,Y)		
	elif inputType == "reflect" :
		param=inputList[1]
		temp=param.split(',')
		if(len(temp)==1):
			if(param=='y=x'):
				for points in M:
					temp=points[0,0]
					points[0,0]=-points[0,1]
					points[0,1]=-temp
			elif(param=='y=-x'):
				for points in M:
					temp=points[0,0]
					points[0,0]=points[0,1]
					points[0,1]=temp
			elif(param=='x'):
				for points in M:
					points[0,1]=-points[0,1]
			elif(param=='y'):
				for points in M:
					points[0,0]=-points[0,0]
		else:
			X=float(temp[0][1:])
			Y=float(temp[1][:len(temp[1])-1])
			sdt=radians(180)
			for points in M:
				X1=points[0,0]
				Y1=points[0,1]
				points[0,0]=(cos(sdt)*(X1-X)-(sin(sdt))*(Y1-Y))+X
				points[0,1]=(sin(sdt)*(X1-X)+(cos(sdt))*(Y1-Y))+Y
		
	elif inputType == "sheer" :
		sumbu=inputList[1]
		K=float(inputList[2])
		sheer(sumbu,K)
		
	elif inputType == "stretch" :
		sumbu=inputList[1]
		K=float(inputList[2])
		stretch(sumbu,K)
	