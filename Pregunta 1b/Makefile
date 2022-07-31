KC=kotlinc
KFLAGS=-cp .

all: \
		Secuencia.class\
		Pila.class\
		Cola.class\
		Grafo.class\
		Busqueda.class\
		DFS.class\
		BFS.class\
		MainKt.class\


Secuencia.class: Secuencia.kt
	${KC} ${KFLAGS} Secuencia.kt

Pila.class: Pila.kt
	${KC} ${KFLAGS} Pila.kt

Cola.class: Cola.kt
	${KC} ${KFLAGS} Cola.kt

Grafo.class: Grafo.kt
	${KC} ${KFLAGS} Grafo.kt

Busqueda.class: Busqueda.kt
	${KC} ${KFLAGS} Busqueda.kt

DFS.class: DFS.kt
	${KC} ${KFLAGS} DFS.kt

BFS.class: BFS.kt
	${KC} ${KFLAGS} BFS.kt

MainKt.class: main.kt
	${KC} ${KFLAGS} main.kt

run: MainKt.class
	kotlin MainKt

clean:
	rm -rf *.class META-INF