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
    dfa1 = read_dfa("useless.xml", input_dir="data")
    print(f'Useless accept states?\t{dfa1.is_useless()}')

    dfa2 = read_dfa("dfa.xml", input_dir="data")
    print(f'Useless accept states?\t{dfa2.is_useless()}')

def main():
    read_xml_test()
    useless_test()

if __name__ == '__main__':
    main()