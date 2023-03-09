public class Grafo {
  Vertice[][] valori;

  // aggiunge solo in un senso
  public void addAdiacente(int fromX, int fromY, int toX, int toY) {
    valori[fromX][fromY].addAdiacente(valori[toX][toY]);
  }
}
