# APP INFO
# Subject: Lenguajes de Programacion 2017-2
# Teacher: Joaquin Fernando Sanchez Cifuentes
# Mealy machine
# Andres Felipe Forero Correa, afforeroc@unal.edu.co
# Kevin Andres Castro Garcia, keacastroga@unal.edu.co
# This Python program execute and draw a Mealy Machine (Finite-state machine) using Python and Graphviz library.

# LIBRARIES
import platform, os
from graphviz import Digraph
from sys import stdin

# Check Operative System
os_name = platform.platform().lower()
if "windows" in os_name:
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#FUNCTIONS

# Initialize and draw an automata with a states list
def inicia_automata(Q, q0):
    automata = Digraph(format = 'png')
    automata.attr(rankdir = 'LR')
    automata.attr(size = "8,5")
    automata.node('qdot', shape = 'point')
    automata.edge('qdot', q0)
    return automata

# Create an answer dictionary
def crea_R(qi, r, R):
    if qi not in R:
        R[qi] = r
    return R

# Build and draw a transition like a graph
def transicion(E, Q, d_lista, R, automata):
    d = {}
    qi = 0
    sr = ''
    for linea in d_lista:
        for i in range(len(E)):
            simbolo = E[i]
            estado = linea[i]
            qi_str = Q[qi]
            if qi_str not in d:
                d[qi_str] = {}
            (d[qi_str])[simbolo] = estado
            r = R[estado]
            sr = simbolo + '/' + r
            automata.edge(qi_str, estado, label = sr)
        qi += 1
    return d, automata

# Give an answer for each indicated state
def respuesta(E, q0, d, cadena, R):
    r = ''
    estado = q0
    nuevo_estado = ''
    for simbolo in cadena:
        if simbolo in E:
            nuevo_estado = (d[estado])[simbolo]
            estado = nuevo_estado
            r += R[estado]
    return r

# MAIN FUNCTION
# Input data
E = stdin.readline().strip().split(' ') # Alphabet
Q = stdin.readline().strip().split(' ') # State set
q0 = stdin.readline().strip() # Initial state

# Graphic automata is created
automata = inicia_automata(Q, q0)

# Create a list with the transition function
d_lista = []
for _ in range(len(Q)):
    linea = stdin.readline().strip().split(' ')
    d_lista.append(linea)

# Create an answer dictionary
R = {}
for _ in range(len(Q)):
    linea = stdin.readline().strip().split(' ')
    R = crea_R(linea[0], linea[1], R)

# Add transitions states for the graphic automata
d, automata = transicion(E, Q, d_lista, R, automata)

# Print the graphic automata
automata.render('mm.gv', view = True)

# Ouput
K = int(stdin.readline()) # Number of sample strings
for _ in range(K):
    cadena = stdin.readline().strip('\n') # String that process a finite-state machine
    r = respuesta(E, q0, d, cadena, R) # Answer
    print(r) # Print the answer
