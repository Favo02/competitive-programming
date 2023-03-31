import java.util.LinkedList;
import java.util.Scanner;

public class Level1 {
  public static void main(String[] args) {
    output(parser());

  }

  public static void output(LinkedList<String> lines) {
    for (var item : lines) {
      System.out.println(winner(item.charAt(0), item.charAt(1)));
    }
  }

  public static LinkedList<String> parser() {
    Scanner scanner = new Scanner(System.in);
    var lines = new LinkedList<String>();
    while (scanner.hasNext()) {
      var line = scanner.nextLine();
      lines.add(line);
    }
    scanner.close();
    lines.removeFirst();
    return lines;

  }

  public static char winner(char a, char b) {
    if (a == b)
      return a;

    if (a == 'R') {
      if (b == 'P')
        return b;
      if (b == 'S')
        return a;
    }

    if (a == 'P') {
      if (b == 'R')
        return a;
      if (b == 'S')
        return b;
    }

    if (a == 'S') {
      if (b == 'P')
        return a;
      if (b == 'R')
        return b;
    }

    return ' ';
  }
}
