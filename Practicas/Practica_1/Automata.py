class Automata:
    def __init__(self, states, initial, final, transitions):
        self.states = states
        self.initial = initial
        self.final = final
        self.transitions = transitions

    def accepts(self, cadena):
        q_actual = self.initial
        for caracter in cadena:
            if (q_actual, caracter) in self.transitions:
                q_actual = self.transitions[(q_actual, caracter)]
            else:
                return False
        return q_actual in self.final

    def match_token(self, texto):
        posicion_token = []
        for i in range(len(texto)):
            q_actual = self.initial
            for j in range(i, len(texto)):
                if (q_actual, texto[j]) in self.transitions:
                    q_actual = self.transitions[(q_actual, texto[j])]
                    if q_actual in self.final:
                        posicion_token.append((i, j+1))
                else:
                    break
        return posicion_token

def compile(regex: str) -> Automata:
    """Función que regresa un autómata finito construyéndolo a partir de una expresión regular"""
    return Automata(states=set(), initial=0, final=set(), transitions={})

def tokenize(texto):
    """Divide el texto en tokens separados por espacios"""
    return texto.split()
