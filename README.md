### MOBI Projekt Mikro 2 bramkowy tranzystor

**Cel:** Wyznaczyć z równania Poissona rozkład potencjału elektrostatycznego w dwubramkowym tranzystorze

**Założenia:**
- stały krok obliczeniowy
- bez równań transportu 
- jako, że tranzystor jest symetryczny można do obliczeń wziąć tylko połowę tranzystora
- warunki brzegowe Dirichletta/Neumanna
     ```
     f'(x) = 0 
     ```
- w środku struktury mamy max czegoś więc również
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
    ni - 
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