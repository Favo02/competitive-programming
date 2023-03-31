import java.util.ArrayList;
import java.util.List;
public class Solver {


  public static String solve(String line) {
      return runLine(line);
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
    while(res.size() >= 2) {
      res = parseLine(res);
    }
    return createOutString(res);
  }

  public static List<String> splitRounds(String fullLine) {
    List<String> out = new ArrayList<String>();
    char[] arrayChar = fullLine.toCharArray();
    for(int i = 0; i < fullLine.length(); i+=2) {
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
