import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

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
        Set<Vertice> visitati = new HashSet<>();
        coda.add(curVer);

        while (!coda.isEmpty()) {
            System.out.print("coda: " + coda + "\n");
            curVer = coda.remove();
            if (visitati.contains(curVer))
                continue;
            visitati.add(curVer);
            for (Vertice adiacente : curVer.adiacenti) {
                if (adiacente.lock == true)
                    continue;
                if (adiacente.sommaIntermedia < curVer.sommaIntermedia + adiacente.valore) {
                    if (adiacente.step > curVer.step + 1 || adiacente.step == -1)
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

        List<Vertice> tempSerp = new LinkedList<>(); // TODO To remove
        var serpenteFinale = new Serpente(dim);
        serpenteFinale.addVertice(maxVer);
        tempSerp.add(maxVer);
        System.out.println("MAX: " + maxVer);
        maxVer.lock = true;

        Vertice curMax = maxVer;
        curVer = maxVer;
        System.out.println("curVer:" + curVer);
        List<Vertice> candidati = new LinkedList<>();
        int i = 0;
        while (curVer.step != 1) {
            candidati.clear();
            System.out.println("-----------------CUR-----------------");
            System.out.println("cureVer: " + curVer);
            System.out.println("cureMax: " + curMax);
            System.out.println("-----------------ADIACENTI-----------------");
            for (Vertice vertice : curVer.adiacenti) {
                if (vertice.step == curVer.step - 1) {
                    System.out.println(vertice);
                    candidati.add(vertice);
                }
            }
            curMax = candidati.get(0);
            System.out.println("-----------------CANDIDATI-----------------");
            for (Vertice vertice : candidati) {
                System.out.println(vertice);
                if (vertice.sommaIntermedia > curMax.sommaIntermedia) {
                    curMax = vertice;
                }
            }

            curMax.lock = true;
            serpenteFinale.addVertice(curMax);
            tempSerp.add(curMax);
            curVer = curMax;

            System.out.println("-----------------PRESI-----------------");
            System.out.println(tempSerp + "\n");
            System.out.println("----------------------------------\n\n");
            // i++;
            if (i == 3) {

                throw new IllegalArgumentException();
            }
        }

        curVer.lock = true;
        // serpenteFinale.addVertice(curVer);
        // tempSerp.add(curVer);
        System.out.println(tempSerp);
        return serpenteFinale;
    }
}
