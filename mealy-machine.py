# APP INFO
# Mealy Machine App
# This Python program execute and draw a Mealy Machine (Finite-state machine) using Python and Graphviz library.

# LIBRARIES
import platform, os
from graphviz import Digraph
from sys import stdin

# OS verification
os_name = platform.platform().lower()
if "windows" in os_name:
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#FUNCTIONS

# Read a generic input file and extract a data list
def readFileToList(inputFile):
    f = open(inputFile, "r")
    if f.mode == 'r':
        dataList = f.readlines()
    f.close()
    return dataList

# Create a automata using a initial state
def startAutomata(q0):
    automata = Digraph(format = 'png')
    automata.attr(rankdir = 'LR')
    automata.attr(size = "8,5")
    automata.node('qdot', shape = 'point')
    automata.edge('qdot', q0)
    return automata

# Create a list of state transitions 
def createStateTransitions(sQ, machineData):
    stateTransitions = []
    for q in range(3, 3+sQ):
        ssPair = machineData[q].strip().split(' ') # State-state pair
        stateTransitions.append(ssPair)
    return stateTransitions

# Fill a generic dict
def fillDict(key, value, D):
    if key not in D:
        D[key] = value
    return D

# Crete a dictionary with state-answers pairs
def createStateAnswerDict(sQ, machineData):
    stateAnswerDict = {} # Create a state-answer dictionary
    for q in range(3+sQ, 3+2*sQ):
        saPair = machineData[q].strip().split(' ') # pair state-answer
        stateAnswerDict = fillDict(saPair[0], saPair[1], stateAnswerDict)
    return stateAnswerDict

# Build and draw a transition like a graph
def mealyMachine(E, Q, stateTransitions, stateAnswerDict, automata):
    d = {}
    qi = 0
    sr = ''
    for ssPair in stateTransitions:
        for i in range(len(E)):
            symbol = E[i]
            state = ssPair[i]
            qi_str = Q[qi]
            print("qi_str = ", qi_str)
            if qi_str not in d:
                d[qi_str] = {}
            (d[qi_str])[symbol] = state
            print("d = ", d)
            r = stateAnswerDict[state]
            sr = symbol + '/' + r
            automata.edge(qi_str, state, label = sr)
        qi += 1
    print("qi_str = ", qi_str)
    print("d = ", d)
    return d, automata

# Give an answer for each indicated state
def traductor(E, q0, d, inputString, mealyMachine):
    q = q0
    qTemp = ''
    outputString = ''
    for s in inputString:
        if s in E:
            qTemp = (d[q])[s]
            outputString += mealyMachine[qTemp]
    return outputString

# MAIN FUNCTION
# Mealy Machine creation
machineData = readFileToList("input\machine.txt") # Obtain all Mealy Machine data
E = machineData[0].strip().split(' ') # Alphabet
Q = machineData[1].strip().split(' ') # State set
sQ = len(Q) # Number of states 
q0 = machineData[2] # Initial state
automata = startAutomata(q0) # Automata is created
stateTransitions = createStateTransitions(sQ, machineData) # Create transition state list
stateAnswerDict = createStateAnswerDict(sQ, machineData) # Create state-answer dictionary


d, automata = mealyMachine(E, Q, stateTransitions, stateAnswerDict, automata) # Fill automata
automata.render('mm.gv', view = True) # Print automata

# Mealy Machine execution
stringsData = readFileToList("input\strings.txt") # Obtain all strings to translate

'''

K = int(stdin.readline()) # Number of sample strings
translatedStrings = []
for _ in range(K):
    iString = stdin.readline().strip('\n') # Input string
    tString = respuesta(E, q0, d, iString, stateAnswer) # Translated string
    translatedStrings.append(tString)
'''

    
