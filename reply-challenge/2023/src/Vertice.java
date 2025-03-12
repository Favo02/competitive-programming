import java.util.ArrayList;
import java.util.List;

public class Vertice {
  final int x;
  final int y;

  final int valore;
  final boolean wormhole;

  boolean lock;

  List<Vertice> adiacenti;

  int sommaIntermedia;
  int step;

  public Vertice(int x, int y, int valore, boolean wormhole) {
    this.x = x;
    this.y = y;

    this.valore = valore;
    this.wormhole = wormhole;

    this.sommaIntermedia = Integer.MIN_VALUE;
    this.step = -1;

    this.lock = false;
    this.adiacenti = new ArrayList<>();
  }

  public String completeToString() {
    StringBuilder sb = new StringBuilder();
    sb.append('x');
    sb.append(x);
    sb.append('y');
    sb.append(y);
    sb.append(" - valore: ");
    sb.append(valore);
    sb.append(" - worm: ");
    sb.append(wormhole);
    sb.append(" - lock: ");
    sb.append(lock);
    sb.append(" - adiacenti: ");
    sb.append(adiacenti);
    sb.append(" - sommaInt: ");
    sb.append(sommaIntermedia);
    sb.append(" - step: ");
    sb.append(step);
    return sb.toString();
  }

  @Override
  public String toString() {
    if (step != -1) {
      return String.format("[%d]", step);
    }
    return String.format("%d-%d", x, y);
  }

  public void lock() {
    this.lock = true;
  }

  public boolean isLocked() {
    return this.lock;
  }

  public void addAdiacente(Vertice v) {
    this.adiacenti.add(v);
  }
}
