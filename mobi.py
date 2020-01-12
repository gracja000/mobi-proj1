import numpy as np
import scipy.sparse as sp
#import matplotlib.pyplot as plt

# Parametry struktury
N_a = 2*10**18 #[cm**-3] koncenatracja domieszki akceptorowej
t_Ox = 1.3*10**-7
t_Si = 16/2*10**-7
V_g = 0.8

#stałe fizyczne
n_i = 1e10
eps = 8.854187817*10**-14
eps_Si = eps*11.7
eps_Ox = eps*3.9

q = 1.602177335*10**-19# %[C] ładunek elementrany
k = 1.380658*10**-23# %[J/K] stała Boltzmana

T = 300# %[K] Temperatura
phi_T = k*T/q# %[V] potencjał termiczny

#Parametry symulacji
Nx=100 #liczba wezłow siatki

M = sp.diags([1, -2, 1], [-1, 0, 1], shape=(Nx,Nx),dtype=int).toarray()
print(M)


#laplasjan(pot.el) -q/e( p - n + Nd - Na)
#n = ni * exp((pot.el - pot.Fermiego)/phi_T)
#p = ni * exp((pot.Fermiego - pot.el)/phi_T)
