from classes import State, FiniteAutomaton
from utils import read_dfa

def useless_test():
    dfa1 = read_dfa("useless.xml", input_dir="data")
    print(f'Useless accept states?\t{dfa1.is_useless()}')

    dfa2 = read_dfa("dfa.xml", input_dir="data")
    print(f'Useless accept states?\t{dfa2.is_useless()}')

def main():
    useless_test()

if __name__ == '__main__':
    main()