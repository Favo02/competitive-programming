package Structures.Graphs;

import java.util.Objects;

public class WeightedEdge<TKey> extends Edge<TKey> implements Comparable<WeightedEdge<TKey>> {

  private long weight;

  public WeightedEdge(Vertex<TKey> vertexFrom, Vertex<TKey> vertexTo, long weight) {
    super(vertexFrom, vertexTo);
    this.weight = weight;
  }

  public long getWeight() {
    return weight;
  }

  @Override
  public int hashCode() {
    return Objects.hash(super.hashCode(), weight);
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (!super.equals(obj))
      return false;
    if (getClass() != obj.getClass())
      return false;
    @SuppressWarnings("unchecked")
    WeightedEdge<TKey> other = (WeightedEdge<TKey>) obj;
    if (weight != other.weight)
      return false;
    return true;
  }

  @Override
  public String toString() {
    return String.format("Edge[vertexFrom=%s, vertexTo=%s, weight=%s]", getVertexFrom(), getVertexTo(), weight);
  }

  @Override
  public int compareTo(WeightedEdge<TKey> other) {
    return Long.compare(this.weight, other.weight);
  }

}
