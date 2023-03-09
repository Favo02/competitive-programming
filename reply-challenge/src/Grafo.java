public class Grafo {
  Vertice[][] valori;

  // aggiunge solo in un senso
  public void addAdiacente(int fromX, int fromY, int toX, int toY) {
    valori[fromX][fromY].addAdiacente(valori[toX][toY]);
  }


  public Grafo(Input input) {

    this.valori = new Vertice[input.r][input.c];

    for (int y = 0; y < input.r; y++) {
      for (int x = 0; x < input.c; x++) {
        if (input.rawMatrix[x][y] == Integer.MAX_VALUE) { // wormhole
          valori[x][y] = new Vertice(x, y, input.rawMatrix[x][y], true);
        } else { // no wormhole
          valori[x][y] = new Vertice(x, y, input.rawMatrix[x][y], false);
        }

      }
    }

    for (int y = 0; y < input.r; y++) {
      for (int x = 0; x < input.c; x++) {

        // no wormhole
        if (!valori[x][y].wormhole) {

          // prima riga
          if (y == 0) {
    
            valori[x][y].addAdiacente(valori[x][input.r-1]); // up
            valori[x][y].addAdiacente(valori[x][y-1]); // down
            valori[x][y].addAdiacente(valori[x-1][y]); // right
            valori[x][y].addAdiacente(valori[x+1][y]); // left
            
            continue;
          }

          // ultima riga
          if (y == input.r) {


            continue;
          }

          // prima colonna
          if (x == 0) {

            continue;
          }

          // ultima colonna
          if (x == input.c) {

            continue;
          }

          valori[x][y].addAdiacente(valori[x][y+1]); // up
          valori[x][y].addAdiacente(valori[x][y-1]); // down
          valori[x][y].addAdiacente(valori[x-1][y]); // right
          valori[x][y].addAdiacente(valori[x+1][y]); // left
        }


      }
    }
  }
}
