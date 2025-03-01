# Práctica 1: Expresiones Regulares y Lexers

Este proyecto implementa un sistema para identificar patrones en cadenas de texto utilizando **autómatas finitos** y expresiones regulares.

## 1️⃣ Clase `Automata` (Autómata Finito)

Esta clase representa un autómata finito que puede ser **determinista o no determinista**.  
 Su objetivo es reconocer cadenas que pertenezcan a un lenguaje definido por un conjunto de reglas de transición.

- `states`: Conjunto de estados posibles del autómata.
- `initial`: Estado inicial desde donde empieza el análisis.
- `final`: Conjunto de estados finales (aceptación).
- `transitions`: Un diccionario que indica cómo cambia el estado del autómata según el símbolo de entrada.

### 🛠️ Métodos

#### 🔹 `accepts(cadena: str) -> bool`

- Verifica si una cadena es aceptada por el autómata.
- **Recorre** la cadena de entrada y cambia de estado según las transiciones definidas.
- Si el estado final es parte del conjunto de estados de aceptación, **retorna `True`**, de lo contrario, **retorna `False`**.

#### 🔹 `match_token(texto: str) -> list`

- Encuentra **todos los tokens válidos** en el texto que sean reconocidos por el autómata.
- Recorre el texto y almacena las posiciones `(inicio, fin)` de los fragmentos que sean aceptados por el autómata.

---

## 2️⃣ Función `compile(regex: str) -> Automata`

- Construye un autómata a partir de una **expresión regular**.
- **Debe reconocer** los operadores:
  - `|` (or)
  - `*` (cierre de Kleene)
  - `+` (una o más veces)
  - `?` (cero o una vez)
- **Retorna** un objeto de la clase `Automata` que representa el autómata generado.

---

## 3️⃣ Pruebas con un Autómata Generado

Se crea un **autómata** a partir de la siguiente expresión regular:

```python
pattern = compile('niña|os?')
```

## 1️⃣ Instalación y Requisitos

- Se requiere **Python 3.x** para ejecutar el programa.
- Para verificar la instalación de Python:
  ```bash
  python3 --version
  ```

---

## 2️⃣ Ejecución del Programa

### a. Ejecutar el archivo principal

- Desde la terminal, dentro del directorio donde está `practica1_compiladores.py`:
  ```bash
  python3 practica1_compiladores.py
  ```
- Esto ejecutará las pruebas del autómata y mostrará los resultados en la consola.

### b. Importar en otro script

- Para usar el autómata en otro archivo Python:

  ```python
  from automata import compile, tokenize

  pattern = compile('niña|os?')
  print(pattern.accepts('niña'))  # True
  print(pattern.match_token('El niño y la niña juegan.'))
  ```

- Esto permite construir autómatas personalizados y analizarlos en distintas cadenas.

---

## 3️⃣ Posibles Errores y Soluciones

- **Error:** `NameError: name 'tokenize' is not defined`

  - **Causa:** La función `tokenize()` no está definida o no ha sido importada.
  - **Solución:** Asegúrate de que `tokenize` está correctamente importado en `practica1_compiladores.py`.

- **Error:** `TypeError: Automata.accepts() missing 1 required positional argument: 'cadena'`
  - **Causa:** El método `accepts()` no está recibiendo un argumento válido.
  - **Solución:** Verifica que el autómata se esté creando correctamente con `compile(regex)` y que `accepts()` se llame con una cadena válida.

---
