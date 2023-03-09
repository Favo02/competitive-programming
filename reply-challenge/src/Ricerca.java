import java.util.LinkedList;
import java.util.Queue;

public class Ricerca {
    public Grafo g;

    public Ricerca(Grafo g) {
        this.g = g;
    }

    public Serpente piazzaSerpente(int x, int y, int dim) {
        var curVer = g.valori[x][y];
        curVer.sommaIntermedia = curVer.valore;
        curVer.lock = true;
        curVer.step = 1;
        var maxVer = curVer;

        Queue<Vertice> coda = new LinkedList<Vertice>();

        while (!coda.isEmpty()) {
            curVer = coda.remove();
            for (Vertice adiacente : curVer.adiacenti) {
                if (adiacente.sommaIntermedia < curVer.sommaIntermedia + adiacente.valore) {
                    adiacente.step = curVer.step + 1;
                    if (adiacente.step > dim) {
                        continue;
                    }
                    adiacente.sommaIntermedia = curVer.sommaIntermedia + adiacente.valore;
                    coda.add(adiacente);
                    if (curVer.sommaIntermedia > maxVer.sommaIntermedia) {
                        maxVer = curVer;
                    }
                }
            }
        }

        var serpenteFinale = new Serpente(dim);
        serpenteFinale.addVertice(maxVer);
        maxVer.lock = true;

        Vertice curMax = maxVer;
        curVer = maxVer;

        while (curVer.step != 1) {
            curMax = curVer.adiacenti.get(0);
            for (Vertice vertice : curVer.adiacenti) {
                if (vertice.step == curVer.step - 1 && vertice.sommaIntermedia > curMax.sommaIntermedia) {
                    curMax = vertice;
                }
            }
            curMax.lock = true;
            serpenteFinale.addVertice(curMax);
            curVer = curMax;
        }

        curVer.lock = true;
        serpenteFinale.addVertice(curVer);
        return serpenteFinale;
    }
}
