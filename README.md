## A simple DigiKey search helper

This little tool helps find parts on digikey. Give it a search query and it will present you results, so you can quickly compare and select the best part for you. Search is keyword-based, but tool filters results a bit - for example removes too expensive bulk orders, or non-stocked parts.

### How to use

First, get some DigiKey api credentials. Export them, like that:
```
export DIGIKEY_CLIENT_ID=....
export DIGIKEY_STORAGE_PATH=/tmp
export DIGIKEY_CLIENT_SECRET=...
```
Then you can run the script (if you want a 12pf SMD 0603 capacitor):
```
./digikey-search.py "12pF 0603"
```

That will draw you the nice table with all the options:
```
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name                 ┃ Description                      ┃ Manufacturer                  ┃ Quantity ┃ M/O ┃ Price ┃ DigiKey part number          ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0603N120J500CT       │ CAP CER 12PF 50V C0G/NP0 0603    │ Walsin Technology Corporation │ 92389    │ 1   │ 0.1   │ 1292-1480-1-ND               │
│ 0603N120J500CT       │ CAP CER 12PF 50V C0G/NP0 0603    │ Walsin Technology Corporation │ 92389    │ 1   │ 0.1   │ 1292-1480-6-ND               │
│ C0603C120K5HAC7867   │ CAP CER 0603 12PF 50V ULTRA STAB │ KEMET                         │ 13016    │ 1   │ 0.1   │ 399-C0603C120K5HAC7867CT-ND  │
│ C0603C120K5HAC7867   │ CAP CER 0603 12PF 50V ULTRA STAB │ KEMET                         │ 13016    │ 1   │ 0.1   │ 399-C0603C120K5HAC7867DKR-ND │
│ 06031A120JAT4A       │ CAP CER 12PF 100V C0G/NP0 0603   │ AVX Corporation               │ 73131    │ 1   │ 0.1   │ 478-10188-1-ND               │
```

### Installation

```
pip install git+https://github.com/dossalab/digikey-helper
```
