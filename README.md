### MOBI Projekt Mikro 2 bramkowy tranzystor

**Cel:** Wyznaczyć z równania Poissona rozkład potencjału elektrostatycznego w dwubramkowym tranzystorze

**Założenia:**
- stały krok obliczeniowy
- bez równań transportu
- jako, że tranzystor jest symetryczny można do obliczeń wziąć tylko połowę tranzystora
- warunki brzegowe Dirichletta/Neumanna ????
     ```
     f'(x) = 0
     ```
- w środku struktury mamy max czegoś więc również ????
    ```
    f'(pot.el) = 0
    ```
- Równanie Poissona wyraża się jako:
    ```
    div(D) = -g
    D - indukcja elektryczna
    g - gęstość ładunku

    div(grad(pot.el)) = -g/e = -q/e( p - n + Nd - Na)
    e - przenikalność elektromagnetyczna półprzewodnika
    q - ładunek elektronu (?)
    p, n - koncentracja dziur(p), elektronów(n)
    Nd, Na - koncentracja dziur(Nd) i elektronów(Na) domieszek
    ```
- Zależność koncentracji od potencjału el.
    ```
    n = ni * exp((pot.el - pot.Fermiego)/(kb*T/q))
    p = ni * exp((pot.Fermiego - pot.el)/(kb*T/q))

    n*p = ni^2

    pot.Fermiego jest rózny dla dziur i elektronów gdy przez tranzystor płynie prąd
    ni - koncentracja samoistna
    kb - stała Boltzmanna
    T - temperatura ok.
    ```
- Dlatego Div(D) -> div(grad(pot.el))
  ```
  E = -q * pot.el
  ```
- Jak przybliżyć pochodną?
    ```
    Metoda różnic skończonych:
    druga pochodna z pot.el będzie obliczona jako:
    delta^2 pot.el/ delta x^2 = ( pot.el|i-1 + 2*pot.el|i + pot.el|i+1 ) / h^2

    Należy to wyznaczyć dla każdego węzła/kroku obliczeniowego/struktury.
    ```
- Macierzowe wyznaczenie pot.el
  ```
  laplasjan(pot.el) = -q/e (p - n + Nd -Na)

  z tego wychodzi nam macierz w pewnym sensie:

  [macierz współczynników, 2 wymiary]*[macierz pot. el, wektor] = [p(pot.el),wektor]

  do macierzy wspólczynnikow itp wstawiamy na poczatek i koniec warunki brzegowe

  a więc wyznaczenie rozkladu bedzie rozwiazaniem macierzy
  a dla 2 bramkowego tranzystora jedynym co sie zmienia są warunki brzegowe(??MAM NADZIEJE??)
  ```
### Plan obliczeń
```
                            laplasjan(pot.el) -q/e( p - n + Nd - Na)         (1)

    3 niewiadome: pot.el, p i n

    Wzory na koncentracje:
                            n = ni * exp((pot.el - pot.Fermiego)/(kb*T/q))   (2)
                            p = ni * exp((pot.Fermiego - pot.el)/(kb*T/q))   (3)

    Bonus niewiadoma: pot.Fermiego..  Ef = -q * Vg ???

    Mamy więc 3 niewiadome oraz 3 równania:
    Możemy złożyć je w jedno:

                    laplasjan(pot.el) = -q/e * ((ni * exp((pot.Fermiego - pot.el)/(kb*T/q)) -
                                        ni * exp((pot.el - pot.Fermiego)/(kb*T/q))) + Nd - Na)   (4)

    aby wyznaczyć to równanie możnaby przenieść wszystko
    na lewą stronę równania a następnie wyznaczyć miejsce zerowe funkcji.

    Jednakże zrobione zostanie to inaczej:
    lapsajan będący drugą pochodną pot.el po x wyznaczymy metodą różnic skończonych.

            laplasjan(pot.el) = (pot.el|i-1 + 2*pot.el|i + pot.el|i+1 ) / h^2           (5)

    czyli potencjal w punkcie x => pot.el(x|i) wyznaczamy na podstawie dwóch sąsiednich kroków.

    Następnie zapiszemy równanie Poissona dla pot.el w formie macierzowej:
                                            Ax = B
    gdzie:
    x to pot.el dla struktury podzielonej przez siatkę ze stałem krokiem obliczeń.
    A - macierz współczynników po prawej stronie w liczniku wzoru (5).
    B - jest prawą stroną wzoru (4).

    Uzywając Metody Newtona-Rhapsona będziemy chceli wyznaczyć coś ???

```
### Założenia Symulacji
-Liczba węzłów siatki Nx = 500.
-Stały krok obliczeniowy w algorytmie Newtona.
-Krok algorytmu Newtona h =tsi/Nx.
-Dokładność wyniku, do którego zbiega algorytm Newtona eps_aim = 5 * 10^-15.
-Jako, że struktura jest symetryczna w symulacji liczymy wartości tylko dla połowy tranzystora, które do wykresów zostaną zwierciadlanie odbite.
-Opis struktury nie uwzględnia równań transportu
-Warunki brzegowe struktury są wyrażone poprzez:
```
  f'(ψ)=0 - w środku struktury
  Vg=1(1+sitoxoxh) -2(sitoxoxh) - na granicy tlenku bramki oraz obszaru aktywnego ponieważ musimy zachować ciągłość potencjału elektrycznego
```
-Wartości początkowe w węzłach zostały wybrane jako liniowo opadające od Vg do 0

## Miara pozwalająca oszacować na bieżąco odległość rozwiązania w danej iteracji od rozwiązania “dokładnego”
```
Jako miarę przyjęto wartość bezwzględną maksymalnej różnicy po wartościach potencjału wyznaczonych w poprzedniej iteracji i iteracji aktualnej. Jeżeli wynik jest mniejszy lub równy dokładności zadanej algorytmu Newtona to posiadamy wynik “dokładny”.

Wartość maksymalna została wzięta w tym przypadku ponieważ wynik ma być “dokładny” dla każdego węzła struktury.
```
### Wyniki:

![alt text](https://github.com/gracja000/mobi-proj1/blob/master/Wyniki/figure_1.png)

![alt text](https://github.com/gracja000/mobi-proj1/blob/master/Wyniki/figure_2.png)
