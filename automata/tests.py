from classes import State, FiniteAutomaton, E_STRING
from utils import read_automaton
import re
import random

def read_xml_test():
    try:
        _ = read_automaton("error1.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)

    try: 
        _ = read_automaton("error2.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)

    try: 
        _ = read_automaton("error3.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)

    try: 
        _ = read_automaton("error4.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)


def useless_test():
    dfa = read_automaton("useless.xml", input_dir="data")
    useless, useless_a = dfa.useless_states()
    print(f'Useless states:\t\t{useless}')
    print(f'Useless accept states:\t{useless_a}')

    dfa = read_automaton("dfa.xml", input_dir="data")
    useless, useless_a = dfa.useless_states()
    print(f'Useless states:\t\t{useless}')
    print(f'Useless accept states:\t{useless_a}')


def nfa_test():
    nfa = read_automaton('nfa2.xml', 'data')
    print(f'nfa is deterministic:\t{nfa.isDeterministic()}')

    mismatches = []
    for _ in range(100_000):
        s = ''.join(random.choices(['0','1'], k=random.randint(1,50)))
        
        nfa_result = nfa.nfa_computation(s)
        rgx_result = re.fullmatch(r'[0|1]*1[0|1]{3}', s) is not None
        if nfa_result != rgx_result:
            mismatches.append(s)
    if len(mismatches) > 0:
        for m in mismatches: print(f'mistatch:\t{m}')
    else:
        print('All tests successful')
    

def main():
    # read_xml_test()
    # useless_test()
    nfa_test()


if __name__ == '__main__':
    main()