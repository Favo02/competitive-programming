

public class Serpente {
    public Vertice[] vertici;
    public int lunghezza;

    public Serpente(int lunghezza) {
        this.lunghezza = lunghezza;
        vertici = new Vertice[lunghezza];
    }

    @Override
    public String toString() {
        /* Devo generare:
            (X Y MOSSE)
            X Y = Coordinate di partenza
            MOSSE = U/D/L/R o (x, y) coordinate worme hole
        */
        return super.toString();
    }

}
