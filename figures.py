# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:49:36 2017

@author: m17bompa
"""

from pylab import *

from random import gauss

from mpl_toolkits.mplot3d import Axes3D



def données(x,sigma):
    
    '''
    x : numéro de la figure
    sigma : réel >=0, écart-type du bruit
    
    Cette fonction génère des données bruitées. La sortie est une liste de coordonnées.
    
    '''
    
    global points00
    

    
    if x==20:
        
        ''''' 2 cercles bruités '''''
    
        t1=linspace(0,2*pi,20)
        x1=10*cos(t1)
        y1=10*sin(t1)
        
        t2=linspace(0,2*pi,12)
        x2=10*cos(t2)/3
        y2=10*sin(t2)/3
        
        
        points1=[[x1[k],y1[k]] for k in range(len(x1))]
        points2=[[x2[k],y2[k]] for k in range(len(x2))]
        
        points0=[points1,points2]
        


    
    
    elif x==21:
        
        ''''' 2 cercles avec un grand nombre de points '''''
        
        t1=linspace(0,2*pi,50)
        x1=10*cos(t1)
        y1=10*sin(t1)
        
        t2=linspace(0,2*pi,30)
        x2=5*cos(t2)
        y2=5*sin(t2)
        
        
        points1=[[x1[k],y1[k]] for k in range(len(x1))]
        points2=[[x2[k],y2[k]] for k in range(len(x2))]
        
        points0=[points1,points2]
        

        
        
        
    elif x==22:
        
        ''' Deux cercles de 50 points chacun rapprochés '''
        
        t=linspace(0,2*pi,50)
        
        points1=[[10*cos(t),10*sin(t)] for t in t]
        points2=[[8*cos(t),8*sin(t)] for t in t]
        
        points0=[points1,points2]
        

        


        
    elif x==23:
        
        ''''' 2 rectangles de tailles différentes générés au hasard '''''
        
        x1 = [2*((random()-1)-0.6) for i in range(40)]
        y1 = [2*(3*(random()-0.5)) for i in range(40)]
        
        x2 = [2*(2*(random())+0.3) for i in range(80)]
        y2 = [2*(0.5*(random()-0.5)) for i in range(80)]

        
        points1=[[x1[k],y1[k]] for k in range(len(x1))]
        points2=[[x2[k],y2[k]] for k in range(len(x2))]
        
        points0=[points1,points2]
        

        
    
    elif x==24:
        
        ''''' 2 cercles rapprochés avec énormément de points'''''
        
        t1=linspace(0,2*pi,150)
        x1=10*cos(t1)
        y1=10*sin(t1)
        
        t2=linspace(0,2*pi,150)
        x2=10*cos(t2)/1.3
        y2=10*sin(t2)/1.3
        
        
        points1=[[x1[k],y1[k]] for k in range(len(x1))]
        points2=[[x2[k],y2[k]] for k in range(len(x2))]
        
        points0=[points1,points2]
        

        
    elif x==25:
        
        ''' Un cercle et un carré concentriques '''
        
        points1=[[10*(random()-0.5),10*(random()-0.5)] for _ in range(150)]
        points2=[[10*cos(t),10*sin(t)] for t in linspace(0,2*pi,50)]
        
        points0=[points1,points2]
        
        
        
        
        
    elif x==26:
        
        ''' Deux cercles proches avec peu de points '''
        
        points1=[[(30/pi)*cos(t),(30/pi)*sin(t)] for t in [((2*pi)/60)*i for i in range(60)]]
        points2=[[(26/pi)*cos(t),(26/pi)*sin(t)] for t in [((2*pi)/52)*i for i in range(52)]]
        
        points0=[points1,points2]
        
        
    elif x==27:
        
        ''' Un carrée très bruité, un carré peu bruité '''
        
        x1=5*list(linspace(-5,0,5))
        y1=[]
        for i in range(5):
            y1+=[i for _ in range(5)]
            
        x2=5*list(linspace(2,4,5))
        y2=[]
        for i in range(5):
            y2+=[i*(2/5)+1 for _ in range(5)]
            
        points1=[[x1[i],y1[i]] for i in range(5*5) ]
        points2=[[x2[i],y2[i]] for i in range(5*5)]
        
        points0=[points1,points2]
            
        

        
        
    elif x==30:
        
        ''''' 3 traits '''''
        
        t1=linspace(-1,1,40)
        
        t2=linspace(-1,1,40)

        t3=linspace(-1,1,40)

        
        points1=[[t1[k],1] for k in range(len(t1))]
        points2=[[t2[k],0] for k in range(len(t2))]
        points3=[[t3[k],-1] for k in range(len(t3))]
        
        points0=[points1,points2,points3]
        

        
    elif x==31:
        
        ''' 3 cercles concentriques '''
        
        points1=[[3*cos(t),3*sin(t)] for t in linspace(0,2*pi,30)]
        points2=[[6*cos(t),6*sin(t)] for t in linspace(0,2*pi,40)]
        points3=[[9*cos(t),9*sin(t)] for t in linspace(0,2*pi,50)]
        
        points0=[points1,points2,points3]
        

        
        
    elif x==32:
        
        ''' Trait, carré, cercle '''
        
        points1=[[-4,12*(random()-0.5)] for _ in range(30)]
        points2=[[5*(random()-0.5)+3,5*(random()-0.5)] for _ in range(70)]
        points3=[[10*cos(t),10*sin(t)] for t in linspace(0,2*pi,50)]
        
        points0=[points1,points2,points3]
        
    elif x==33:
        
        ''' Deux carrés, un trait '''
        
        x1=5*list(linspace(-4,-2,5))
        y1=[]
        for i in range(5):
            y1+=[i*(2/5) for _ in range(5)]        
        
        x2=5*list(linspace(2,4,5))
        y2=[]
        for i in range(5):
            y2+=[i*(2/5)+1 for _ in range(5)]
            
        x3=[cos(t) for t in linspace(0,1.5*pi,30)]
        y3=[y for y in linspace(-1,3,25)]  
        
        points1=[[x1[i],y1[i]] for i in range(5*5) ]
        points2=[[x2[i],y2[i]] for i in range(5*5) ]
        points3=[[x3[i],y3[i]] for i in range(5*5) ]
        
        points0=[points1,points2,points3]

        

    
    elif x==40:
        
        ''' Quatre pavés '''
        
        points1=[[random()-5,random()+5] for _ in range(25)]
        points2=[[random()+5,random()+5] for _ in range(25)]
        points3=[[random()-5,random()-5] for _ in range(25)]
        points4=[[random()+5,random()-5] for _ in range(25)]
        
        points0=[points1,points2,points3,points4]
        
    
    elif x==41:
    
        ''' Quatre lettres '''
        
        x1=[x for x in linspace(-10,-8,10)]+[-9 for _ in range(20)]
        y1=[10 for _ in linspace(-10,-8,10)]+[y for y in linspace(10,6,20)]
        
        x2=[-6 for _ in range(20)]+3*[x for x in linspace(-6,-4,10)]
        y2=[y for y in linspace(10,6,20)]+[10 for _ in range(10)]+[8 for _ in range(10)]+[6 for _ in range(10)]
        
        x3=[-1+cos(t) for t in linspace(0,3*pi,25)]
        y3=[y for y in linspace(10,6,25)]
        
        
        x4=[x for x in linspace(2,4,10)]+[3 for _ in range(20)]
        y4=[10 for _ in linspace(-10,-8,10)]+[y for y in linspace(10,6,20)]
        
        points1=[[x1[t],y1[t]] for t in range(len(x1))]
        points2=[[x2[t],y2[t]] for t in range(len(x2))]
        points3=[[x3[t],y3[t]] for t in range(len(x3))]
        points4=[[x4[t],y4[t]] for t in range(len(x4))]
        
        points0=[points1,points2,points3,points4]
        
    elif x==80:
        
        ''' Huit pavés '''
        
        points1=[[random()-3,random()+3] for _ in range(25)]
        points2=[[random(),random()+3] for _ in range(25)]
        points3=[[random()+3,random()+3] for _ in range(25)]
        points4=[[random()-3,random()] for _ in range(25)]
        points5=[[random(),random()] for _ in range(25)]
        points6=[[random()+3,random()] for _ in range(25)]
        points7=[[random()-3,random()-3] for _ in range(25)]
        points8=[[random(),random()-3] for _ in range(25)]
        
        points0=[points1,points2,points3,points4,points5,points6,points7,points8]
        
        
        
    elif x==81:
        
        ''' Huit classes '''
        
        x1=[x for x in linspace(-10,-8,10)]+[-9 for _ in range(10)]
        y1=[10 for _ in linspace(-10,-8,10)]+[y for y in linspace(10,6,10)]
        
        x2=[-6 for _ in range(10)]+3*[x for x in linspace(-6,-4,10)]
        y2=[y for y in linspace(10,6,10)]+[10 for _ in range(10)]+[8 for _ in range(10)]+[6 for _ in range(10)]
        
        x3=[-1+cos(t) for t in linspace(0,3*pi,20)]
        y3=[y for y in linspace(10,6,20)]
        
        
        x4=[x for x in linspace(2,4,10)]+[3 for _ in range(10)]
        y4=[10 for _ in linspace(-10,-8,10)]+[y for y in linspace(10,6,10)]
        
        x5=[x for x in linspace(-10,-8,4)]*4
        y05=[[y0 for _ in range(4)] for y0 in linspace(-2,2,4)]
        y5=[]
        for k in y05:
            y5.extend(k)
            
        x6=[4*cos(t) for t in linspace(0,2*pi,30)]
        y6=[4*sin(t) for t in linspace(0,2*pi,30)]
        
        x7=[2*cos(t) for t in linspace(0,2*pi,20)]
        y7=[2*sin(t) for t in linspace(0,2*pi,20)]
        
        x8=[-12 for _ in range(40)]+[x for x in linspace(-12,6,40)]+[6 for _ in range(40)]+[x for x in linspace(6,-12,40)]
        y8=[y for y in linspace(-6,12,40)]+[12 for _ in range(40)]+[y for y in linspace(12,-6,40)]+[-6 for _ in range(40)]
        
        
        
        points1=[[x1[t],y1[t]] for t in range(len(x1))]
        points2=[[x2[t],y2[t]] for t in range(len(x2))]
        points3=[[x3[t],y3[t]] for t in range(len(x3))]
        points4=[[x4[t],y4[t]] for t in range(len(x4))]
        points5=[[x5[t],y5[t]] for t in range(len(x5))]
        points6=[[x6[t],y6[t]] for t in range(len(x6))]
        points7=[[x7[t],y7[t]] for t in range(len(x7))]
        points8=[[x8[t],y8[t]] for t in range(len(x8))]
        
        points0=[points1,points2,points3,points4,points5,points6,points7,points8]
        
    
    elif x==82:
        
        ''' Huit classes de différente densité '''
        
        x1=[x for x in linspace(-10,-8,10)]+[-9 for _ in range(10)]
        y1=[10 for _ in linspace(-10,-8,10)]+[y for y in linspace(10,6,10)]
        
        x2=[-6 for _ in range(10)]+3*[x for x in linspace(-6,-4,10)]
        y2=[y for y in linspace(10,6,10)]+[10 for _ in range(10)]+[8 for _ in range(10)]+[6 for _ in range(10)]
        
        x3=[-1+cos(t) for t in linspace(0,3*pi,20)]
        y3=[y for y in linspace(10,6,20)]
        
        
        x4=[x for x in linspace(2,4,10)]+[3 for _ in range(10)]
        y4=[10 for _ in linspace(-10,-8,10)]+[y for y in linspace(10,6,10)]
        
        x5=[x for x in linspace(-10,-8,4)]*4
        y05=[[y0 for _ in range(4)] for y0 in linspace(-3,1,4)]
        y5=[]
        for k in y05:
            y5.extend(k)
            
        x6=[4*cos(t) for t in linspace(0,2*pi,30)]
        y6=[4*sin(t) for t in linspace(0,2*pi,30)]
        
        x7=[2*cos(t) for t in linspace(0,2*pi,20)]
        y7=[2*sin(t) for t in linspace(0,2*pi,20)]
        
        x8=[15*cos(t)-2 for t in linspace(0,2*pi,35)]
        y8=[15*sin(t)+2 for t in linspace(0,2*pi,35)]
        
        
        
        points1=[[x1[t],y1[t]] for t in range(len(x1))]#20
        points2=[[x2[t],y2[t]] for t in range(len(x2))]#40
        points3=[[x3[t],y3[t]] for t in range(len(x3))]#20
        points4=[[x4[t],y4[t]] for t in range(len(x4))]#20
        points5=[[x5[t],y5[t]] for t in range(len(x5))]#16
        points6=[[x6[t],y6[t]] for t in range(len(x6))]#30
        points7=[[x7[t],y7[t]] for t in range(len(x7))]#20
        points8=[[x8[t],y8[t]] for t in range(len(x8))]#35
        
        points0=[points1,points2,points3,points4,points5,points6,points7,points8]
        
        M=[0.1]*100+[0.9]*16+[0.1]*60+[0.7]*35   
    
        
        
        
        
    
    elif x==320:
        
        ''' Deux hélices '''
        
        points1=[[9*cos(t),9*sin(t),t] for t in linspace(0,12*pi,100)]
        points2=[[3*cos(t),3*sin(t),t] for t in linspace(0,12*pi,100)]
        
        points0=[points1,points2]
        

    
    
    ''' Bruitage '''

        
    for classe in points0:
        for point in classe:
            for i in range(len(point)):
                point[i]+=gauss(0,sigma)
    
    points00=[[tuple(a) for a in points0[k]] for k in range(len(points0))]
    
    points=[]
    for k in points00:
        points.extend(k)
    
    return points
    
    
def tracer(points,couleur="bo",montrer=True,échelle='Défaut'):
    
    '''
    points : liste, liste de coordonnées (tuples)
    
    Cette fonction trace des données en 2D ou 3D.
    
    '''
    
    if échelle=='Défaut':
        xmin=min([a[0] for a in points])
        xmax=max([a[0] for a in points])
        
        ymin=min([a[1] for a in points])
        ymax=max([a[1] for a in points])
                
        E=((xmin-(xmax-xmin)/4,xmax+(xmax-xmin)/4),(ymin-(ymax-ymin)/4,ymax+(ymax-ymin)/4))
        
    else :
        
        E=échelle

    if len(points[0])==2:
        x=[a[0] for a in points]
        y=[a[1] for a in points]
        
        xlim(E[0][0],E[0][1])
        ylim(E[1][0],E[1][1])
        
        plot(x,y,couleur)
        title("   ")
        
    if len(points[0])==3:
        x=[a[0] for a in points]
        y=[a[1] for a in points]
        z=[a[2] for a in points]
        
        xlim(E[0][0],E[0][1])
        ylim(E[1][0],E[1][1])
        
        gca(projection='3d').plot(x,y,z,couleur)
    
    if montrer==True:
        show()
    
    

    
def données_classées(x,sigma):
    
    '''
    x : numéro de la figure
    sigma : écart-type du bruit
    
    Cette fonction génère des données bruitées et classées.
    La sortie est une liste de (sous-)listes correspondant chacune à un cluster.
    Elle est utilisée pour effectuer des tests de clustering (taux d'erreur).
    
    '''
    
    données(x,sigma)
    return points00
    

def données_bl(x,M):
    
    '''
    x : numéro de la figure
    M : liste, de longueur égale au nombre de points, des écarts-type du bruit propres à chaque point.
    
    Cette fonction génère des données bruitées localement. La sortie est une liste de coordonnées.
    
    '''
    
    global points00
    
    points0=données_classées(x,0)

    points00=[[tuple([points0[k][i][j]+gauss(0,M[i+int(sum([len(points0[k0]) for k0 in range(k)]))]) for j in range(len(points0[0][0]))]) for i in range(len(points0[k]))] for k in range(len(points0))]
    
    points=[]
    for k in points00:
        points.extend(k)

    return points
    
def données_classées_bl(x,M):
    
    '''
    x : numéro de la figure
    M : liste, de longueur égale au nombre de points, des écarts-type du bruit propres à chaque point.
    
    Cette fonction génère des données bruitées localement et classées.
    La sortie est une liste de (sous-listes) correspondant chacune à un cluster.
    Elle est utilisée pour effectuer des tests de clustering (taux d'erreur).
    
    '''
    
    données_bl(x,M)
    
    return points00
    
    
    
    
    
