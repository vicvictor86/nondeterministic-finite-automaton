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
            self.transition_function[current_state][symbol] = next_state
        else:
            self.transition_function[current_state][symbol] = next_state

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

    def __str__(self):
        return "States: " + str(self.states) + "  Alphabet: " + str(self.alphabet) + "  Initial State: " + str(self.initial_state) + "  Final States: " + str(self.final_states)
    