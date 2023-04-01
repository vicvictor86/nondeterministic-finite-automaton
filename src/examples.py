from NonDeterministAutomata import NFA

def example1():
    #  NFAE example that accepts words that contain a's that are followed by b's
    transition_functions = {
        ('q0', 'a'): {'q0'},
        ('q1', 'b'): {'q1'},
        ('q0', ''): {'q1'},
    }

    nfae = NFA(['a', 'b'], ['q0', 'q1', 'q2'], "q0", ["q1"])
    nfae.add_all_transitions(transition_functions)
    return nfae

def example2():
    # NFAE example that accepts words that start and end with the same symbol
    alphabet = ['0', '1']
    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']
    transition_functions = {
        ('q0', ''): ['q1', 'q4'],
        ('q0', '0'): ['q7'],
        ('q0', '1'): ['q7'],
        ('q1', '0'): ['q2'],
        ('q2', '0'): ['q2', 'q3'],
        ('q2', '1'): ['q2'],
        ('q3', ''): ['q7'],
        ('q4', '1'): ['q5'],
        ('q5', '0'): ['q5'],
        ('q5', '1'): ['q5', 'q6'],
        ('q6', ''): ['q7'],
        ('q7', '0'): ['q7'],
        ('q7', '1'): ['q7'],
    }
    initialState = 'q0'
    finalStates = ['q7']

    nfae = NFA(alphabet, states, initialState, finalStates)
    
    nfae.add_all_transitions(transition_functions)

    return nfae

def example3():
    # NFAE example
    transition_functions = {
        ('q0', 'a'): ['q0'],
        ('q0', ''): ['q1'],
        ('q1', 'b'): ['q1'],
        ('q1', ''): ['q2'],
        ('q2', 'a'): ['q2'],
    }

    nfae = NFA(['a', 'b'], ['q0', 'q1', 'q2'], "q0", ["q2"])
    nfae.add_all_transitions(transition_functions)
    return nfae

def example4():
    # NFA example for recognition, words that contain 110 as a substring
    transition_functions = {
        ('q0', '0'): ['q0'],
        ('q0', '1'): ['q0', 'q1'],
        ('q1', '1'): ['q2'],
        ('q2', '0'): ['q3'],
        ('q3', '0'): ['q3'],
        ('q3', '1'): ['q3'],
    }
    nfa = NFA(['0', '1'], ['q0', 'q1', 'q2', 'q3'], "q0", ["q3"])

    nfa.add_all_transitions(transition_functions)
    return nfa

def example5():
    # NFA example for recognition, words that starts with 0 and ends with 1
    states = ['q0', 'q1', 'q2']
    alphabet = ['0', '1']
    transitionFunctions = {
        ('q0', '0'): ['q1'],
        ('q1', '0'): ['q1'],
        ('q1', '1'): ['q1', 'q2'],
        ('q2', '1'): ['q2']
    }
    initialState = 'q0'
    finalStates = ['q2']

    nfa = NFA(alphabet, states, initialState, finalStates)
    nfa.add_all_transitions(transitionFunctions)
    print(nfa)
    print(nfa.get_transitions())
    return nfa