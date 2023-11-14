# from classes import State, FiniteAutomaton
from utils import read_dfa

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

def main():
    read_xml_test()
    useless_test()

if __name__ == '__main__':
    main()