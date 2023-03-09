import java.util.Scanner;

public class Parser {

    public static Input parseInput() {
        int c;
        int r;
        int s;
        String line;
        String[] splittedLine;
        int[] serpenti;
        int[][] rawMatrix;

        Scanner scanner = new Scanner(System.in);
        line = scanner.nextLine();
        splittedLine = line.split(" ");
        c = Integer.parseInt(splittedLine[0]);
        r = Integer.parseInt(splittedLine[1]);
        s = Integer.parseInt(splittedLine[2]);

        serpenti = new int[s];
        rawMatrix = new int[c][r];

        line = scanner.nextLine();
        splittedLine = line.split(" ");

        int i = 0;
        for (String string : splittedLine) {
            serpenti[i] = Integer.parseInt(string);
            i++;
        }

        int y = 0; // numero di riga
        int x = 0; // numero di colonna
        while (scanner.hasNext()) {
            line = scanner.nextLine();
            splittedLine = line.split(" ");
            x = 0;
            for (String token : splittedLine) {
                if (token == "*")
                    rawMatrix[x][y] = Integer.MAX_VALUE;
                else
                    rawMatrix[x][y] = Integer.parseInt(token);
                x++;
            }
            y++;
        }
        return new Input(c, r, s, serpenti, rawMatrix);
    }

}
