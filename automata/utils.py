from classes import State, FiniteAutomaton
from xml.etree import ElementTree as ET
from csv import DictReader
import os

# def read_automaton(file_name="dfa.csv", input_dir="."):
#     states = []
#     Sigma = []
#     delta = {}
#     q_start = None
#     final_states = []

#     path = os.path.join(input_dir, file_name)
#     # print(path)
#     with open(path, "r") as f:
#         d_reader = DictReader(f)
#         for d in list(d_reader):
#             q1 = d['q1'].strip()
#             _sigma = d['sigma'].strip()
#             q2 = d['q1'].strip()

#             if q1 not in [q.name for q in states]:
#                 states.append(State(name=q1, accept=states==[]))
#             if q2 not in [q.name for q in states]:
#                 states.append(State(name=q2, accept=states==[]))

#             if _sigma not in Sigma:
#                 Sigma.append(_sigma)


def read_dfa(file_name="dfa.xml", input_dir="."):
    states = []
    q_0 = None
    accept = []
    alphabet = []
    delta = {}

    tree = ET.parse(os.path.join(input_dir,file_name))
    root = tree.getroot()

    for child in root:
        if child.tag == 'states':
            for s in child:
                if s.attrib['name'] in [s.name for s in states]: return
                state = State(s.attrib['name'], s.attrib['accepting']=='true')
                if state == []: q_0 = state
                if state.isAccept(): accept.append(state)
                states.append(state)
                
        
        if child.tag == 'q_start':
            if child.attrib['name'] not in [s.name for s in states]: return # raise an error?
            for s in states:
                if s.name == child.attrib['name']: s.accept = True

        if child.tag == 'alphabet':
            for symbol in child:
                if symbol.attrib['name'] in [s for s in alphabet]: return
                alphabet.append(symbol.attrib['name'])

        if child.tag =='transitions':
            for d in child:
                if (d.attrib['q1'],d.attrib['symbol']) in delta.keys():
                    delta[(d.attrib['q1'],d.attrib['symbol'])].append(d.attrib['q2'])
                else:
                    delta[(d.attrib['q1'],d.attrib['symbol'])] = [d.attrib['q2']]

    return FiniteAutomaton(states, alphabet, delta, q_0, accept)
