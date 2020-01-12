import numpy as np
import scipy.sparse as sp
import matplotlib.pyplot as plt

# Parametry Struktury 1D, dwu bramkowego tranzystora
Vg = 0.8  # Napięcie bramki [V]
Na = 2 * 10 ** 18  # Koncenatracja domieszki akceptorowej [cm^-3]
ni = 1e10  # Koncentracja dziur/elektronów samoistnych [cm^-3]
t_Ox = 1.3 * 10 ** -7  # Grubość tlenku bramki [m]
t_Si = 16 / 2 * 10 ** -7  # Grubość krzemu [m]
eps = 8.854187817 * 10 ** -14  # Przenikalność elektryczna w próżni [F/cm]
eps_si = eps * 11.7  # Przenikalność elektryczna w krzemie [F/cm]
eps_ox = eps * 3.9  # Przenikalność elektryczna w tlenku bramki [F/cm]
q = 1.602177335 * 10 ** -19  # Ladunek elementarny [C]
kb = 1.380658 * 10 ** -23  # Stała Boltzmana [J/K]
T = 300  # Temperatura [K]
phi_T = kb * T / q  # % Potencjał termiczny [V]

# Parametry do Symulacji
# W strukturze tranzystora została podzieloną siatką o stałej odległości między węzłami siatki.
# Dla uproszczenia założono stały krok obliczeniowy.
Nx = 500  # Liczba węzłow siatki
h = t_Si / Nx  # Krok obliczoniowy
eps_aim = 5 * 10 ** -15  # Dokładność obliczeń, do której będzie dążyć metoda Newtona-Rhapsona.

# Równanie Poissona
# Należy wyliczyć div(grad(psi)) = -q/eps * ( p - n + Nd - Na)
# W zadaniu rozkład potencjału będziemy wyliczać tylko dla krzemu dlatego nasze Nd=0, nie użyto domieszki donorowej
#
# Do obliczenia psi[pot.el] potrzebne nam są nam jeszcze dwa równania na niewiadome p i n.
# Zostaną obliczone za pomocą następujących wzorów:
def n(psi_vec):
    return ni * np.exp(psi_vec / phi_T)
def p(psi_vec):
    return ni * np.exp((-psi_vec) / phi_T)

# Dzięki nim możemy przedstawić równanie Poissona jako równanie z jedną zmienną.
def poisson(psi_vec):
    return (-h ** 2 * q / eps_si) * (p(psi) - n(psi) + Na)
def poisson_I(psi_vec):
    return (-h ** 2 * q / eps_si / phi_T) * (-p(psi_vec) - n(psi_vec))

# Jako, że musimy wyznaczyć rozkład pot.el obliczenia zostaną wykonane macierzowo
#                                                       Ax=B
# Metodą róznic skończonych uzyskujemy wzór na lewą stronę równania Poissona(A) ( laplasjan(psi) )
# Za pomocą potencjału w poprzednim(i-1), aktualnym(i) i następnym(i+1) węźle
# można wyznaczyć wartość laplasjanu w węźle i.
#                                 laplasjan(psi|i) = (psi|i-1 - 2*psi|i + psi|i+1) / h^2
# Współczynniki są więc następujące [1, -2, 1] i kształtujemy z nich macierz współczynników.
coeff_arr = sp.diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)).toarray()

# Warunki brzegowe wynikające z ciągłości pot.el na granicy tlenku bramki i krzemu
coeff_arr[0, 0] = 1 + (eps_si * t_Ox / (eps_ox * h))
coeff_arr[0, 1] = -(eps_si * t_Ox / (eps_ox * h))

# Warunki brzegowe w środku struktury
coeff_arr[Nx - 1, Nx - 1] = -1
coeff_arr[Nx - 1, Nx - 2] = 1

# Wektor wartości początkowych, zostały wybrane eksperymentalnie z przybliżeniem zakładającym, że
# Maksimum pot.el będzie przy tlenku bramki a w środku struktury będzie minimum pot.el
# Maksimum jest napięcie bramki V_g.
psi = np.linspace(Vg, 0, Nx)

# Pomocnicze listy do przechowywania wartości błędu i pot.el w kolejnych iteracjach
eps_per_iter = []
psi_per_iter = []

# Metoda iteracyjna Newtona-Rhapsona
steps_c = 0
while eps > eps_aim:
    L = coeff_arr - np.diag(poisson_I(psi))
    R = poisson(psi) - poisson_I(psi) * psi

    # Warunki brzegowe dla prawej strony równania macierzowego
    R[0] = Vg
    R[-1] = 0

    # Rozwiązanie liniowego równania macierzowego
    psi_prev_iter = psi
    psi = np.linalg.solve(L, R)

    # Skorzystanie z symetryczności struktury
    # 2 bramkowego tranzsytora i zachowanie kolejnych wartości wektora pot.el
    psi_flipped = np.flip(psi)
    psi_concat = np.concatenate((psi, psi_flipped))
    psi_per_iter.append(psi_concat)

    eps = np.abs(np.max(psi_prev_iter - psi))
    eps_per_iter.append(eps)
    steps_c += 1

# Wykreślenie potencjału elektrostatycznego w funkcji y
# Dla kilku iteracjii
plt.figure(1)
for i in np.arange(0, steps_c, 2):
    plt.plot(psi_per_iter[i])

# Wykreślenie błędu w kolejnych iteracjach
plt.figure(2)
plt.semilogy(eps_per_iter)
plt.show()
