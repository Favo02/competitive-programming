import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

public class Ricerca {
    public Grafo g;

    public Ricerca(Grafo g) {
        this.g = g;
    }

    public Serpente piazzaSerpente(int x, int y, int dim) {
        var curVer = g.valori[x][y];
        var coda = new HashSet<Vertice>(); // implementare con una priorityqueue con comparator
        var serpenteFinale = new Serpente(dim);

        coda.add(curVer);
        int step = 0;
        while (step < dim) {
            var maxVertice = new Vertice(-1, -1, Integer.MIN_VALUE, false); // Da allocare fuori una sola volta
            for (Vertice v : coda) {
                if (v.valore > maxVertice.valore) {
                    maxVertice = v;
                }
            }
            coda.remove(maxVertice);
            maxVertice.lock = true;
            maxVertice.step = step;
            serpenteFinale.addVertice(maxVertice);
            for (Vertice v : maxVertice.adiacenti) {
                if (!v.lock)
                    coda.add(v);
            }
            step++;
        }
        System.out.println(g.debugToString());

        return serpenteFinale;
    }
}
