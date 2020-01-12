import numpy as np
import scipy.sparse as sp
#import matplotlib.pyplot as plt

# Parametry struktury
N_a = 2*10**18 #[cm**-3] koncenatracja domieszki akceptorowej
n_i = 1e10
t_Ox = 1.3*10**-7
t_Si = 16/2*10**-7
V_g = 0.8

#stałe fizyczne

eps = 8.854187817*10**-14
eps_Si = eps*11.7
eps_Ox = eps*3.9

q = 1.602177335*10**-19# %[C] ładunek elementrany
k = 1.380658*10**-23# %[J/K] stała Boltzmana

T = 300# %[K] Temperatura
phi_T = k*T/q# %[V] potencjał termiczny

#Parametry symulacji
Nx=100 #liczba wezłow siatki
eps_aim =10**-15

M = sp.diags([1, -2, 1], [-1, 0, 1], shape=(Nx,Nx),dtype=int).toarray()
M[0,0] =1; M[0,1] =0
M[Nx-1,Nx-1] =1; M[Nx-1,Nx-2] =0

psi = np.linspace(V_g,V_g,Nx)

print(psi)
print(M)

#iteracyjna metoda Newtona

steps_c = 0
#while(eps > eps_aim)
#    steps_c +=1
#    print(steps_c)

print(steps_c)


#laplasjan(pot.el) -q/e( p - n + Nd - Na)
#n = ni * exp((pot.el - pot.Fermiego)/phi_T)
#p = ni * exp((pot.Fermiego - pot.el)/phi_T)
