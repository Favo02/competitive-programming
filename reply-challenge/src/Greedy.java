public class Greedy {
  

  public Vertice getStart(Grafo g) {

    Vertice max = null;

    for (int y = 0; y < g.valori[0].length; y++) {
      for (int x = 0; x < g.valori.length; x++) {
        var cur = g.valori[x][y]; 
        if (!cur.lock) {
          if (max == null || max.valore < cur.valore) {
            max = cur;
          }
        } 
      }
    }

    return max;
  } 
  
}
