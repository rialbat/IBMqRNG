<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/logo.png?raw=true" width="400px"/>
</p>

-----------------

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7319546.svg)](https://doi.org/10.5281/zenodo.7319546)
[![License](https://camo.githubusercontent.com/ec1b7780bdc1d8401873e5a03328cc295d44f6b797b35f493b32996c0faad199/68747470733a2f2f706f7365722e707567782e6f72672f6c61726176656c2f6672616d65776f726b2f6c6963656e73652e737667)](https://github.com/rialbat/IBMqRNG/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues-raw/rialbat/IBMqRNG)](https://github.com/rialbat/IBMqRNG)
[![Status](https://img.shields.io/badge/status-alpha-green)](https://github.com/rialbat/IBMqRNG)
[![Python](https://img.shields.io/badge/python-3.9%2C3.10-green)](https://github.com/rialbat/IBMqRNG)

IBMqRNG is a random bit (number) generator for IBM Quantum API written with PySide6.

## Requirements
-----------------
Tested on Python 3.9, 3.10
  
| Package   | Version |
| ---     | --- |
| [**Qiskit**](https://github.com/Qiskit/qiskit) | [![](https://img.shields.io/github/release/Qiskit/qiskit.svg?)](https://github.com/Qiskit/qiskit/releases/tag/0.39.2)  |
| [**Matplotlib**](https://github.com/matplotlib/matplotlib) | [![](https://img.shields.io/github/release/matplotlib/matplotlib.svg?)](https://github.com/matplotlib/matplotlib/releases/tag/v3.6.2) |
| [**PySide6**](https://pypi.org/project/PySide6/) | [![version](https://img.shields.io/badge/release-v6.4.0.1-1182C3)](https://pypi.org/project/PySide6/) |

## Manual installation
-----------------
1. Create a virtual environment in the current directory:
```
python3 -m venv venv
```
2. Activate the virtual environment:
```
# On Mac/Linux:
source venv/bin/activate
# On Windows:
call venv\scripts\activate.bat
```
3. Install requirements:
```
pip install -r requirements.txt
```
4. Run program:
```
python main.py
```
## Guide to using
-----------------
1. Use your [IBMQ](https://quantum-computing.ibm.com/) key.

<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/Auth.png?raw=true" width="300"/>
</p>

2. Choose one of the cloud or local backends.

<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/Main1.png?raw=true" width="600px"/>
</p>

3. Specify the number of shots (20 000 max), qbits, and threads (max 5 for free IBM account).
4. If you want to see the results in the table, check the box "Show results in the table" (Don't use this for a large number of values).

<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/Main2.png?raw=true" width="600px"/>
</p>

5. Use "File -> Save bit sequence" to save the result.
6. In the statistics menu, you can calculate frequencies, plot a distribution graph, as well as a bitmap.

<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/Main3.png?raw=true" width="600px"/>
</p>
<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/Main4.png?raw=true" width="600px"/>
</p>

7. If you need to form a numerical sequence of bits, use the "Generate numbers" button.

<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/Gen1.png?raw=true" width="300"/>
</p>
<p align="center">
  <img src="https://github.com/rialbat/IBMqRNG/blob/main/images/Gen2.png?raw=true" width="600px"/>
</p>

### ❗Warning
At the moment, statistics can be built only once, then there will be overlays

7. Use "Clear result" button to free up memory.

## TODO
-----------------

1. Add the ability to overwrite statistical tests' results.
2. Clear the code.

## Why are the values obtained randomly?
-----------------
Quantum Random-Number Generators (QRNG), unlike PseudoRandom Number Generators (PRNG), generate truly random numbers. There are several reasons for this. Firstly, quantum generators are hardware generators. All generation and measurement processes take place in digital-analogue space, as opposed to PRNG, which operates, as a rule, on the same processor architecture in the form of a machine language algorithm. Secondly, any generator with good statistical and cryptographic properties only works with entropy. Moreover, the difference lies in the fact that the entropy of the PRNG is, as a rule, the reading of external physical (natural) noises, for example, temperature, vibration, and the photoelectric effect, which can be restored according to the existing laws of physics with an understanding of the initial conditions, and the entropy of the QRNG is chaotic quantum processes that are almost impossible to measure.

## ![:octocat:](https://github.githubassets.com/images/icons/emoji/octocat.png ":octocat:")References
-----------------
1. PySide6 - https://wiki.qt.io/Qt_for_Python
2. IBMQ - https://quantum-computing.ibm.com/
3. Matplotlib - https://matplotlib.org/
4. Qiskit - https://qiskit.org/

## 📄 License
-----------------
**[MIT License](https://github.com/rialbat/IBMqRNG/blob/main/LICENSE)**

Copyright (c) 2022 **[rialbat](https://github.com/rialbat)**
