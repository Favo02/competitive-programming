package Structures.Graphs;

import java.util.Iterator;

public interface Graph<TKey> {
  
  public Iterator<Vertex<TKey>> getVertexesIterator();

  public Iterator<Edge<TKey>> getEdgesIterator();

  public Vertex<TKey> findVertex(TKey key);

  public Edge<TKey> findEdge(TKey keyFrom, TKey keyTo);

}
