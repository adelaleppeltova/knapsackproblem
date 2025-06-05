# Optimalizace batohového problému pomocí genetického algoritmu

Tento projekt implementuje genetický algoritmus (GA) pro řešení klasického **0/1 batohového problému** v jazyce Python.
Cílem je najít takovou kombinaci položek, která se vejde do batohu s omezenou kapacitou a zároveň maximalizuje celkovou hodnotu a efektivitu využití prostoru.

## Použitý přístup

- Genetický algoritmus (GA) inspirovaný evoluční biologií.
- Reprezentace jedince: binární vektor.
- Fitness funkce zohledňuje hodnotu a počet položek, penalizuje překročení hmotnosti.
- Operace: selekce (ruletová), jednobodové křížení, mutace s nízkou pravděpodobností.

## Parametry

| Parametr          | Význam                    | Typická hodnota |
| ----------------- | ------------------------- | --------------- |
| `MAX_WEIGHT`      | Maximální hmotnost batohu | 7.0             |
| `POPULATION_SIZE` | Počet jedinců v generaci  | 50              |
| `GENERATIONS`     | Počet generací algoritmu  | 100             |
| `MUTATION_RATE`   | Pravděpodobnost mutace    | 0.05            |

## Výstup

- Výpis nejlepšího nalezeného řešení.
- Seznam vybraných položek, jejich váha a hodnota.
- Celková hmotnost, hodnota a počet položek.
- Binární reprezentace výsledku.

## Literatura

- Holland, J. H. (1975). _Adaptation in Natural and Artificial Systems_.
- Goldberg, D. E. (1989). _Genetic Algorithms in Search, Optimization, and Machine Learning_.
- Martello, S., & Toth, P. (1990). _Knapsack Problems: Algorithms and Computer Implementations_.
- Mitchell, M. (1998). _An Introduction to Genetic Algorithms_.

---

**Autor:** Bc. Adéla Leppeltová  
**Fakulta informatiky a managementu, Univerzita Hradec Králové**
