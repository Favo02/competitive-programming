package Algorithms;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import Structures.FibonacciHeap;
import Structures.Graphs.Vertex;
import Structures.Graphs.WeightedEdge;
import Structures.Graphs.Implementations.Weighted.EdgesListGraph;
import Structures.Graphs.Implementations.Weighted.IncidenceListGraph;
import Structures.Graphs.Implementations.Weighted.WeightedAdjacencyMatrix;

public class ShortestPaths {

  // Algorithm based on implementaion by Keith Schwarz (htiek@cs.stanford.edu)
  // (http://keithschwarz.com/interesting)
  public static <TKey> Map<Vertex<TKey>, Long> dijkstra(IncidenceListGraph<TKey> graph, Vertex<TKey> start) {

    FibonacciHeap<Vertex<TKey>> priorityQueue = new FibonacciHeap<>();
    Map<Vertex<TKey>, FibonacciHeap.Entry<Vertex<TKey>>> priorityQueueEntries = new HashMap<>();
    Map<Vertex<TKey>, Long> distances = new HashMap<>();

    Iterator<Vertex<TKey>> vertexesIterator = graph.getVertexesIterator();
    while (vertexesIterator.hasNext()) {
      Vertex<TKey> vertex = vertexesIterator.next();
      priorityQueueEntries.put(vertex, priorityQueue.enqueue(vertex, Long.MAX_VALUE));
    }

    priorityQueue.decreaseKey(priorityQueueEntries.get(start), 0);

    while (!priorityQueue.isEmpty()) {
      FibonacciHeap.Entry<Vertex<TKey>> curr = priorityQueue.dequeueMin();

      distances.put(curr.getValue(), curr.getPriority());

      Iterator<WeightedEdge<TKey>> incidentIterator = graph.getAdjacentByVertexIterator(curr.getValue());
      while (incidentIterator.hasNext()) {

        WeightedEdge<TKey> edge = incidentIterator.next();

        if (distances.containsKey(edge.getVertexTo())) {
          continue;
        }

        long newDist = curr.getPriority() + edge.getWeight();

        FibonacciHeap.Entry<Vertex<TKey>> dest = priorityQueueEntries.get(edge.getVertexTo());
        if (newDist < dest.getPriority()) {
          priorityQueue.decreaseKey(dest, newDist);
        }
      }
    }

    return distances;
  }

  // Algorithm based on implementaion by Keith Schwarz (htiek@cs.stanford.edu)
  // (http://keithschwarz.com/interesting)
  public static <TKey> Map<Vertex<TKey>, Long> bellmanFord(EdgesListGraph<TKey> graph, Vertex<TKey> start) {
    /*
     * Construct a map from the nodes to their distances, then populate it
     * with the initial value of the recurrence (the source is at distance
     * zero from itself; all other nodes are at infinite distance).
     */
    Map<Vertex<TKey>, Long> result = new HashMap<>();

    Iterator<Vertex<TKey>> vertexesIterator = graph.getVertexesIterator();
    int vertexCount = 0;
    while (vertexesIterator.hasNext()) {
      Vertex<TKey> vertex = vertexesIterator.next();
      result.put(vertex, null);
      vertexCount++;
    }
    result.put(start, Long.valueOf(0));

    /*
     * Create a new map that acts as scratch space. We'll flip back and
     * forth between the result map and this map during each iteration of
     * the algortihm so that we avoid needlessly reallocating maps.
     */
    Map<Vertex<TKey>, Long> scratch = new HashMap<>();

    /*
     * Starting with k = 1, compute the new values for the distances by
     * evaluating the recurrence.
     */
    for (int k = 1; k <= vertexCount; ++k) {
      /*
       * Begin by guessing that each node in this new iteration will have
       * a cost equal to its cost on the previous iteration.
       */
      scratch.putAll(result);

      /*
       * Scan across all the edges in the graph, updating the costs of
       * the paths of the nodes at their endpoints.
       */
      Iterator<WeightedEdge<TKey>> edgesIterator = graph.getWeightedEdgesIterator();
      while (edgesIterator.hasNext()) {
        WeightedEdge<TKey> edge = edgesIterator.next();
        /*
         * The new cost of the shortest path to this node is no
         * greater than the cost of the shortest path to the nodes'
         * neighbor plus the cost of the edge from that neighbor
         * into this node.
         */
        Long storedVal = scratch.get(edge.getVertexTo());
        Long resultVal = result.get(edge.getVertexFrom());
        if (resultVal != null) {
          if (storedVal == null)
            scratch.put(edge.getVertexTo(), edge.getWeight() + resultVal);
          else
            scratch.put(edge.getVertexTo(), Math.min(storedVal, edge.getWeight() + resultVal));
        }
      }

      /*
       * Finally, exchange the scratch buffer holding the new result with
       * the result map holding last iteration's results.
       */
      Map<Vertex<TKey>, Long> temp = result;
      result = scratch;
      scratch = temp;
    }

    /* Finally, report the distances. */
    return result;
  }

  // modifies the original graph
  public static <TKey> WeightedAdjacencyMatrix<TKey> floydWarshall(WeightedAdjacencyMatrix<TKey> graph) {

    Iterator<Vertex<TKey>> kIterator = graph.getVertexesIterator();
    
    while (kIterator.hasNext()) {
      Vertex<TKey> k = kIterator.next();
      
      Iterator<Vertex<TKey>> iIterator = graph.getVertexesIterator();
      while (iIterator.hasNext()) {
        Vertex<TKey> i = iIterator.next();
        
        Iterator<Vertex<TKey>> jIterator = graph.getVertexesIterator();
        while (jIterator.hasNext()) {
          Vertex<TKey> j = jIterator.next();

          System.out.println(k);
          System.out.println(i);
          System.out.println(j);
          System.out.println();

          if (graph.getWeight(i, k) == Long.MAX_VALUE) {
            continue;
          }
          if (graph.getWeight(k, j) == Long.MAX_VALUE) {
            continue;
          }

          long oldDist = graph.getWeight(i, j);
          long newDist = graph.getWeight(i, k) + graph.getWeight(k, j);

          if (newDist < oldDist) {
            graph.setWeight(i, j, newDist);
          }
        }
      }
    }

    return graph;
  }

}

