#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# LIBRARIES
import platform, os
from sys import stdin
try:
    from graphviz import Digraph
except:
  print("'graphviz' library is not installed, please use command: 'pip3 install graphviz'")
  exit()

# operative system verification
os_name = platform.platform().lower()
if "windows" in os_name:
    try:
        if os.path.exists('C:/Program Files (x86)/Graphviz2.38/bin/'): # Graphviz software verification
            os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    except:
        print("Graphviz software is not installed or their path dont exist")
        exit()

# GENERIC FUNCTIONS
# Read a generic input file and extract a data list
def readFileToList(inputFile):
    try:
        f = open(inputFile, "r")
    except:
        print(f'Cant open "{inputFile}" file')
        exit()
    if f.mode == 'r':
        dataList = f.read().splitlines()
    f.close()
    return dataList

# Write a generic output file from a data list
def writeListToFile(dataList, outputFile):
    try:
        f = open(outputFile, "w")
    except:
        print(f'Cant open "{outputFile}" file')
        exit()
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

# MEALY MACHINE CREATE FUNCTIONS

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

def createMealyDict(alphabet, states, stateTransitions):
    mealyDict = {}
    j = 0
    for statePair in stateTransitions:
        for i in range(len(alphabet)):
            state = states[j]
            symbol = alphabet[i]
            newState = statePair[i]
            fillDoubleDict(state, symbol, newState, mealyDict)
        j += 1
    return mealyDict

# MEALY MACHINE DIGRAPH FUNCTIONS
def initializeMealyDigraph(q0):
    mealyDigraph = Digraph(format = 'png')
    mealyDigraph.attr(rankdir = 'LR')
    mealyDigraph.attr(size = "10")
    mealyDigraph.node('qdot', shape = 'point')
    mealyDigraph.edge('qdot', q0)
    return mealyDigraph

def createMealyDigraph(alphabet, mealyDict, stateAnswerDict, mealyDigraph):
    for state in mealyDict:
        answer = stateAnswerDict[state]
        for symbol in alphabet:
            newState = (mealyDict[state])[symbol]
            symbolAnswer = symbol + '/' + answer
            mealyDigraph.edge(state, newState, label = symbolAnswer)
    return mealyDigraph

# TRANSLATE FUNCTIONS
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
if __name__ == '__main__':
    # Mealy machine creation
    machineData = readFileToList("input/machine.txt") # Obtain all Mealy Machine data
    alphabet = machineData[0].strip().split(' ') # Alphabet set
    states = machineData[1].strip().split(' ') # State set
    numStates = len(states) # Number of states 
    q0 = machineData[2] # Initial state
    stateTransitions = createStateTransitions(numStates, machineData) # Create a transition state list
    stateAnswerDict = createStateAnswerDict(numStates, machineData) # Create a state-answer dictionary
    mealyDict = createMealyDict(alphabet, states, stateTransitions) # Create a Mealy machine dictionary

    # Mealy machine digraph
    mealyDigraph = initializeMealyDigraph(q0) # Initialize a Mealy machine Digraph
    mealyDigraph = createMealyDigraph(alphabet, mealyDict, stateAnswerDict, mealyDigraph) # create a Mealy machine Digraph
    mealyDigraph.render(filename='output/mealy_machine_digraph', cleanup=False, format='png', view = True) # Print a Mealy machine digraph

    # Mealy machine execution
    inputStrings = readFileToList("input/input_strings.txt") # Obtain all strings to translate
    outputStrings = translateStringList(q0, stateAnswerDict, mealyDict, inputStrings) # Translate all input strings
    writeListToFile(outputStrings, "output/output_strings.txt") # Write all translated strings on a file