import java.util.ArrayList;
import java.util.List;

public class Match{
    public char left;
    public char right;

    public Match(char left, char right){
        this.left = left;
        this.right = right;
    }

    public List<Match> GenerateNext(){
        var next = new  ArrayList<Match>(4);
        next.add(new Match(left, left));
        next.add(new Match(left, findCharToWin(left)));
        next.add(new Match(right, right));
        next.add(new Match(right, findCharToWin(right)));
        return next;
    }

    public static List<Match> GenerateFirstStep(char root){
        var next = new  ArrayList<Match>(2);
        next.add(new Match(root, root));
        next.add(new Match(root, findCharToWin(root)));
        return next;
    }

    public char winner() {
        if (left == right)
        return left;

        if (left == 'R') {
        if (right == 'P')
            return right;
        if (right == 'S')
            return left;
        }

        if (left == 'P') {
        if (right == 'R')
            return left;
        if (right == 'S')
            return right;
        }

        if (left == 'S') {
        if (right == 'P')
            return left;
        if (right == 'R')
            return right;
        }

        return ' ';
    }

    public static char findCharToWin(char a){
        switch (a) {
            case 'R':
                return 'S';
            case 'P':
                return 'R';
            case 'S':
                return 'P';
        }
        return '0';
    }

    @Override
    public String toString() {
        return String.format("%c%c", left, right);
    }

    
}
