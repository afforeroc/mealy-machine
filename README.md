# Mealy machine app
This is an app about that recreates a functional Mealy machine. It was written using Python3 language and Graphviz software.<br>
Additional, it contains a configuration manual for use.

Functionalities:
* It build a functional Mealy machine.
* It draw and show a directed graph that represents the machine.
* It translate strings.

## Configuration manual
This manual was designed to be done on a personal computer.<br> 
Some steps/sections require using of console commands and text editing that will indicated with `Terminal` and `Text` labels.

### Required software
* Command prompt like Terminal(Linux) or PowerShell(Windows).
* Text editor like Notepad++, Visual Studio Code, etc.

### 1. Configure environment for app execution
1.1 Install stable/latest version of [Python3](https://www.python.org/downloads/).

1.2 Verify Python installation.
> Terminal
```
py -3
```
```
pip3 --version
```
> **Note** stop Python3 console with <kbd>ctrl</kbd> + <kbd>Z</kbd>, <kbd>Enter</kbd>

1.3.a Install Graphviz software on **Windows**.<br>
Download [here](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
> It's not necessary verify installation/path for this software.

1.3.b Install and verify Graphviz software on **Ubuntu**.
> Terminal
```
sudo apt install graphviz
```
```
graphviz --version
```

1.4 Install and verify Graphviz library on Python 3.
> Terminal
```
pip3 install graphviz
```
```
pip3 show graphviz
```

### 2. Configure and run Mealy Machine app
With purpose of explaining app execution it used this following statement.
> e.g.
* English (traduced): *" A Mealy machine with input alphabet {0,1} and output alphabet {s, n} that produces as output 's' if last two digits of a string are same and 'n' if they are different"*
* Spansh(original): *"Un máquina de Mealy con alfabeto de entrada {0,1} y alfabeto de salida {s,n} que produzca como salida 's' si los dos últimos dígitos de una cadena son iguales y 'n' si son diferentes"*

Based on the above statement, a Mealy machine was built obtained a transition state table and a state-answer table.

* Table 1- transition state table

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

* Table 2- state-answer table<br>
> Note: Lambda symbol used here is `^`.

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
The app requires an input file with all data (1 to 5 section) to construct a functional Mealy Machine and their representative directed graph, and some sample strings (6 and 7 section) to generate their respective traduced strings. The followings sections explain required order and type of data for this file. All showed data is in 'input.in' file.
* Section 1- All alphabet symbols ('E' elements separated by spaces in one line).
> Text (e.g.)
```
0 1
```

* Section 2- All states ('Q' elements separated by spaces in one line).
> Text (e.g.)
```
q0 q1 q2 q3 q4 q5 q6 q7 q8
```

* Section 3- Initial state (one element in one line).
> Text (e.g.)
```
q0
```

* Section 4- All transitions states (state-state pairs). The states should be inputted in order like Table 1 (a pair separated by spaces in one line. 'Q' pairs separated by breaklines).
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

* Section 5- All state-answer pairs. Each state with their answer (a pair separated by spaces in one line. 'Q' pairs separated by breaklines).
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

* Section 6- A number ('K') of sample strings that they will be translated (one element in one line).
> Text (e.g.)
```
14
```

* Section 7- All sample strings (these strings don't have spaces. 'K' strings separated by breaklines)
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

### 4. Run the app
After entering all mentioned data like in the previous sections.
Now you can run the app using a command prompt taking the input file to generate a output file.<br>
> Terminal
```
python mealy-machine.py < input.in > ouput.out
```

### 5. Output data
After running the app, it will output a 'output.out' file and 'mm.gv.png' image.

* `output.out`- A set of lines with translated strings.
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

* `mm.gv.png`- directed graph representation of Mealy machine.
> Image (e.g.)

![Mealy machine graph](https://raw.githubusercontent.com/afforeroc/mealy-machine/master/mm.gv.png)