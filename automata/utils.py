from .classes import State, FiniteAutomaton
from xml.etree import ElementTree as ET
# from csv import DictReader
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


def read_automaton(file_name="dfa.xml", input_dir=".") -> FiniteAutomaton:
    '''
    Read a finite automaton from an XML file

    Parameters
    ----------
    file_name : str
        file name, including file extension
    input_dir : str
        file directory relative to environment

    Returns
    -------
    FiniteAutomaton

    Raises
    ------
    Exception
        when the xml file doesn't follow the automaton format
    '''
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
                if s.attrib['name'] in [s.name for s in states]:
                    raise Exception(f'State with name {s.attrib["name"]} already exists in {states}')
                state = State(s.attrib['name'], s.attrib['accepting']=='true')
                if state.isAccept(): accept.append(state)
                states.append(state)
        
        if child.tag == 'q_start':
            if child.attrib['name'] not in [s.name for s in states]: 
                raise Exception(f'Start state {child.attrib["name"]} not among the states provided in {states}')
            for s in states:
                if s.name == child.attrib['name'] and q_0 is None: q_0 = s
                elif s.name == child.attrib['name']: 
                    raise Exception(f'Deterministic finite automata can have only one start state. (Other is {q_0})')

        if child.tag == 'alphabet':
            for symbol in child:
                if symbol.attrib['name'] in [s for s in alphabet]: 
                    raise Exception(f'Symbol {symbol.attrib["name"]} already defined in alphabet {alphabet}')
                alphabet.append(symbol.attrib['name'])

        if child.tag == 'transitions':
            for d in child:
                q1 = None
                q2 = None
                for s in states:
                    if s.name == d.attrib['q1']: q1 = s
                    if s.name == d.attrib['q2']: q2 = s
                if (q1,d.attrib['symbol']) in delta.keys():
                    delta[(q1,d.attrib['symbol'])].append(q2)
                else:
                    delta[(q1,d.attrib['symbol'])] = [q2]

    return FiniteAutomaton(states, alphabet, delta, q_0, accept)