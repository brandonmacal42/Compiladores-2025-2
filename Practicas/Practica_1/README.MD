IDENTIFICADORES
[a-zA-Z\_][a-zA-Z0-9_]\* { printf("IDENTIFICADOR: %s\n", yytext); }
-Reconoce nombres de variables y funciones.
-Deben empezar con una letra o _.
-Pueden contener letras, números y _ después.

OPERADORES BINARIOS
+|-|\*|/|% { printf("OPERADOR_BINARIO: %s\n", yytext); }
-Detecta los operadores matemáticos +, -, \*, /, %.

OPERADORES UNARIOS
++|-- { printf("OPERADOR_UNARIO: %s\n", yytext); }
-Detecta ++ y --.

OPERADORES DE RELACION
==|!=|<=|>=|<|> { printf("OPERADOR_RELACIONAL: %s\n", yytext); }
-Detecta ==, !=, <=, >=, <, >.
-Se usan en comparaciones y estructuras condicionales.

ESPACIOS
[ \t\n] ; /_ Ignorar espacios y saltos de línea _/
-Ignora espacios, tabulaciones y saltos de línea.
-No genera salida para estos caracteres.

OTRO CARACTER
. { printf("OTRO: %s\n", yytext); }
-Imprime "OTRO" para cualquier carácter no contemplao.

CÓMO COMPILAR Y EJECUTAR

1. Guarda el código en un archivo lexer.l.

2. Genera el código en C:
   flex lexer.l

3. Compila el código:
   gcc lex.yy.c -o lexer

4. Ejecuta el lexer:
   ./lexer

Ingresa una expresión y observa los tokens generados.
