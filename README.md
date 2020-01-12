# Projekt MOBI Mikroelektronika 2019/20
## Rozkład potencjału w dwubramkowym tranzystorze

### Wykonane przez: Mateusz Wąsowski, Adam Drawc

### Cel projektu:

W dwubramkowym krzemowym tranzystorze MOS należy wykreślić rozkład potencjału elektrostatycznego.

Do tego potrzebne jest skonstruowanie opisu jednowymiarowego tej struktury w przekroju y.
Do zadania przedstawiony został rysunek tranzystora i struktury pasmowe na Rys.2 wziętym wprost z instrukcji do projektu.

![alt text](https://github.com/gracja000/mobi-proj1/blob/master/png/Struktura.png)

Opis struktury należy stworzyć używając Metody Różnic Skończonych oraz algorytmu Newtona.
Rozkład potencjału zostanie wyznaczony dla zadanego napięcia bramki Vg równego 0.8V.

### Opis struktury:
#### Stałe fizyczne i inne parametry:
- ładunek elementarny q = 1,602177335 x 10–19 C,
- przenikalność elektryczna próżni ε0 = 8,854187817 x 10–12 F/m,
- przenikalność elektryczna dwutlenku krzemu εox = 3,9 ε0,
- przenikalność elektryczna krzemu εSi = 11,7 ε0,
- stała Boltzmanna kB =  1,380658 x 10–23 J/K,
- koncentracja samoistna nośników w krzemie ni = 1 x 10^10 cm–3,
- temperatura T = 300 K.
#### Parametry tranzystora:
- koncentracja domieszki akceptorowej w obszarze aktywnym NA = 2 x 1018 cm–3,
- grubość tlenku bramkowego tox = 1,3 nm,
- grubość obszaru aktywnego (krzemu) tSi = 16 nm,
- bramka metalowa (brak zagięcia pasm); różnica prac wyjścia bramka-  podłoże ΦMS = 0

### Założenia Symulacji
- Liczba węzłów siatki Nx = 500.
- Stały krok obliczeniowy w algorytmie Newtona.
- Krok algorytmu Newtona h =tsi/Nx.
- Dokładność wyniku, do którego zbiega algorytm Newtona eps_aim = 5 * 10^-15.
- Jako, że struktura jest symetryczna w symulacji liczymy wartości tylko dla połowy tranzystora, które do wykresów zostaną zwierciadlanie odbite.
- Opis struktury nie uwzględnia równań transportu
- Wartości początkowe w węzłach zostały wybrane jako liniowo opadające od Vg do 0
![alt text](https://github.com/gracja000/mobi-proj1/blob/master/png/Zalozenia.png)

#### Miara pozwalająca oszacować na bieżąco odległość rozwiązania w danej iteracji od rozwiązania “dokładnego”

Jako miarę przyjęto wartość bezwzględną maksymalnej różnicy po wartościach potencjału wyznaczonych w poprzedniej iteracji i iteracji aktualnej. Jeżeli wynik jest mniejszy lub równy dokładności zadanej algorytmu Newtona to posiadamy wynik “dokładny”.

Wartość maksymalna została wzięta w tym przypadku ponieważ wynik ma być “dokładny” dla każdego węzła struktury.

### Wyniki:

![alt text](https://github.com/gracja000/mobi-proj1/blob/master/Wyniki/figure_1.png)

![alt text](https://github.com/gracja000/mobi-proj1/blob/master/Wyniki/figure_2.png)
