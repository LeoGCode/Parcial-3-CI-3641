/**
 * Define a data type that represents graphs as adjacency lists
 * and each node is represented by an integer. node is represented
 * by an integer (you can use all the libraries available in the language). available in the language).
 *
 * In addition, define an abstract class Search that must have a method search.
 * This method must receive two integers: D and H, and it must return the number of nodes
 * explored, starting from node D until reaching node H. In case H is not reachable from D,
 * it must return the number of nodes explored. is not reachable from D, it must return the value -1 (minus one).
 * This class must be partially implemented, leaving only the abstracted order in which the nodes are to be explored.
 */

import Grafo

import Secuencia

abstract class Busqueda(val grafo: Grafo) {

    abstract fun getSecuencia(): Secuencia<Int>

    fun buscar(D: Int, H: Int): Int {
        val color = Array(grafo.grafo.size) { false }
        var nodosExplorados = 0
        val sec: Secuencia<Int> = getSecuencia()
        sec.agregar(D)
        color[D] = true
        while (!sec.vacio()) {
            val n = sec.remover()!!
            print("$n ")
            if (n == H) {
                println()
                return nodosExplorados
            }
            for (i in grafo.grafo[n]) {
                if (!color[i]) {
                    sec.agregar(i)
                    color[i] = true
                }
            }
            nodosExplorados++
        }
        println()
        nodosExplorados = -1
        return nodosExplorados
    }
}