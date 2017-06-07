import networkx as  nx
from threading import Thread
import time
try: import psyco; psyco.full()
except: pass

def modu11(G,U,U1):
    cpt=0
    for i in U:
        for j in U1:
            if G.has_edge(i,j):
                cpt=cpt+1
    return(cpt)
def modu1(G,U,N):

    n=len(U);
    #t=nx.degree(G);
    #N=len(G.edges())
    S=G.subgraph(U)
    cpt=float(S.number_of_edges())
    sum1=0;
    nodedeg=G.degree(U)
    d=float(sum(nodedeg.values()))
    b=(d/(2*N))



    sum1=(cpt/N)-(b**2)
    res=[]
    res.append(sum1)
    res.append(cpt)
    res.append(d)
    res.append(b)
    return(res)	
def Based(f,sep):
    ls=f.readlines()
    print(len(ls))
    t=[]
    for i in range(len(ls)) :
        t.append(list(range(2)))
    k=0
    for i in ls:
        l=i.split(sep)
        t[k][0]=int(l[0])
        t[k][1]=int(l[1])
        k=k+1
    G=nx.Graph()
    i=0
    #while i<n:
        #G.add_node(i)
        #i=i+1
    i=0
    while i<len(t):
        G.add_edge(t[i][0],t[i][1])
        i=i+1
    print(len(G.nodes()))

    print(len(G.edges()))




    ns=G.number_of_nodes()
    N=G.number_of_edges()
    den=nx.density(G)
    print(den)
    if den<0.001:
        se=0.25
    else:
        se=0.5
    
    
    i=0
    
    w1=[]
    tps1= time.time()
    T1=G.nodes()
    while i<ns:
        cpt1=0
        xx=G.neighbors(T1[i])
        a=len(xx)
        j=0
        while j < a-1:
            j1=j+1
            while j1<a:
                if  G.has_edge(xx[j],xx[j1]):
                   cpt1=cpt1+1
                j1=j1+1
            j=j+1
        
        w1.append(cpt1)
        i=i+1
    print('b')

    T=G.edges()

    w=[]
    w2=[]
    cp=[]
    #TT=T

    i=0
    wp=[]
    tt=[]
    ab=[]
    pp=[]
    w5=[]


    while i<N:
        a=G.degree(T[i][0])
        b=G.degree(T[i][1])
        cpt=len(sorted(nx.common_neighbors(G, T[i][0], T[i][1])))
        if cpt==0:
        
            
            #w4=w1[T1.index(T[i][0])]+w1[T1.index(T[i][1])]
            ab.append([0,T[i][0], T[i][1]])
        elif (cpt/(a+b-cpt))<se:
            #pp.append([T[i][0], T[i][1]])
            #wp.append(cpt)
            w4=w1[T1.index(T[i][0])]+w1[T1.index(T[i][1])]
            w5.append([(w4/(cpt*(a+b))),T[i][0], T[i][1]])
        i=i+1

    print('a')
    tps2= time.time()
    l=w5
    print('le temps', tps2-tps1)

    #print('a')
    k=len(l)
    print(k)
    print('v')
    

    l.sort(reverse=True)
    #ab.sort(reverse=True)
    l=ab+l
    
    tps1= time.time()
    print('v')
    #G11=nx.Graph()
    G11 = G.copy()
    i=0
    print('problèèèèèèèèèème')
    G1=G
    m1=0
    sup=[]
    aj=[]
    while i<len(l):



        e1=l[i][1]
        e2=l[i][2]
        G1.remove_edge(e1,e2)
        y=G.degree(e1)
        y1=G.degree(e2)












        if y<1 or y1<1 :#or m<m1 :
        #if len(la)<4:


            G1.add_edge(e1,e2)
        else:
            aj=[e1,e2]


            sup.append(aj)
            #m1=m
        i=i+1;

    gr = list(nx.connected_component_subgraphs(G1))



    k=0
    m=0
    g=[]
    #g=[i.nodes() for i in gr]
    for i in gr:


        g.append(i.nodes())








    i1=0
    while i1<len(g):
        ii=g[i1]
        if len(ii)<4:
            #print(len(g))
            i=len(sup)-1
            while i>=0:
                b=0
                if sup[i][0] in ii :
                    if not(sup[i][1] in ii):
                        b=1
                        break
                    else:
                        sup.pop(i)
                        i-1                     
                                               
                if  sup[i][1] in ii:
                    if not(sup[i][0] in ii):
                        b=2
                        break
                    else:
                        sup.pop(i)
                        i=i-1                       
                                              


                i=i-1
            if b==1:
                for kk in g:
                    if sup[i][1] in kk:


                        r=list(set(ii)|set(kk))
                        ind1=g.index(kk)
                        ind2=i1
                        g[ind1]=r
                        g.remove(g[ind2])

                        break


            elif b==2:
                for kk in g:
                    if sup[i][0] in kk:


                        r=list(set(ii)|set(kk))
                        ind1=g.index(kk)
                        ind2=i1
                        g[ind1]=r
                        g.remove(g[ind2])

                        break
            else:
                i1=i1+1
        else:
            i1=i1+1
    m=0
    k=1
    mm=[]
    mm1=[]
    #m2=[]
    m3=[]
    for i in g:
        #print(i)
        temp=modu1(G11,i,N)
        #mm.append(temp[0])
        mm1.append(temp[1])
        #m2.append(temp[2])
        m3.append(temp[3])

        #m=m+temp[0]

    #print(m)
    i1=0

    while i1<len(g):
        ii=g[i1]
        #print(len(g))
        i=len(sup)-1
        while i>=0:
            b=0
            if sup[i][0] in ii:
                if not(sup[i][1] in ii):
                    b=1
                    break
                else:
                    sup.pop(i)
                    i=i-1
                                       
            if  sup[i][1] in ii :
                if not(sup[i][0] in ii):
                    b=2
                    break
                else:
                    sup.pop(i)
                    i=i-1
                                      


            i=i-1
        #print('a')    
        if b==1:
            for kk in g:
                if sup[i][1] in kk:

                    r=list(set(ii)|set(kk))
                    ind1=g.index(kk)
                    ind2=i1
                    #aa=mm[ind1]
                    #bb=mm[ind2]
                    rr1=modu11(G11,kk,ii)
                    rr=(rr1/N)-(2*m3[ind1]*m3[ind2])

                    #mo=modu1(G11,r,tt,N)



                    if rr>0:

                        #mo=mm[ind1]+mm[ind2]+rr
                        g[ind1]=r
                        g.remove(g[ind2])
                        #mm[ind1]=[0,(rr1+aa[1]+bb[1]),0,]
                        mm1[ind1]=rr1+mm1[ind1]+mm1[ind2]
                        m3[ind1]=m3[ind1]+m3[ind2]
                        #mm.pop(ind2)
                        mm1.pop(ind2)
                        m3.pop(ind2)


                    else:
                        i1=i1+1



                    break


        elif b==2:
            for kk in g:
                if sup[i][0] in kk:
                    r=list(set(ii)|set(kk))
                    ind1=g.index(kk)
                    ind2=i1
                    #aa=mm[ind1]
                    #bb=mm[ind2]
                    rr1=modu11(G11,kk,ii)
                    rr=(rr1/N)-(2*m3[ind1]*m3[ind2])

                    #mo=modu1(G11,r,tt,N)



                    if rr>0:

                        #mo=mm[ind1]+mm[ind2]+rr
                        g[ind1]=r
                        g.remove(g[ind2])
                       # mm[ind1]=[0,(rr1+aa[1]+bb[1]),0,aa[3]+bb[3]]
                        mm1[ind1]=rr1+mm1[ind1]+mm1[ind2]
                        m3[ind1]=m3[ind1]+m3[ind2]
                        #mm.pop(ind2)
                        mm1.pop(ind2)
                        m3.pop(ind2)


                    else:
                        i1=i1+1



                    break



        else:
            i1=i1+1
    tps2= time.time()        
    m=0
    k=0
    mm=[]
    l1=[]
    #mm1=[]
    #m2=[]
    #m3=[]
    for i in range(ns) :
        l1.append(list(range(1)))
    for i in g:
        #print(i)
        temp=modu1(G11,i,N)
        mm.append(temp)
        #mm1.append(temp[1])
        #m2.append(temp[2])
        #m3.append(temp[3])
        for r in i:
            l1[T1.index(r)]=k
        k=k+1   

        m=m+temp[0]

    print(m)
    #print(l1)

    
    print('le temps', tps2-tps1)
class poids(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, T, deb, fin,G,W1,p,T1,se,l):
        Thread.__init__(self)
        self.T = T
        self.deb=deb
        self.fin=fin
        self.G=G
        self.w1=W1
        self.p=p
        self.T1=T1
        self.se=se
        self.l=l


    def run(self):
        l=[]


        i = self.deb
        while i < self.fin:
            e1=self.T[i][0]
            e2=self.T[i][1]
            #a=len(self.G[e1])#aa[1]
            #b=len(self.G[e2])#bb[1]
            cpt=self.p[i]
            ind1=self.T1.index(e1)
            ind2=self.T1.index(e2)
            b2=self.w1[ind1][1]+self.w1[ind2][1]
            #tes=cpt/b2
            ww1=self.w1[ind1][0]+self.w1[ind2][0]
            ww3=(ww1)/(cpt*(b2))#(((a-1)*a)+(b*(b-1))))#*(a+b))
            l.append([ww3,e1,e2])
            i=i+1
            
        self.l=l