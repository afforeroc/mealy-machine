# Mealy machine
Mealy Machine implementation using Python and Graphviz

## Configure a execution environment for app execution
1.1 Install stable/latest version of [Python 3](https://www.python.org/downloads/).

1.2 Verify Python installation.
```
py -3
```
> Stop Python console with <kbd>ctrl</kbd> + <kbd>Z</kbd>, <kbd>Enter</kbd>
```
pip3 --version
```

1.3.a Install Graphviz software on Windows
Download [here](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
> This app don't require enviroment path for Graphviz software

1.3.b Install and verify Graphviz software On Ubuntu.
```
sudo apt install graphviz
```
```
graphviz --version
```

1.4 Install and verify Graphviz library on Python 3.
```
pip3 install graphviz
```
```
pip3 show graphviz
```

## Run Mealy Machine app
Mealy machine is an interactive app that receives input data by commands (step by step). It is necessary input specific data in specific order because don't be there text that indicates when input the requested data.

For next input data forms it used this statement:
* Spanish(original): "Construir una máquina de Mealy con alfabeto de entrada {0,1} y alfabeto de salida {s,n} que produzca como salida ’s’ si los dos últimos dígitos de la cadena binaria son iguales y ’n’ si son diferentes"
* English(translated): "Construct a Mealy machine with input alphabet {0,1} and output alphabet {s, n} that produces as output ’s’ if the last two digits of the binary string are the same and ’n’ if they are different"

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

### 1. Input data step by step
Each step describes what information is required.
1. First step- Input all alphabet symbols ('E' elements separated by spaces in one line).
> e.g.
```
0 1
```

2. Second step- Input all states ('Q' elements separated by spaces in one line).
> e.g.
```
q0 q1 q2 q3 q4 q5 q6 q7 q8
```

3. Third step- Input initial state (one element in one line).
> e.g.
```
q0
```

4. Fourth step- Input all transitions states (state-state pairs). The states should inputted in order like we're inputted on step 2) (a pair separated by spaces in one line. 'Q' pairs separated by breaklines).
>e.g.
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

5. Fourth step- Input all state-answer pairs. The pairs should inputted in order like we're inputted on step 2) (a pair separated by spaces in one line. 'Q' pairs separated by breaklines).
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

6. Sixth- Input a number ('K') of sample strings (one element in one line).
>e.g.
```
14
```

7. Seventh- Input all sample strings (these strings don't have spaces. 'K' strings separated by breaklines)
>e.g.
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

### 2. Using data using an input file
The input file should has all 
```
python mealy-machine.py < input.in > ouput.out
```

## Output data
A set of lines with answers for each symbol that compose the lines.<br>
Lambda symbol is `^`.
> e.g.
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