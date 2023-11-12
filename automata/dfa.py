from classes import State, FiniteAutomaton

def main():
    states = [State(name=f"q_{i+1}") for i in range(3)]
    states[1].accept = True

    sigma = ["0", "1"]

    delta = {
        (states[0], "0"): [states[0]],
        (states[0], "1"): [states[1]],
        (states[1], "0"): [states[2]],
        (states[1], "1"): [states[1]],
        (states[2], "0"): [states[1]],
        (states[2], "1"): [states[1]],
    }

    q_start = states[0]

    final_states = [state for state in states if state.isAccept()]
    # print(sigma)
    # print(final_states)

    dfa = FiniteAutomaton(states,sigma,delta,q_start,final_states)
    input_str = "1"
    print(dfa.compute(input_str))

if __name__ == '__main__':
    main()