import re
import random
import unittest
import sys
import os

sys.path.append(os.path.join('..', os.getcwd()))
from automata.classes import *
from automata.utils import *

class TestAutomata(unittest.TestCase):

    def test_read_xml(self):
        '''
        Test automata input in xml format
        '''

        automaton = read_automaton('dfa.xml', input_dir='data')
        self.assertIsInstance(automaton, FiniteAutomaton)

    def test_read_xml_exceptions(self):
        '''
        Test exceptions when reading atomata
        '''

        self.assertRaisesRegex(Exception, 
                               r'^State with name .* already exists in .*', 
                               read_automaton, 
                               'error1.xml', 
                               'data')
        self.assertRaisesRegex(Exception, 
                               r'^Start state .* not among the states provided in .*', 
                               read_automaton, 
                               'error2.xml', 
                               'data')
        self.assertRaisesRegex(Exception, 
                               r'^Deterministic finite automata can have only one start state. \(Other is .*\)', 
                               read_automaton, 
                               'error3.xml', 
                               'data')
        self.assertRaisesRegex(Exception, 
                               r'^Symbol .* already defined in alphabet .*', 
                               read_automaton, 
                               'error4.xml', 
                               'data')

    def test_useless_states(self):
        '''
        Test whether an automaton has useless states
        '''

        dfa = read_automaton('useless.xml', input_dir='data')
        useless, useless_a = dfa.useless_states()
        self.assertEqual([s.name for s in useless], ['q_3', 'q_5'])
        self.assertEqual([s.name for s in useless_a], ['q_3'])

        dfa = read_automaton('dfa.xml', input_dir='data')
        useless, useless_a = dfa.useless_states()
        self.assertEqual([s.name for s in useless], [])
        self.assertEqual([s.name for s in useless_a], [])

    def test_automaton_is_deterministic(self):
        '''
        Test whether an automaton is an NFA or a DFA
        '''
        
        nfa = read_automaton('nfa2.xml', 'data')
        self.assertFalse(nfa.isDeterministic())

    def test_nfa_computation(self):
        '''
        Test an NFA's computation of a string
        '''

        nfa = read_automaton('nfa2.xml', 'data')
        for _ in range(1_000):
            s = ''.join(random.choices(['0','1'], k=random.randint(1,50)))

            nfa_result = nfa.nfa_computation(s)
            rgx_result = re.fullmatch(r'[0|1]*1[0|1]{3}', s) is not None

            self.assertEqual(nfa_result, rgx_result)  


if __name__ == '__main__':
    unittest.main()