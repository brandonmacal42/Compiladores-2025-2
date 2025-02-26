

Identificadores
[a-zA-Z_][a-zA-Z0-9_]*  { printf("IDENTIFICADOR: %s\n", yytext); }

Reconoce nombres de variables y funciones.

Deben empezar con una letra o _.

Pueden contener letras, números y _ después.

Operadores Binarios
+|-|*|/|%        { printf("OPERADOR_BINARIO: %s\n", yytext); }

Detecta los operadores matemáticos +, -, *, /, %.

Se usan en operaciones matemáticas.

Operadores Unarios
++|--            { printf("OPERADOR_UNARIO: %s\n", yytext); }

Detecta ++ y --.

Se usan para incrementar y decrementar variables.

Operadores Relacionales
==|!=|<=|>=|<|>       { printf("OPERADOR_RELACIONAL: %s\n", yytext); }

Detecta ==, !=, <=, >=, <, >.

Se usan en comparaciones y estructuras condicionales.

Espacios y saltos de línea
[ \t\n]              ; /* Ignorar espacios y saltos de línea */

Ignora espacios, tabulaciones y saltos de línea.

No genera salida para estos caracteres.

Cualquier otro carácter
.                   { printf("OTRO: %s\n", yytext); }

Imprime "OTRO" para cualquier carácter no contemplado.

Útil para detectar errores o caracteres no reconocidos.

FUNCIÓN PRINCIPAL

int main() {
printf("Ingresa una expresión:\n");
yylex();
return 0;
}

main(): Ejecuta el lexer y procesa la entrada del usuario.

yylex(): Lee la entrada y aplica las reglas definidas.

CÓMO COMPILAR Y EJECUTAR

Guarda el código en un archivo lexer.l.

Genera el código en C:
flex lexer.l

Compila el código:
gcc lex.yy.c -o lexer

Ejecuta el lexer:
./lexer

Ingresa una expresión y observa los tokens generados.