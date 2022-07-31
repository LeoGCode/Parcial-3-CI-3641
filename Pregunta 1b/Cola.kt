import Secuencia

class Cola<T> : Secuencia<T> {
    val cola: MutableList<T> = mutableListOf()

    override fun agregar(elemento: T) {
        cola.add(elemento)
    }

    override fun remover(): T? {
        return if (cola.isEmpty()) null else cola.removeAt(0)
    }

    override fun vacio(): Boolean {
        return cola.isEmpty()
    }
}