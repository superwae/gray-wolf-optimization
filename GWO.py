import random
import math 

max_iter=10
N=5
minx=0
maxx=200
wolfs=[]
bool=False
alphax=100000
alphay=100000
betax=100000
betay=100000
deltax=100000
deltay=100000

#0<x1,x2<200
#y=x1*x2-x1
def target_function(x1,x2):
    y=x1*x2-x1
    return y



class wolf:
  def __init__(self, postionx,postiony):
    self.postionx = postionx
    self.postiony = postiony
    

  def testfit(self,postionx,postiony):
    global alphax
    global alphay
    global betax
    global betay
    global deltax
    global deltay
    if(target_function(postionx,postiony)<target_function(alphax,alphay)):
        temp1x,temp1y,temp2x,temp2y=alphax,alphay,betax,betay
        alphax=postionx
        alphay=postiony
        betax=temp1x
        betay=temp1y
        deltax=temp2x
        deltay=temp2y
    elif(target_function(postionx,postiony)<target_function(betax,betay)):
        tempx,tempy=betax,betay
        betax=postionx
        betay=postiony
        deltax=tempx
        deltay=tempy
    elif(target_function(postionx,postiony)<target_function(deltax,deltay)):
        deltax=postionx
        deltay=postiony


for i in range (N):
    x=random.randint(minx,maxx)
    y=random.randint(minx,maxx)
    postion={x,y}
    currwolf=wolf(x,y)
    wolfs.append(currwolf)
    currwolf.testfit(x,y)
for i in range (max_iter):
    for j in wolfs:
        a=(1*(i/max_iter))
        A1=(2*a*random.randint(0,1))-a
        C1=2*random.randint(0,1)
        D_alphax=(C1*(j.postionx)-j.postionx)
        D_alphay=(C1*(j.postiony)-j.postiony)
        X1x=alphax-A1*D_alphax
        X1y=alphay-A1*D_alphay

        A2=(2*a*random.randint(0,1))-a
        C2=2*random.randint(0,1)
        D_betax=(C2*(j.postionx)-j.postionx)
        D_betay=(C2*(j.postiony)-j.postiony)
        X2x=alphax-A2*D_alphax
        X2y=alphay-A2*D_alphay

        A3=(2*a*random.randint(0,1))-a
        C3=2*random.randint(0,1)
        D_deltax=(C3*(j.postionx)-j.postionx)
        D_deltay=(C3*(j.postiony)-j.postiony)
        X3x=alphax-A3*D_alphax
        X3y=alphay-A3*D_alphay

        Xnewx=(X1x+X2x+X3x)/3
        Xnewy=(X1y+X2y+X3y)/3
        if(target_function(Xnewx,Xnewy)<target_function(j.postionx,j.postiony)):
            j.postionx=Xnewx
            j.postiony=Xnewy
            print(alphax,alphay)
            print(target_function(alphax,alphay))
    for i in range(N):
        j.testfit(j.postionx,j.postiony)   
