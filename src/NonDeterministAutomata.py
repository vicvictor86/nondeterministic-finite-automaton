class NFA:
    def __init__(self, alphabet: list[str], states: list[str], initial_state: str, final_states: list[str]):
        self.alphabet = alphabet
        self.states = states
        self.transition_function = {}
        self.initial_state = initial_state
        self.final_states = final_states

    def add_all_transitions(self, transitions):
        for transition in transitions:
            self.add_transitions(transition[0], transition[1], transitions[transition])

    def add_transitions(self, current_state: str, symbol: str, next_state: list[str]):
        if self.transition_function.get(current_state) is None:
            self.transition_function[current_state] = {}
        if self.get_transition(current_state, symbol) is None:
            self.transition_function[current_state][symbol] = []
            self.transition_function[current_state][symbol] += next_state
        else:
            self.transition_function[current_state][symbol] += next_state

    def get_transitions(self):
        return self.transition_function
    
    def get_transition(self, state: str, symbol: str):
        try:
            return self.transition_function[state][symbol]
        except:
            return None

    def recognition(self, word: str):
        current_states = [self.initial_state]
        for symbol in word:
            next_states = []
            for state in current_states:
                current_transition = self.get_transition(state, symbol)
                if current_transition is not None:
                    next_states.extend(current_transition)
                    
            current_states = next_states

        for state in current_states:
            if state in self.final_states:
                return True
        return False
    
    def get_epsilon_closure(self, state: str):
        epsilon_closure = [state]
        if self.get_transition(state, "") is not None:
            for next_state in self.get_transition(state, ""):
                epsilon_closure.extend(self.get_epsilon_closure(next_state))
        return epsilon_closure
        
    
    def convertNFAEtoNFA(self):
        nfa = self
        epsilon_closure = {}
        for state in nfa.states:
            epsilon_closure[state] = nfa.get_epsilon_closure(state)

        for state in epsilon_closure:
            for symbol in nfa.alphabet:
                if len(epsilon_closure[state]) > 1:
                    for next_state in epsilon_closure[state]:
                        if next_state != state:
                            nfa.add_transitions(state, symbol, [next_state])

        final_states = []

        for final_state in nfa.final_states:
            if final_state in nfa.get_epsilon_closure(nfa.initial_state):
                final_states.append(nfa.initial_state)

        nfa.final_states += final_states

                    

        for state in nfa.states:
            if nfa.get_transition(state, "") is not None:
                nfa.transition_function[state].pop("")
        return nfa



    def __str__(self):
        return "States: " + str(self.states) + "  Alphabet: " + str(self.alphabet) + "  Initial State: " + str(self.initial_state) + "  Final States: " + str(self.final_states)
    
def from_txt(path: str):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    alphabet = lines[0].split()
    states = lines[1].split()
    initial_state = lines[2]
    final_states = lines[3].split()
    nfa = NFA(alphabet, states, initial_state, final_states)
    for i in range(4, len(lines)):
        line = lines[i].split()
        nfa.add_transitions(line[0], line[1], [line[2]])

    return nfa