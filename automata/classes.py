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

    def __init__(self, states: List[State], sigma: List[str], delta, q_0: State, q_a: List[State]):
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