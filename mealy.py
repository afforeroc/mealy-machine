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

# GENERIC FUNCTIONS

# Read a generic input file and extract a data list
def readFileToList(inputFile):
    f = open(inputFile, "r")
    if f.mode == 'r':
        dataList = f.read().splitlines()
    f.close()
    return dataList

# Write a generic output file from a data list
def writeListToFile(dataList, outputFile):
    f = open(outputFile, "w")
    if f.mode == 'w':
        for line in dataList:
            f.write(line+'\n')
    f.close()

# Fill a simple generic dictionary
def fillSimpleDict(key, value, dict):
    if key not in dict:
        dict[key] = value
    return dict

# Fill a double generic dictionary
def fillDoubleDict(key1, key2, value, dict):
    if key1 not in dict:
        dict[key1] = {}
    (dict[key1])[key2] = value
    return dict

# SPECIAL FUNCTIONS

# Create a list of state transitions 
def createStateTransitions(sQ, machineData):
    stateTransitions = []
    for q in range(3, 3+sQ):
        statePair = machineData[q].strip().split(' ') # State-state pair
        stateTransitions.append(statePair)
    return stateTransitions

# Crete a dictionary with state-answers pairs
def createStateAnswerDict(sQ, machineData):
    stateAnswerDict = {} # Create a state-answer dictionary
    for q in range(3+sQ, 3+2*sQ):
        stateAnswerPair = machineData[q].strip().split(' ') # State-answer pair
        stateAnswerDict = fillSimpleDict(stateAnswerPair[0], stateAnswerPair[1], stateAnswerDict)
    return stateAnswerDict

# Create a automata using a initial state
def initializeMealyDigraph(q0):
    automata = Digraph(format = 'png')
    automata.attr(rankdir = 'LR')
    automata.attr(size = "8,5")
    automata.node('qdot', shape = 'point')
    automata.edge('qdot', q0)
    return automata

# Build and draw a transition like a graph
def createAutomata(alphabet, states, stateTransitions, stateAnswerDict, mealyDigraph):
    mealyDict = {}
    j = 0
    sr = ''
    for statePair in stateTransitions:
        for i in range(len(alphabet)):
            symbol = alphabet[i]
            state = statePair[i]
            qi = states[j]
            fillDoubleDict(qi, symbol, state, mealyDict)
            r = stateAnswerDict[state]
            sr = symbol + '/' + r
            mealyDigraph.edge(qi, state, label = sr)
        j += 1
    return mealyDict, mealyDigraph

# Give an answer for each indicated state
def translateString(q0, stateAnswerDict, mealyDict, iString):
    state = q0
    oString = ''
    for symbol in iString:
        newState = (mealyDict[state])[symbol]
        oString += stateAnswerDict[newState]
        state = newState
    return oString

def translateStringList(q0, stateAnswerDict, mealyDict, inputStrings):
    outputStrings = []
    for iString in inputStrings:
        oString = translateString(q0, stateAnswerDict, mealyDict, iString)
        outputStrings.append(oString)
    return outputStrings

# MAIN FUNCTION

# Mealy Machine creation
machineData = readFileToList("input/machine.txt") # Obtain all Mealy Machine data
alphabet = machineData[0].strip().split(' ') # Alphabet set
states = machineData[1].strip().split(' ') # State set
numStates = len(states) # Number of states 
q0 = machineData[2] # Initial state
stateTransitions = createStateTransitions(numStates, machineData) # Create transition state list
stateAnswerDict = createStateAnswerDict(numStates, machineData) # Create state-answer dictionary

# Mealy Machine Digraph
mealyDigraph = initializeMealyDigraph(q0) # Initialize a Mealy machine Digraph
mealyDict, mealyDigraph = createAutomata(alphabet, states, stateTransitions, stateAnswerDict, mealyDigraph)
mealyDigraph.render(filename='output/mealy_machine_digraph', cleanup=False, format='png', view = True) # Print a Mealy machine digraph

# Mealy Machine execution
inputStrings = readFileToList("input/input_strings.txt") # Obtain all strings to translate
outputStrings = translateStringList(q0, stateAnswerDict, mealyDict, inputStrings)
writeListToFile(outputStrings, "output/output_strings.txt")