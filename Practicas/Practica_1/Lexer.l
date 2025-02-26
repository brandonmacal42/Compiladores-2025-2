%option noyywrap
%{
#include <stdio.h>
%}

%%
[a-zA-Z_][a-zA-Z0-9_]*  { printf("IDENTIFICADOR: %s\n", yytext); }

\+|\-|\*|\/|%        { printf("OPERADOR_BINARIO: %s\n", yytext); }
\+\+|\-\-            { printf("OPERADOR_UNARIO: %s\n", yytext); }
==|!=|<=|>=|<|>       { printf("OPERADOR_RELACIONAL: %s\n", yytext); }

if|else|while|return  { printf("KEYWORD: %s\n", yytext); }

[0-9]+                { printf("NUMERO_ENTERO: %s\n", yytext); }
[0-9]+\.[0-9]+       { printf("NUMERO_FLOTANTE: %s\n", yytext); }

\"([^\"]*)\"       { printf("LITERAL: %s\n", yytext); }

[.,;:(){}\[\]]        { printf("SIGNO_DE_PUNTUACION: %s\n", yytext); }

true|false            { printf("BOOLEANO: %s\n", yytext); }

[ \t\n]              ; /* Ignorar espacios y saltos de línea */
.                   { printf("OTRO: %s\n", yytext); }
%%

int main() {
    printf("Ingresa una expresión:\n");
    yylex();
    return 0;
}
