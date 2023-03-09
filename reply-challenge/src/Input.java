import java.util.Arrays;

public class Input {
    public int c;
    public int r;
    public int s;
    public int[] serpenti;
    public int[][] rawMatrix;

    public Input(int c, int r, int s, int[] serpenti, int[][] rawMatrix) {
        this.c = c;
        this.r = r;
        this.s = s;
        this.serpenti = serpenti;
        this.rawMatrix = rawMatrix;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("colonne: %d, righe: %d serpenti: %d \n", c, r, s)); // TODO rimuovere nel caso serva un
                                                                                     // toString uguale all'input
        sb.append("Serpenti: ");
        sb.append(Arrays.toString(serpenti));
        sb.append('\n');

        int curVal;
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                curVal = rawMatrix[x][y];
                if (curVal == Integer.MAX_VALUE)
                    sb.append('*');
                else
                    sb.append(rawMatrix[x][y]);
                sb.append(' ');
            }
            sb.append('\n');
        }
        sb.append('\n');
        return sb.toString();
    }

}
