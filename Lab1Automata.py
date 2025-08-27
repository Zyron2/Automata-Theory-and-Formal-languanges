class Automata:
    def __init__(self, states, alphabet, transition, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, string):
        # Check if all symbols are in the alphabet
        if not all(symbol in self.alphabet for symbol in string):
            return False
        state = self.start_state
        for symbol in string:
            if (state, symbol) not in self.transition:
                return False
            state = self.transition[(state, symbol)]
        return state in self.accept_states


# Number 1
dfa1 = Automata(
    states={'a', 'b', 'c'},
    alphabet={'0', '1'},
    transition={
        ('a', '0'): 'a',
        ('a', '1'): 'b',
        ('b', '0'): 'c',
        ('b', '1'): 'a',
        ('c', '0'): 'b',
        ('c', '1'): 'c'
    },
    start_state='a',
    accept_states={'c'}
)

# Number 2.
dfa2 = Automata(
    states={'q0', 'q1', 'q2', 'q3'},
    alphabet={'a', 'b'},
    transition={
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q2',
        ('q1', 'a'): 'q0',
        ('q1', 'b'): 'q3',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q0', 
        ('q3', 'a'): 'q2',
        ('q3', 'b'): 'q1'
    },
    start_state='q0',
    accept_states={'q3','q0'}  # Accepts if ends in q0 or q3
)

# Number 1. 3 accepted and rejected
print("=== Automaton 1 (0 and 1) ===")
examples1 = ["10", "101", "1110", "1010", "1", "11"]  # first 3 = accepted, last 3 = rejected
for s in examples1:
    print(f"{s!r}: {'ACCEPTED ✅' if dfa1.accepts(s) else 'REJECTED ❌'}")

# Number 2. 3 Accepted and rejected
print("\n=== Automaton 2 (a/b) ===")
examples2 = ["ab", "abaa", "abaabb", "aaa","abb", "aba"]  # first 3 = accepted, last 3 = rejected
for s in examples2:
    print(f"{s!r}: {'ACCEPTED ✅' if dfa2.accepts(s) else 'REJECTED ❌'}")


while True:
    print("\nChoose Automaton:")
    print("1. Automaton 1 (Type Only combination of 1 and 0)")
    print("2. Automaton 2 (Type Only combination of a and b)")
    print("e. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "e":
        print("Exiting...")
        break
    elif choice not in {"1", "2"}:
        print("Invalid choice, try again.")
        continue

    string = input("Enter a string to test: ").strip()

    if choice == "1":
        result = dfa1.accepts(string)
    else:
        result = dfa2.accepts(string)

    print(f"Result: {'ACCEPTED ✅' if result else 'REJECTED ❌'}")
