from Automata import compile, tokenize

# Construye el autómata de la regex
pattern = compile('niña|os?')

#Cadenas que acepta
print(pattern.accepts('niño'))
print(pattern.accepts('niña'))
print(pattern.accepts('niñas'))
print(pattern.accepts('niños'))
print(pattern.accepts('niñs'))

"""### d. Utiliza el autómata para localizar los patrones que coinciden en el siguiente texto (la función tokenize utiliza los espacios en blanco para obtener tókens):"""

# Tokenización del texto
text = tokenize('Las niñas extranjeras jugaban con el niño y la niña en el patio.')



# Encuentra las correspondecias
matches = pattern.match_token(text)

# Imprime índices y tokenes
# que cumplen el patrón dentro del texto
for i in matches:
    print(i, text[i])

