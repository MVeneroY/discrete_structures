from typing import List, Dict

class State():

    def __init__(self, name: str="", accept: bool=False):
        self.name = name
        self.accept = accept

    def __str__(self) -> str:
        return f'{self.name}'
    
    def __repr__(self) -> str:
        return f'{self.name}'

    def isAccept(self) -> bool: 
        return self.accept

class FiniteAutomaton():

    curr_state = None

    def __init__(self, states: List[State], sigma: List[str], delta: Dict[tuple,State], q_0: State, q_a: List[State]):
        '''
        init function

        Parameters
        ----------
        states : [State]
            a list of the states included in the DFA
        sigma : [str]
            a list of the symbols included in the DFA's alphabet
        delta : { (State, str): State }
            a dictionary, where the key is a (q1, symbol) tuple and the value is q2
        q_0 : State
            the starting state
        q_a : [State]
            an array of accepting states

        Returns
        -------
        None

        Raises
        ------
        None
        '''
            
        self.states = states
        self.sigma = sigma
        self.delta = delta
        self.q_0 = q_0
        self.q_a = q_a
            

    def dfa_computation(self, input: str) -> bool:
        '''Attempt to compute string input. Return True if automaton reaches an accepting state'''
        self.curr_state = self.q_0

        # print(f'{self.curr_state.name}', end=" ")

        for symbol in input:
            if not self.dfa_transition(symbol):
                return False
            print(f'{self.curr_state.name}', end=" ")
            if self.curr_state.isAccept(): return True

        return True

    def dfa_transition(self, symbol: str) -> bool:
        '''
        Transition to another state in the DFA
        
        Parameters
        ----------
        symbol : str
            The symbol in the alphabet to transition on
            
        Returns
        -------
        bool
            whether the transition took place successfully
        
        Raises
        ------
        Exception
            if current state in DFA is None
        Exception
            if automaton is not a DFA
        '''
        if self.curr_state is None:
            raise Exception(f'Current state in automaton is None')
        if not self.isDeterministic():
            raise Exception(f'Automaton is not deterministic')

        for k in self.delta:
            if k[0] == self.curr_state and k[1] == symbol:
                self.curr_state = self.delta[k][0]
                return True
            
        return False
    
    # TODO: implement token based computation
    # https://dl.acm.org/doi/10.1145/1103845.1094839
    def nfa_computation(self, input: str) -> bool:
        '''
        Pseudocode:

        mark q_0
        over every symbol in the input string:
            over every transition possible by the marked states on symbol:
                mark the states we transition into
                if this is was the last symbol in the string:
                    if either of those states is accepting: 
                        return True
            unmark the states we transitioned from
            If no transitions took place, return False

        return False
        '''
        tokens = {s: False for s in self.states}

        tokens[self.q_0] = True
        strlen = len(input)
        symbol_count = 0

        for symbol in input:
            q_next_list = []
            q_from_list = []
            for (q_curr,_symbol),q_next in self.delta.items():
                if tokens[q_curr] and symbol == _symbol:
                    q_next_list.extend([q for q in q_next if q not in q_next_list])
                    q_from_list.append(q_curr)
            # print(f'transitions on symbol {symbol} would occur from: {q_from_list}')
            # print(f'possible transitions: {q_next_list}')

            for q_from in q_from_list: tokens[q_from] = False
            for q_next in q_next_list: tokens[q_next] = True

            symbol_count += 1

            for state, marked in tokens.items():
                if state.isAccept() and marked and symbol_count == strlen: 
                    return True
                # if accept state was reached before the last symbol is consumed
                if state.isAccept() and marked:
                    tokens[state] = False

        return False

    # def nfa_transition(self, state: State, symbol: str):
    #     next_list = []
    #     for (q_1,s),q_next_list in self.delta.items():
    #         if s != symbol or q_1 != state: continue
    #         for q_next in q_next_list: next_list.append(q_next)

    #     print(f'possible transitions on symbol {symbol}: {next_list}')
    #     return next_list

    def isDeterministic(self):
        '''Return whether automaton is deterministic or not'''
        for v in self.delta.values():
            if len(v) > 1:
                return False
        
        return True
    
    def useless_states(self) -> (List[State], List[State]):
        marked_dict = {s:False for s in self.states}
        queue = []

        queue.append(self.q_0)
        # marked_dict[self.q_0] = True

        while queue:
            root = queue.pop(0)
            # print(f'checking state {root}')
            # print(f'{root}', 'accepts' if root.isAccept() else 'does not accept')

            transitions = []
            for d in self.delta:
                if d[0] != root.name: continue
                # print('transitions', end=' ')
                for transition in self.delta[d]:
                    # print(transition, end=' ')
                    transitions.append(transition)
                # print()

            for leaf in [s for s in self.states if s.name in transitions]:
                if not marked_dict[leaf]:
                    queue.append(leaf)
                    marked_dict[leaf] = True

        # print(marked_dict)
        # print(self.q_a)
        useless = []
        useless_a = []
        for s in self.states:
            if not marked_dict[s] and s != self.q_0:
                useless.append(s)
                if s.isAccept(): useless_a.append(s)
        return useless, useless_a
    
    def NFA_to_DFA(self):
        if self.isDeterministic():
            raise Exception('Finite automaton is already deterministic')
        
