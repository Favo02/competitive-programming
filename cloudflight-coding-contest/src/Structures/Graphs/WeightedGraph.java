package Structures.Graphs;

import java.util.Iterator;

public interface WeightedGraph<TKey> extends Graph<TKey> {

  @Override
  public WeightedEdge<TKey> findEdge(TKey keyFrom, TKey keyTo);

  public Iterator<WeightedEdge<TKey>> getWeightedEdgesIterator();

}
