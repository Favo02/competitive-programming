public class Main {
    public static void main(String[] args) throws Exception {
        
        Input i = Parser.parseInput();
        Grafo f = new Grafo(i);
        System.out.println(f);
    
    }
}
