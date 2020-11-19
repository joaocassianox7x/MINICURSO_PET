"""
PROGRAMA PARA PLOTAR A DIFERENCA DE TEMPO ENTRE EIG, EIGH, EIGVALS E EIGVALSH.
"""


import time as t
import matplotlib.pyplot as plt
import numpy.linalg as alg
import numpy as np

t0,t1,t2,t3 = [],[],[],[]


xis = range(50,1500+50,50)

for dim in xis:
    Me = np.random.random((dim,dim))
    Me+=np.transpose(Me)
    
    Ma = np.random.random((dim,dim)) #matriz aleatória
    
    ti = t.time()
    val1,vel1 = alg.eig(Ma) #autovalores e autovetores de uma matriz qualquer
    t0.append(t.time()-ti)
    
    
    ti = t.time()
    vec2,vel2 = alg.eigh(Me) #autovalores e autovetores de uma matriz hermitiana
    t1.append(t.time()-ti)

    ti = t.time()
    val1 = alg.eigvals(Ma) #autovalores de uma matriz qualquer
    t2.append(t.time()-ti)
    
    ti = t.time()
    val2 = alg.eigvalsh(Me) #autovalores de uma matriz hermitiana
    t3.append(t.time()-ti)

plt.plot(xis,t0,'k-o')
plt.plot(xis,t1,'y-o')
plt.plot(xis,t2,"b-o")
plt.plot(xis,t3,'g-o')

plt.ylabel("Tempo [s]")
plt.xlabel("Dimensão [n]")
plt.legend(["eig","eigh","eigvals","eigvalsh"])
plt.xlim(xis[0],xis[-1])
plt.savefig("figura.pdf")