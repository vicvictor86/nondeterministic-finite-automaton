from NonDeterministAutomata import NFA

# nfa = NFA(["a", "b"], ["qo", "q1", "q2", "qf"], "q0", ["qf"])

# nfa.addTransitions("q0", "a", ["q0", "q1"])
# nfa.addTransitions("q0", "b", ["q0", "q2"])
# nfa.addTransitions("q1", "a", ["qf"])
# nfa.addTransitions("q2", "b", ["qf"])
# nfa.addTransitions("qf", "a", ["qf"])
# nfa.addTransitions("qf", "b", ["qf"])

nfa = NFA(['0', '1'], ['q1', 'q2', 'q3', 'q4', 'q5', 'q6'], "q1", ["q4"])

transition_functions = {
    ('q1', '0'): {'q1'},
    ('q1', '1'): {'q1', 'q2'},
    ('q2', '1'): {'q3'},
    ('q3', '0'): {'q4'},
    ('q4', '0'): {'q4'},
    ('q4', '1'): {'q4'},
}

nfa.add_all_transitions(transition_functions)

print(nfa.get_transitions())

print(nfa.recognition("100100"))
