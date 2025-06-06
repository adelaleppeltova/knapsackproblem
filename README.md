# Optimalizace batohového problému pomocí genetického algoritmu

Tento projekt implementuje genetický algoritmus (GA) pro řešení klasického **batohového problému**.
Cílem je nalézt takovou kombinaci položek, která nepřekročí maximální povolenou hmotnost batohu, zároveň maximalizuje celkovou hodnotu a využije dostupný prostor co nejefektivněji.

## Použitý přístup

- Genetický algoritmus (GA) –
- Reprezentace jedince: binární vektor, (např. [1, 0, 1, 1, 0])
- Fitness funkce zohledňuje hodnotu a počet položek, penalizuje překročení hmotnosti.
- Operace: selekce, křížení, mutace s nízkou pravděpodobností.

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

---

**Autor:** Bc. Adéla Leppeltová  
**Fakulta informatiky a managementu, Univerzita Hradec Králové, 2025**
