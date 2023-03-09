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

  

  @Override
  public String toString() {
    return "Vertice [x=" + x + ", y=" + y + ", valore=" + valore + ", wormhole=" + wormhole + ", lock=" + lock
         + ", sommaIntermedia=" + sommaIntermedia + ", step=" + step + "]";
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
