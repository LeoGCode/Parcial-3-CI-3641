interface Secuencia<T> {
    fun agregar(elemento: T)
    fun remover(): T?
    fun vacio(): Boolean
}