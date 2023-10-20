package Structures.Graphs;

import java.util.Objects;

public class Edge<TKey> {

  private Vertex<TKey> vertexFrom;
  private Vertex<TKey> vertexTo;

  public Edge(Vertex<TKey> vertexFrom, Vertex<TKey> vertexTo) {
    this.vertexFrom = vertexFrom;
    this.vertexTo = vertexTo;
  }

  public Vertex<TKey> getVertexFrom() {
    return vertexFrom;
  }

  public Vertex<TKey> getVertexTo() {
    return vertexTo;
  }

  @Override
  public int hashCode() {
    return Objects.hash(vertexFrom, vertexTo);
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    @SuppressWarnings("unchecked")
    Edge<TKey> other = (Edge<TKey>) obj;
    if (vertexFrom == null) {
      if (other.vertexFrom != null)
        return false;
    } else if (!vertexFrom.equals(other.vertexFrom))
      return false;
    if (vertexTo == null) {
      if (other.vertexTo != null)
        return false;
    } else if (!vertexTo.equals(other.vertexTo))
      return false;
    return true;
  }

  @Override
  public String toString() {
    return String.format("Edge[vertexFrom=%s, vertexTo=%s]", vertexFrom, vertexTo);
  }

}
