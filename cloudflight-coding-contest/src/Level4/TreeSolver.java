package Level4;

import java.util.ArrayList;
import java.util.List;

class A {
  public static void main(String[] args) {
    TreeSolver ts = new TreeSolver(5, 5, 6);
    ts.Solve('S', 3);
  }
}

public class TreeSolver {

  Status status;

  private class Status {
    public int R;
    public int P;
    public int S;

    Status() {
    }

    Status(Status other) {
      this.R = other.R;
      this.P = other.P;
      this.S = other.S;
    }

    @Override
    public boolean equals(Object obj) {
      Status other = (Status) obj;
      return other.R == this.R && other.P == this.P && other.S == S;
    }

  }

  public TreeSolver(int R, int P, int S) {
    this.status = new Status();
    status.R = R;
    status.P = P;
    status.S = S;

  }

  public ArrayList<Match> Solve(char root, int depth) {
    ArrayList<Match> step = new ArrayList<Match>();
    step.addAll(Match.GenerateFirstStep(root));
    for (int i = 0; i < depth; i++) {
      System.out.println(step);
      step = nextStep(step);
    }
    return step;
  }

  private ArrayList<Match> leafStep(Match currentStep) {
    var localStatus = new Status(this.status);
    ArrayList<Match> nextStep = new ArrayList<>(2);
    var itemLeafs = currentStep.GenerateNext();
    // choose left
    var choice = choose(itemLeafs.get(1), new Status(localStatus));
    if (!choice.equals(localStatus)) {
      nextStep.add(itemLeafs.get(1));
    } else {
      choice = choose(itemLeafs.get(0), new Status(localStatus));
      if (choice.equals(localStatus))
        throw new RuntimeException("Ran out of items");
      nextStep.add(itemLeafs.get(0));
    }
    // choose right
    choice = choose(itemLeafs.get(3), new Status(localStatus));
    if (!choice.equals(localStatus)) {
      nextStep.add(itemLeafs.get(3));
    } else {
      choice = choose(itemLeafs.get(2), new Status(localStatus));
      if (choice.equals(localStatus))
        throw new RuntimeException("Ran out of items");
      nextStep.add(itemLeafs.get(2));
    }
    this.status = choice;
    return nextStep;
  }

  private ArrayList<Match> nextStep(ArrayList<Match> currentStep) {
    var nextStep = new ArrayList<Match>(currentStep.size() * 2);
    for (var item : currentStep) {
      nextStep.addAll(leafStep(item));
    }
    return nextStep;
  }

  private Status choose(Match item, Status s) {
    Status newStatus = s;
    int R = 0, P = 0, S = 0;
    switch (item.left) {
      case 'R': {
        R++;
      }
        break;
      case 'P': {
        P++;
      }
        break;
      case 'S': {
        S++;
      }
        break;
      default:
    }
    switch (item.right) {
      case 'R': {
        R++;
      }
        break;
      case 'P': {
        P++;
      }
        break;
      case 'S': {
        S++;
      }
        break;
      default:
    }
    if (s.R < R || s.P < P || s.S < S) {
      return newStatus; // Original state
    }
    newStatus = new Status(s);
    if (s.R >= R) {
      newStatus.R -= R;
    }
    if (s.P >= P) {
      newStatus.P -= P;
    }
    if (s.S >= S) {
      newStatus.S -= S;
    }
    return newStatus;
  }

}
