# Mealy machine app
This app recreates a functional Mealy machine. It was written using Python3 language and Graphviz software.<br>
Additional, it contains a configuration and use manual.

Functionalities:
* It builds a functional Mealy machine.
* It draws and shows a directed graph that represents the machine.
* It translates strings.

## Manual
This manual was designed to be done on a personal computer.<br> 
Some steps/sections require using of command-line interpreter, text edition, etc. These are indicated with `Terminal`, `Text`, `Image` labels.

### Minimum required software
* Command-line interpreter like Terminal, PowerShell, etc.
* Text editor like Notepad++, Visual Studio Code, etc.

### 1. App environment configuration
1.1 Install stable/latest version of [Python3](https://www.python.org/downloads/).

1.2 Verify Python installation.
> Command-line
```
py -3
```
```
pip3 --version
```
> **Note** stop Python3 console with <kbd>ctrl</kbd> + <kbd>Z</kbd>, <kbd>Enter</kbd>

1.3.a Install Graphviz software on **Windows**.<br>
Download [here](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
> **Note**: It's not necessary verify installation/path for this software.

1.3.b Install and verify Graphviz software on **Ubuntu**.
> Command-line
```
sudo apt install graphviz
```
```
graphviz --version
```

1.4 Install and verify Graphviz library on Python3.
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
* English (translated): *" A Mealy machine with input alphabet {0,1} and output alphabet {s, n} that produces as output 's' if last two digits of a string are same and 'n' if they are different"*
* Spansh (original): *"Un máquina de Mealy con alfabeto de entrada {0,1} y alfabeto de salida {s,n} que produzca como salida 's' si los dos últimos dígitos de una cadena son iguales y 'n' si son diferentes"*

Based on the above statement I built a Mealy machine with this following transition state and state-answer tables.

* **Table 1**- Transition state table

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
The app requires an input file with all data (1 to 5 section) to construct a functional Mealy machine and their representative directed graph, and some sample strings (6 and 7 section) to generate their respective traduced strings. Followings sections explain required order and type of data for this file. All showed data is in 'input.in' file. If you need your customized Mealy machine you need edit `ìnput.in` with all respective data. 

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

The previous sections can sumarized in content of `input.in` file.
> Text (e.g.)
```
0 1
q0 q1 q2 q3 q4 q5 q6 q7 q8
q0
q1 q5
q2 q3
q2 q3
q4 q7
q2 q3
q6 q7
q2 q8
q6 q7
q6 q7
q0 ^
q1 ^
q2 s
q3 n
q4 n
q5 ^
q6 n
q7 s
q8 n
14
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
After entering all data as mentioned in "input data" section, now you can run the app using a command prompt taking the input file to generate a output file that will contains translated strings, aditional it will generated a image with graph of Mealy Machine.
> Terminal
```
python3 mealy-machine.py < input.in > ouput.out
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