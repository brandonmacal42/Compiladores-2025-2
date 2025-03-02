import re
from collections import defaultdict

class State:
    def __init__(self):
        self.transitions = defaultdict(set)
        self.epsilon = set()
        self.is_final = False

class Automata:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final
    
    def accepts(self, cadena):
        def epsilon_closure(states):
            stack = list(states)
            closure = set(states)
            while stack:
                state = stack.pop()
                for next_state in state.epsilon:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
            return closure
        
        current_states = epsilon_closure({self.initial})
        for caracter in cadena:
            next_states = set()
            for state in current_states:
                next_states.update(state.transitions[caracter])
            current_states = epsilon_closure(next_states)
        return any(state.is_final for state in current_states)

def tokenize(texto):
    return re.findall(r'\w+|\S', texto)

def compile(regex: str) -> Automata:
    if '|' in regex and '(' not in regex and ')' not in regex and regex.count('|') == 1:
        pos = regex.index('|')
        left = regex[:pos]
        right = regex[pos+1:]
        if len(left) >= 1 and len(right) >= 1:
            regex = left[:-1] + "(" + left[-1] + "|" + right[0] + ")" + right[1:]
    
    postfix = infix_to_postfix(regex)
    stack = []
    
    for token in postfix:
        if token.isalnum():
            s1, s2 = State(), State()
            s1.transitions[token].add(s2)
            stack.append((s1, s2))
        elif token == '*':
            s1, s2 = State(), State()
            nfa = stack.pop()
            s1.epsilon.update([nfa[0], s2])
            nfa[1].epsilon.update([nfa[0], s2])
            stack.append((s1, s2))
        elif token == '|':
            if len(stack) < 2:
                raise ValueError("Expresión inválida: operador '|' sin suficientes operandos.")
            s1, s2 = State(), State()
            nfa2, nfa1 = stack.pop(), stack.pop()
            s1.epsilon.update([nfa1[0], nfa2[0]])
            nfa1[1].epsilon.add(s2)
            nfa2[1].epsilon.add(s2)
            stack.append((s1, s2))
        elif token == '?':
            s1, s2 = State(), State()
            nfa = stack.pop()
            s1.epsilon.update([nfa[0], s2])
            nfa[1].epsilon.add(s2)
            stack.append((s1, s2))
        elif token == '+':
            s1, s2 = State(), State()
            nfa = stack.pop()
            nfa[1].epsilon.add(nfa[0])
            nfa[1].epsilon.add(s2)
            stack.append((nfa[0], s2))
        elif token == '.':  # Concatenación explícita
            if len(stack) < 2:
                raise ValueError("Expresión inválida: concatenación sin suficientes operandos.")
            nfa2, nfa1 = stack.pop(), stack.pop()
            nfa1[1].epsilon.add(nfa2[0])
            stack.append((nfa1[0], nfa2[1]))
    
    if len(stack) != 1:
        raise ValueError("Expresión regular mal formada.")
    
    initial, final = stack.pop()
    final.is_final = True
    return Automata(initial, final)

def infix_to_postfix(regex):
    precedence = {'|': 1, '.': 2, '?': 3, '*': 3, '+': 3, '(': 0}
    output, stack = [], []
    
    augmented_regex = ""
    for i, token in enumerate(regex):
        augmented_regex += token
        if i + 1 < len(regex):
            next_token = regex[i + 1]
            if (token.isalnum() or token in '*+?)') and (next_token.isalnum() or next_token == '('):
                augmented_regex += '.'
    
    for token in augmented_regex:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # elimina el '('
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return output

# Prueba del autómata con la transformación implícita:
pattern = compile('niña|os?')
print(pattern.accepts('niño'))  # True
print(pattern.accepts('niña'))  # True
print(pattern.accepts('niñas')) # True
print(pattern.accepts('niños')) # True
print(pattern.accepts('niñs'))  # False


