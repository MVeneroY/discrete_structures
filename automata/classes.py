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

    def __init__(self, states: List[State], sigma: List[str], delta: Dict[tuple,str], q_0: State, q_a: List[State]):
        '''
        init function

        Parameters
        ----------
        states : [State]
            a list of the states included in the DFA
        sigma : [str]
            a list of the symbols included in the DFA's alphabet
        delta : { (str, str): str }
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
            

    def compute(self, input: str) -> bool:
        '''Attempt to compute string input. Return True if automaton reaches an accepting state'''
        self.curr_state = self.q_0

        # print(f'{self.curr_state.name}', end=" ")

        for symbol in input:
            if not self.transition(symbol):
                return False
            print(f'{self.curr_state.name}', end=" ")
            if self.curr_state.isAccept(): return True

        return True

    def transition(self, symbol: str) -> bool:
        '''Transition to another state. Return True if a legal transition took place'''
        if self.curr_state is None: return
        if not self.isDeterministic(): return

        for k in self.delta:
            if k[0] == self.curr_state and k[1] == symbol:
                self.curr_state = self.delta[k][0]
                return True
            
        return False

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
                if s in self.q_a: useless_a.append(s)
        return useless, useless_a