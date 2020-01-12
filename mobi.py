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
h = t_Si/Nx
eps_aim =10**-15

#równanie poissona
n = lambda psi: n_i*np.exp((psi)/phi_T)
p = lambda psi: n_i*np.exp((-psi)/phi_T)

poisson = lambda psi: (-h**2*q/eps_Si)*(p(psi)-n(psi)+N_a)
poisson_div = lambda psi: (-h**2*q/eps_Si/phi_T)*(-p(psi)-n(psi))



M = sp.diags([1, -2, 1], [-1, 0, 1], shape=(Nx,Nx)).toarray()
M[0,0] = 1 + (eps_Si*t_Ox/(eps_Ox*h))
M[0,1] = -(eps_Si*t_Ox/(eps_Ox*h))
M[Nx-1,Nx-1] =-1; M[Nx-1,Nx-2] =1

psi = np.linspace(V_g,0,Nx)

steps_c = 0
while(eps > eps_aim):

    L = M-np.diag(poisson_div(psi))
    P = poisson(psi)-poisson_div(psi)*psi

    P[0] = V_g;
    P[-1] = 0;

    #Obliczenia
    psi_prev = psi
    psi= np.linalg.solve(L,P)

    steps_c +=1
    print(steps_c)

    eps = np.abs(np.max(psi_prev-psi));
    print(eps)



print(steps_c)
print(psi)
