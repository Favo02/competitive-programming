package Structures.Graphs;

import java.util.Objects;

public class Vertex<TKey> {

  private TKey key;

  public Vertex(TKey key) {
    this.key = key;
  }

  public TKey getKey() {
    return key;
  }

  @Override
  public int hashCode() {
    return Objects.hash(key);
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
    Vertex<TKey> other = (Vertex<TKey>) obj;
    if (key == null) {
      if (other.key != null)
        return false;
    } else if (!key.equals(other.key))
      return false;
    return true;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("Vertex[key=");
    sb.append(key);
    sb.append("]");
    return sb.toString();
  }

}
