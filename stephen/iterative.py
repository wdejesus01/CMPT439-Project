import math
import numpy as np
import matplotlib as pyplot
def jacobi(matrice,tolval,stopcriterion,n):
    
    ###
    coefficent = matrice[:,:-1] # coeffiecent
    augmented = matrice[:,-1] #augmented
    
    noveaucoe = coefficent.copy()#copying coefficent
    noveauaug = augmented.copy()#copying augmented 
    for i in range(n):#checking if val is diagonally dominant or not
        offsum = 0#retreiving sum
        diagnonal = np.abs(noveaucoe[i,i])#
        for j in range(n):
            if(i!=j):#if it is not, just get sum of coefficents
                offsum +=np.abs(noveaucoe[i,j])
        if diagnonal < offsum:
            print("not diagonally dominant. Must transform")#if the diagonal is smaller than sum,display this message
            
        
    for i in range(n):
        noveauaug[i]=noveauaug[i]/noveaucoe[i,i]#transforming biasses via dividng them by diagonal element
        for j in range(n):
            if i !=j:# avoiding redundant operations in main loop
                noveaucoe[i,j]= noveaucoe[i,j]/noveaucoe[i,i]
    newval=np.ones(n)
    oldval=np.ones(n)        
    error=10#starting new while loop
    while(error>tolval):#main loop for our iterative process
        error = 0#initalizer of error
        for i in range(n):
            oldval[i]=newval[i]#store current approximations
            newval[i] = noveauaug[i]#storing current approximations
        for i in range(n):#loop for calculations
            for j in range(n):
                if(i!=j):
                    newval[i]=newval[i]-noveaucoe[i,j]*oldval[j]
                    
       
        if stopcriterion == "MAE":
            error = np.mean(np.abs(newval-oldval))
        elif stopcriterion == "RMSE":
            error = np.sqrt(np.mean(np.abs(newval-oldval)**2))
        elif stopcriterion == "true mae":
            error  = np.mean(np.abs(np.dot(coefficent,newval)-augmented))
        elif stopcriterion == "true rmse":
            error = np.sqrt(np.mean((np.dot(coefficent,newval)-augmented)**2))
    return newval


def gauss(matrice,tolval,stopcriterion,n):
    coefficent = matrice[:,:-1] # coeffiecent
    augmented = matrice[:,-1] #augmented
    
    noveaucoe = coefficent.copy()
    noveauaug = augmented.copy()
    #checking if dagonaly or not
    for i in range(n):
        offsum = 0
        diagnonal = np.abs(noveaucoe[i,i])
        for j in range(n):
            if(i!=j):
                offsum +=np.abs(noveaucoe[i,j])
        if diagnonal < offsum:
            print("not diagonally dominant. Must transform")
            
    for i in range(n):
        noveauaug[i]=noveauaug[i]/noveaucoe[i,i]
        for j in range(n):
            if(i!=j):
                 noveaucoe[i,j]= noveaucoe[i,j]/ noveaucoe[i,i]
    x=np.ones(n)
    oldval=np.ones(n)
    error = 10#error intializer is assigned to 10
    
    while(error > tolval):
        error=0# initalzatior of error
        oldval=x.copy()
        for i in range(n):
            x[i]=noveauaug[i]#updating current approximations of new x array
            for j in range(n):
                if i!= j:
                    x[i]=x[i]- noveaucoe[i,j]*x[j]#latest avaliable approximations
                    
            #stop criterions
        if stopcriterion == "MAE":
            error = np.mean(np.abs(x-oldval))
        elif stopcriterion == "RMSE":
            error = np.sqrt(np.mean(np.abs(x-oldval)**2))
        elif stopcriterion == "true mae":
            error  = np.mean(np.abs(np.dot(coefficent,x)-augmented))
        elif stopcriterion == "true rmse":
            error = np.sqrt(np.mean((np.dot(coefficent,x)-augmented)**2))
        
    return x
