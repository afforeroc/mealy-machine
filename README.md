# Mealy machine app
A functional Mealy machine that draw own digraph and translate example strings.<br>
It was written using Python3 language and Graphviz software/library.<br>
Additional, it contains a configuration and use manual.

## Manual
This manual was designed to be done on a personal computer.<br> 
Some steps/sections require using of command-line interpreter, text edition, etc. These are indicated with `Terminal`, `Text`, `Image` labels.

### Recommended software
* Command-line interpreter like Terminal, PowerShell, etc.
* Text editor like Notepad++, Visual Studio Code, etc.

### 1. App environment configuration
1.1 Install stable/latest version of [Python3](https://www.python.org/downloads/).

1.2 Verify Python installation.
> Command-line
```
py -3 --version
```
```
pip3 --version
```

1.3.a Install Graphviz software on **Windows**.<br>
Download [here](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
> It's not necessary verify installation/path for this software.

1.3.b Install and verify Graphviz software on **Ubuntu**.
> Command-line
```
sudo apt install graphviz
```
```
graphviz --version
```

1.4 Install and verify Graphviz library for Python3.
> Command-line
```
pip3 install graphviz
```
```
pip3 show graphviz
```

### 2. A Mealy machine example
With purpose of explaining app execution, I used this following statement that describes a Mealy machine example.
> e.g.
* **English (translated)**- *" A Mealy machine with input alphabet {0,1} and output alphabet {s, n} that produces as output 's' if last two digits of a string are same and 'n' if they are different"*
* **Spansh (original)**- *"Un máquina de Mealy con alfabeto de entrada {0,1} y alfabeto de salida {s,n} que produzca como salida 's' si los dos últimos dígitos de una cadena son iguales y 'n' si son diferentes"*

Based on the above statement I built a Mealy machine with this following transition state and state-answer tables.

* **Table 1**- Transition state table
> e.g.

| State | Input<br> 0 1 |
|:-----:|:-----:|
| q0    | q1 q5 |
| q1    | q2 q3 |
| q2    | q2 q3 |
| q3    | q4 q7 |
| q4    | q2 q3 |
| q5    | q6 q7 |
| q6    | q2 q8 |
| q7    | q6 q7 |
| q8    | q6 q7 |

* **Table 2**- State-answer table<br>
> e.g.<br>
> Lambda symbol: `^`.

| State | Answer |
|:-----:|:------:|
| q0    | ^      |
| q1    | ^      |
| q2    | s      |
| q3    | n      |
| q4    | n      |
| q5    | ^      |
| q6    | n      |
| q7    | s      |
| q8    | n      |

### 3. Input data
The app requires:
* `machine.txt`- input file with all data to construct a representative Mealy machine and their digraph.
* `input_strings.txt`- input file with set of strings that will be translated. 

These input files are in `input/` folder and must be edited according to your needs.
Followings sections I explain required order of data for these files with examples.

**machine.txt**

* First section- All alphabet symbols ('E' elements separated by spaces in one line).
> Text (e.g.)
```
0 1
```

* Second section- All states ('Q' elements separated by spaces in one line).
> Text
```
q0 q1 q2 q3 q4 q5 q6 q7 q8
```

* Third section- Initial state (only one element in one line).
> Text (e.g.)
```
q0
```

* Fourth section- All transitions states (state-state pairs). These states should be inputted according with order like states were inputted, as Table 1 (a pair separated by spaces in one line. 'Q' pairs separated by breaklines).
> Text (e.g.)
```
q1 q5
q2 q3
q2 q3
q4 q7
q2 q3
q6 q7
q2 q8
q6 q7
q6 q7
```

* Fifth section- All state-answer pairs. Each state with their answer. These state-answers should be inputted according with order like states were inputted, as Table 2 (a pair separated by spaces in one line. 'Q' pairs separated by breaklines).
> Text (e.g.)
```
q0 ^
q1 ^
q2 s
q3 n
q4 n
q5 ^
q6 n
q7 s
q8 n
```
**input_strings.txt**
* All input strings that will be translated (these strings lines don't have spaces and are separated by breaklines)
> Text (e.g.)
```
0
1
00
01
10
11
000
001
010
011
100
101
110
111
```

You can check looking inside of these input files.

### 4. App running
After entering/editing all mentioned data in these files, now you can run the app using a command-line interpreter.
> Command-line
```
python3 mealy.py
```

### 5. Output data
After app execution, these followings output files will be in `output/` folder.

* `output_strings.txt`- translated strings set.
> Text (e.g.)
```
^
^
^s
^n
^n
^s
^ss
^sn
^nn
^ns
^ns
^nn
^sn
^ss
```

* `mealy_machine_digraph.png`- a Mealy machine digraph.
> Image (e.g.)

![Mealy machine graph](https://raw.githubusercontent.com/afforeroc/mealy-machine/master/output/mealy_machine_digraph.png)