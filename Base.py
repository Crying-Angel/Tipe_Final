import random as rd 



   
def avalanche(Niter,taille,pc):
    S=[[0 for j in range(taille)] for i in range(taille)]
    for grain in range(Niter):
        ip=rd.randint(taille//2-taille//5,taille//2+taille//5)
        jp=rd.randint(taille//2-taille//5,taille//2+taille//5)
        S[ip][jp]+=1
        ava=True    
        while ava:
            for i in range(1,taille-1):
                for j in range(1,taille-1):
                    p=rd.random()
                    ic=rd.randint(0,1)
                    jc=rd.randint(0,1)
                    ic=2*ic-1
                    jc=2*jc-1
                    if ((S[i][j]-S[i][j+1]>3) or (S[i][j]-S[i][j-1]>3) or (S[i][j]-S[i+1][j]>3) or (S[i][j]-S[i-1][j]>3) ):
                        S[i][j]-=1
                        S[ic][jc]+=1
                        ava=True
                    elif ((S[i][j]-S[i][j+1]>2) or (S[i][j]-S[i][j-1]>2) or (S[i][j]-S[i+1][j]>2) or (S[i][j]-S[i-1][j]>2) )and (pc>=p):
                        S[i][j]-=1
                        S[ic][jc]+=1
                        ava=True 
                    else:
                        ava=False
    return (S)




                        
