import java.util.ArrayList;
import java.util.List;

public class Utilities {

  public static int findMaxSumSubmatrix(int[][] matrix) {
    // caso base
    if (matrix == null || matrix.length == 0) {
      return 0;
    }

    // Matrice `M × N`
    int M = matrix.length;
    int N = matrix[0].length;

    // `S[i][j]` memorizza la somma della sottomatrice formata dalla riga 0 a `i-1`
    // e dalla colonna 0 a `j-1`
    int[][] S = new int[M + 1][N + 1];

    // preelabora la matrice per riempire `S`
    for (int i = 0; i <= M; i++) {
      for (int j = 0; j <= N; j++) {
        if (i == 0 || j == 0) {
          S[i][j] = 0;
        } else {
          S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] +
              matrix[i - 1][j - 1];
        }
      }
    }

    int maxSum = Integer.MIN_VALUE;
    int rowStart = 0, rowEnd = 0, colStart = 0, colEnd = 0;

    // considera ogni sottomatrice formata dalla riga da `i` a `j`
    // e le colonne da `m` a `n`
    for (int i = 0; i < M; i++) {
      for (int j = i; j < M; j++) {
        for (int m = 0; m < N; m++) {
          for (int n = m; n < N; n++) {
            // calcola la somma della sottomatrice usando `S[][]` nel tempo O(1).
            int submatrix_sum = S[j + 1][n + 1] - S[j + 1][m]
                - S[i][n + 1] + S[i][m];

            // se la somma della sottomatrice è maggiore del massimo trovato finora
            if (submatrix_sum > maxSum) {
              maxSum = submatrix_sum;
              rowStart = i;
              rowEnd = j;
              colStart = m;
              colEnd = n;
            }
          }
        }
      }
    }

    List<List<Integer>> result = new ArrayList<>();
    for (int i = rowStart; i <= rowEnd; i++) {
      List<Integer> row = new ArrayList<>();
      for (int j = colStart; j <= colEnd; j++) {
        row.add(matrix[i][j]);
      }
      result.add(row);
    }

    System.out.println("The maximum sum submatrix is " + result);
    return maxSum;
  }

}
