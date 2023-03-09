import java.util.ArrayList;

public class Serpente {
    public Vertice[] vertici;
    public final int segmenti;
    private int mossa;

    public Serpente(int segmenti) {
        this.segmenti = segmenti;
        this.mossa = 0;
        vertici = new Vertice[segmenti];
    }

    public void addVertice(Vertice vertice) {
        vertici[this.mossa++] = vertice;
    }

    public void addVertici(Vertice[] vertici) {
        this.vertici = vertici;
    }

    public int getPunteggio() {
        int punteggio = 0;
        for (Vertice vert : this.vertici) {
            if (!vert.wormhole) {
                punteggio += vert.valore;
            }
        }
        return punteggio;
    }

    public void reverse() {
        for (int i = 0; i < this.segmenti; i++) {
            Vertice tmp = this.vertici[i];
            this.vertici[i] = this.vertici[this.segmenti - i];
            this.vertici[this.segmenti - i] = tmp;
        }
    }
    @Override
    public String toString() {
        /* Devo generare:
            (X Y MOSSE)
            X Y = Coordinate di partenza
            MOSSE = U/D/L/R o (x, y) coordinate worme hole
        */
        Vertice partenza = this.vertici[0];
        StringBuilder output = new StringBuilder();
        output.append(partenza.x);
        output.append(' ');
        output.append(partenza.y);
        output.append(' ');

        for(int i = 0; i < this.segmenti - 1; i++) {
            // Se wormhole aggiungere la direzione verso il wormhole e le coordinate di uscita
            Vertice vert = this.vertici[i];
            Vertice vertProx = this.vertici[i + 1];
            char direzione = 'U';
            if (vert.y == vertProx.y) {
                if (vertProx.x > vert.x) {
                    direzione = 'R';
                } else {
                    direzione = 'L';
                }
            } else {
                if (vertProx.y > vert.y)
                    direzione = 'D';
            }
            output.append(direzione);
            output.append(' ');
            if ( vertProx.wormhole ) {
                output.append(this.vertici[i + 1].x);
                output.append(' ');
                output.append(this.vertici[i + 1].y);
                output.append(' ');
            }
        }


        return output.toString();
    }

}
