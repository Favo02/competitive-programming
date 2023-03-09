public class Main {
    public static void main(String[] args) throws Exception {
        
        Input i = Parser.parseInput();
        Grafo g = new Grafo(i);
        Ricerca r = new Ricerca(g);

        var start = Greedy.getStart(g);

        System.out.println("s" + start);
        var s = r.piazzaSerpente(start.x, start.y, 3);

        System.out.println(s);
    
    }
}
