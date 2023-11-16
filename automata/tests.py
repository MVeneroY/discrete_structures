# from classes import State, FiniteAutomaton
from utils import read_dfa
import re
import random

def read_xml_test():
    try:
        _ = read_dfa("error1.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)

    try: 
        _ = read_dfa("error2.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)

    try: 
        _ = read_dfa("error3.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)

    try: 
        _ = read_dfa("error4.xml", input_dir="data")
    except Exception as e:
        print(f'Error:', e)


def useless_test():
    dfa = read_dfa("useless.xml", input_dir="data")
    useless, useless_a = dfa.useless_states()
    print(f'Useless states:\t\t{useless}')
    print(f'Useless accept states:\t{useless_a}')

    dfa = read_dfa("dfa.xml", input_dir="data")
    useless, useless_a = dfa.useless_states()
    print(f'Useless states:\t\t{useless}')
    print(f'Useless accept states:\t{useless_a}')


def nfa_test():
    nfa = read_dfa('nfa2.xml', 'data')
    print(f'nfa is deterministic:\t{nfa.isDeterministic()}')

    mismatches = []
    for _ in range(100_000):
        s = ''.join(random.choices(['0','1'], k=random.randint(1,50)))
        
        nfa_result = nfa.nfa_computation(s)
        rgx_result = re.fullmatch(r'[0|1]*1[0|1][0|1][0|1]', s) is not None
        if nfa_result != rgx_result:
            mismatches.append(s)
    if len(mismatches) > 0:
        print('mismatches')
        print(len(mismatches))
        for m in mismatches: print(m)
    else:
        print('All tests successful')
    

def regex_test():
    s = '1110101'
    print(re.fullmatch(r'[0|1]*1[0|1][0|1][0|1]', s))
    s = '1010101010'
    print(re.fullmatch(r'[0|1]*1[0|1][0|1][0|1]', s).group() == s)


def main():
    # read_xml_test()
    # useless_test()
    nfa_test()
    # regex_test()


if __name__ == '__main__':
    main()