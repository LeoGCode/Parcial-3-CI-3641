import Secuencia

class Pila<T> : Secuencia<T> {
     val pila: MutableList<T> = mutableListOf()

    override fun agregar(elemento: T) {
        pila.add(0,elemento)
    }

    override fun remover(): T? {
        return if (pila.isEmpty()) null else pila.removeAt(0)
    }

    override fun vacio(): Boolean {
        return pila.isEmpty()
    }
}