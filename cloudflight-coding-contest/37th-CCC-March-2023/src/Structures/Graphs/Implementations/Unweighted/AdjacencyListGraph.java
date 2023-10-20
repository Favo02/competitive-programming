package Structures.Graphs.Implementations.Unweighted;

import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import Structures.Graphs.Edge;
import Structures.Graphs.Graph;
import Structures.Graphs.Vertex;

public class AdjacencyListGraph<TKey> implements Graph<TKey> {

  private Map<Vertex<TKey>, Set<Vertex<TKey>>> adjacencyList;

  public AdjacencyListGraph() {
    this.adjacencyList = new HashMap<>();
  }

  public void addAdjacent(Vertex<TKey> from, Vertex<TKey> adjacent) {

    if (!adjacencyList.containsKey(from)) {
      adjacencyList.put(from, new HashSet<>());
    }

    adjacencyList.get(from).add(adjacent);
  }

  public void removeAdjacent(Vertex<TKey> from, Vertex<TKey> adjacent) {
    Set<Vertex<TKey>> fromHashSet = adjacencyList.get(from);
    if (fromHashSet == null) {
      throw new NullPointerException("from does not exist in the graph");
    }
    fromHashSet.remove(adjacent);
  }

  public Iterator<Vertex<TKey>> getAdjacentByVertexIterator(Vertex<TKey> from) {
    return Collections.unmodifiableCollection(adjacencyList.get(from)).iterator();
  }

  @Override
  public Iterator<Vertex<TKey>> getVertexesIterator() {
    return Collections.unmodifiableCollection(adjacencyList.keySet()).iterator();
  }

  @Override
  public Iterator<Edge<TKey>> getEdgesIterator() {

    Set<Edge<TKey>> edges = new HashSet<>();

    for (Vertex<TKey> from : adjacencyList.keySet()) {
      for (Vertex<TKey> to : adjacencyList.get(from)) {
        edges.add(new Edge<>(from, to));
      }
    }

    return Collections.unmodifiableCollection(edges).iterator();
  }

  @Override
  public Vertex<TKey> findVertex(TKey key) {

    for (Vertex<TKey> vertex : adjacencyList.keySet()) {
      if (vertex.getKey().equals(key)) {
        return vertex;
      }
    }

    return null;
  }

  @Override
  public Edge<TKey> findEdge(TKey keyFrom, TKey keyTo) {

    for (Vertex<TKey> from : adjacencyList.keySet()) {
      if (from.getKey().equals(keyFrom)) {
        for (Vertex<TKey> to : adjacencyList.get(from)) {
          if (to.getKey().equals(keyTo)) {
            return new Edge<TKey>(from, to);
          }
        }
      }
    }

    return null;
  }

  // TODO implement toString
}
