class DeterministicFiniteAutomata(object):
    """ 決定性有限オートマトン """
    def __init__(self, states, alphabets, transitions, init_state, final_states):
        self.states = states
        self.alphabets = alphabets
        self.transitions = transitions
        self.init_state = init_state
        self.final_states = final_states
    def run(self, string):
        """ stringを認識するかチェックする """
        state = self.init_state
        for char in string:
            if char not in self.alphabets:
                print("ERROR : invalid character \"%s\"" % char)
                return -1
            else:
                state = self.transitions[state][char] # 状態を遷移させる
        return state in self.final_states

# from dfa import DeterministicFiniteAutomata as DFA
transitions = {
    a: {"0": a, "1": b},
    b: {"0": c, "1": a},
    c: {"0": b, "1": c},
}
