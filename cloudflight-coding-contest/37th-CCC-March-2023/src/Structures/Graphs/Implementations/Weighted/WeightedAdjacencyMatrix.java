package Structures.Graphs.Implementations.Weighted;

import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import Structures.Graphs.Edge;
import Structures.Graphs.Vertex;
import Structures.Graphs.WeightedEdge;
import Structures.Graphs.WeightedGraph;

public class WeightedAdjacencyMatrix<TKey> implements WeightedGraph<TKey> {

  // TODO use BiMap instead of two maps
  private Map<Vertex<TKey>, Integer> vertexToIndex; // vertex to index
  private Map<Integer, Vertex<TKey>> indexToVertex; // index to vertex

  private long[][] matrix;

  public WeightedAdjacencyMatrix(Set<Vertex<TKey>> vertexes) {

    this.vertexToIndex = new HashMap<>();
    this.indexToVertex = new HashMap<>();

    int vertexNumber = vertexes.size();

    this.matrix = new long[vertexNumber][vertexNumber];
    
    for (int i = 0; i < vertexNumber; i++) {
      for (int j = 0; j < vertexNumber; j++) {
        if (i == j) {
          this.matrix[i][j] = 0;
        } else {
          this.matrix[i][j] = Long.MAX_VALUE;
        }
      }
    }
    //TODO matrixelement internal class mutable wrapper for long type
    int i = 0;
    for (Vertex<TKey> vertex : vertexes) {
      vertexToIndex.put(vertex, i);
      indexToVertex.put(i, vertex);
      i++;
    }

  }

  public long getWeight(Vertex<TKey> from, Vertex<TKey> to) {
    int indexFrom = vertexToIndex.get(from);
    int indexTo = vertexToIndex.get(to);

    return matrix[indexFrom][indexTo];
  }

  public void setWeight(Vertex<TKey> from, Vertex<TKey> to, long weight) {
    int indexFrom = vertexToIndex.get(from);
    int indexTo = vertexToIndex.get(to);

    matrix[indexFrom][indexTo] = weight;
  }

  public void removeWeight(Vertex<TKey> from, Vertex<TKey> to) {
    int indexFrom = vertexToIndex.get(from);
    int indexTo = vertexToIndex.get(to);

    matrix[indexFrom][indexTo] = Long.MAX_VALUE;
  }

  @Override
  public Iterator<Vertex<TKey>> getVertexesIterator() {
    return Collections.unmodifiableCollection(vertexToIndex.keySet()).iterator();
  }

  @Override
  public Iterator<Edge<TKey>> getEdgesIterator() {

    Set<Edge<TKey>> edges = new HashSet<>();

    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix.length; j++) {
        // TODO adds edges duplicated?
        edges.add(new Edge<>(indexToVertex.get(i), indexToVertex.get(j)));
      }
    }

    return Collections.unmodifiableCollection(edges).iterator();
  }

  @Override
  public Vertex<TKey> findVertex(TKey key) {

    for (Vertex<TKey> vertex : vertexToIndex.keySet()) {
      if (vertex.getKey().equals(key)) {
        return vertex;
      }
    }

    return null;
  }

  @Override
  public WeightedEdge<TKey> findEdge(TKey keyFrom, TKey keyTo) {
    Vertex<TKey> vertexFrom = new Vertex<TKey>(keyFrom);
    Vertex<TKey> vertexTo = new Vertex<TKey>(keyTo);

    if (!(vertexToIndex.containsKey(vertexFrom))) {
      return null;
    }
    if (!(vertexToIndex.containsKey(vertexTo))) {
      return null;
    }

    int indexFrom = vertexToIndex.get(vertexFrom);
    int indexTo = vertexToIndex.get(vertexTo);

    if (matrix[indexFrom][indexTo] != Long.MAX_VALUE) {
      return new WeightedEdge<>(vertexFrom, vertexTo, matrix[indexFrom][indexTo]);
    }

    return null;
  }

  @Override
  public Iterator<WeightedEdge<TKey>> getWeightedEdgesIterator() {
    
    Set<WeightedEdge<TKey>> edges = new HashSet<>();

    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix.length; j++) {
        // TODO adds edges duplicated?
        edges.add(new WeightedEdge<>(indexToVertex.get(i), indexToVertex.get(j), matrix[i][j]));
      }
    }

    return Collections.unmodifiableCollection(edges).iterator();
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append(vertexToIndex.toString());
    sb.append('\n');
    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] != Long.MAX_VALUE) {
          sb.append(matrix[i][j]);
        } else {
          sb.append("inf");
        }
        sb.append('\t');
      }
      sb.append('\n');
    }
    return sb.toString();
  }  

}
