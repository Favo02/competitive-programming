package Algorithms;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;

import Structures.Graphs.Vertex;
import Structures.Graphs.Implementations.Unweighted.AdjacencyListGraph;

public class Searchs {

  public static <TKey> Map<Vertex<TKey>, Long> bfs(AdjacencyListGraph<TKey> graph, Vertex<TKey> start) {
    
    Map<Vertex<TKey>, Long> distances = new HashMap<>();

    Queue<Vertex<TKey>> queue = new LinkedList<>();

    distances.put(start, Long.valueOf(0));
    queue.add(start);

    while (queue.size() != 0) {
      Vertex<TKey> cur = queue.poll();

      Iterator<Vertex<TKey>> adjacentIterator = graph.getAdjacentByVertexIterator(cur);

      while (adjacentIterator.hasNext()) {
        Vertex<TKey> adj = adjacentIterator.next();

        if (!(distances.containsKey(adj))) {
          distances.put(adj, distances.get(cur) + 1);
          queue.add(adj);
        }
      }
    }

    return distances;
  }

  public static <TKey> List<Vertex<TKey>> dfs(AdjacencyListGraph<TKey> graph, Vertex<TKey> start) {

    List<Vertex<TKey>> visisted = new ArrayList<>();
    Stack<Vertex<TKey>> stack = new Stack<>();

    visisted.add(start);
    stack.push(start);

    while (!stack.isEmpty()) {
      Vertex<TKey> cur = stack.pop();

      if (!(visisted.contains(cur))) {
        visisted.add(cur); // visit

        Iterator<Vertex<TKey>> adjacentIterator = graph.getAdjacentByVertexIterator(cur);

        while (adjacentIterator.hasNext()) {
          Vertex<TKey> adj = adjacentIterator.next();
          
          if (!(visisted.contains(adj))) {
            stack.push(adj);
          }
        }
      }
    }

    return visisted;
  }

}
