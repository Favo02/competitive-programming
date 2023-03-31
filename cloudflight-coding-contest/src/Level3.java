import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Level3 {

  static int N = 0; // Numero tornei 
  static int M = 0; // Numero fighters
  static int amountR, amountP, amountS = 0;
  public static void main(String[] args) {
    var lines = parser();
    int i = 1;
    for (String line : lines) {
        // System.out.println("Trying lines: " + i++);
        amountR = Integer.parseInt(line.split(" ")[0].replace("R", ""));
        amountP = Integer.parseInt(line.split(" ")[1].replace("P", ""));
        amountS = Integer.parseInt(line.split(" ")[2].replace("S", ""));
        System.out.println(fillContainers(amountP, amountR, amountS));
    }
  }

  public static String fillContainers(int p, int r, int s) {
    int index = 0;
    int tot = M;

    char[] containers = new char[tot];

    // System.out.println(p);
    // System.out.println(r);
    // System.out.println(s);

    int rcont = 0;
    while (index < tot) {
      if (r > 3 && p > 1) {
        // System.out.print("z");
        containers[index] = 'R';
        containers[index+1] = 'R';
        containers[index+2] = 'R';
        containers[index+3] = 'P';
        r-=3;
        p--;
        index += 4;
        continue;
      }

      if (r < 3 && r > 0) {
        // System.out.print("y");
        // System.out.print(r);
        // System.out.print(p);
        
        containers[index] = 'R';
        r--;
        index++;

        if (p > 0) {

          containers[index] = 'P';
          p--;
          index++;
        }
        continue;
      }

      if (r > 0 && rcont < 3) {
        // System.out.print("a");
        
        containers[index] = 'R';
        rcont++;
        r--;
        index++;
        continue;
      }

      else if (r > 0 && rcont == 3) {
        // System.out.print("b");
        containers[index] = 'P';
        rcont = 0;
        p--;
        index++;
        continue;
      }

      if (r == 0 && p > 0) {
        // System.out.print("c");
        // 
        containers[index] = 'P';
        p--;
      index++;
      continue;
      }
      
      if (r==0 && p == 0) {
        // System.out.print("d");
        containers[index] = 'S';
        
      index++;
      continue;
      }

    }

    
    // return Arrays.toString(containers);
    return Arrays.toString(containers).replace("[", "").replace(", ", "").replace("]", "");
  }



  public static String createOutString(List<String> list){
    StringBuilder sb = new StringBuilder();
    for (var item : list) {
        sb.append(item);
    }
    return sb.toString();
      }
  
  
  public static String runLine(String fullLine) {
    var res = splitRounds(fullLine);
    for (int i = 0; i < 2; i++) {
      res = parseLine(res);
    }
    return createOutString(res);
  }

  public static List<String> splitRounds(String fullLine) {
    List<String> out = new ArrayList<String>();
    char[] arrayChar = fullLine.toCharArray();
    for(int i = 0; i < M; i+=2) {
      out.add(String.format("%s%s", arrayChar[i], arrayChar[i + 1]));
    }
    return out;
  }

  public static List<String> parseLine(List<String> parsedLine){
    var newLine = new ArrayList<String>(parsedLine.size()/2);
      for (int i = 0; i < parsedLine.size(); i+=2) {
        var item1 = parsedLine.get(i);
        var item2 = parsedLine.get(i+1);

        // System.out.println("i1" + item1);
        // System.out.println("i2" + item2);

        var winner1 = winner(item1.charAt(0), item1.charAt(1));
        var winner2 = winner(item2.charAt(0), item2.charAt(1));
        newLine.add(String.format("%c%c", winner1, winner2) );
      }
      // System.out.println(newLine);
      return newLine;
  }

  public static List<String> parser() {
    Scanner scanner = new Scanner(System.in);
    var lines = new ArrayList<String>();
    int lineIndex = 0;
    while (scanner.hasNext()) {
      
      var line = scanner.nextLine();
      if (lineIndex == 0) {
        N = Integer.parseInt(line.split(" ")[0]);
        M = Integer.parseInt(line.split(" ")[1]);
        
      } else {
        lines.add(line);
      }
      lineIndex++;
    }
    scanner.close();
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
