import java.io.*;
import java.util.*;

class dfsGraph {
  private HashMap<Integer, Node> nodeLookup = new HashMap<Integer, Node>();

  class Node {
      // it doesnt matter if the following variables are private
      // cos the outer class can access them regardless
      private int value;
      List<Node> adjacent = new ArrayList<Node>();

      private Node(int value) {
        this.value = value;
      }
  }

  public void addNode(int value) {
    nodeLookup.put(value, new Node(value));
  }

  private Node getNode(int value) {
    return nodeLookup.get(value);
  }

  public void connectNodes(int s, int d) {
    Node source = getNode(s);
    Node destination = getNode(d);
    source.adjacent.add(destination);
    // destination.add(source);
  }

  public Boolean checkPath(int s, int d) {
    HashSet<Integer> visited = new HashSet<Integer>();

    return dfs(getNode(s), getNode(d), visited);
  }

  private Boolean dfs(Node s, Node d, HashSet visited) {
    if (visited.contains(s.value)) {
      return false;
    }

    if (s == d) {
      return true;
    }

    visited.add(s.value);

    for (Node n: s.adjacent) {
      if (dfs(n, d, visited)) {
        return true;
      }
    }

    return false;
  }

}

public class dfs {
  public static void main(String[] args) {
    dfsGraph graph = new dfsGraph();
    graph.addNode(1);
    graph.addNode(2);
    graph.addNode(3);
    graph.addNode(4);
    graph.addNode(5);
    graph.connectNodes(1, 2);
    graph.connectNodes(1, 3);
    graph.connectNodes(3, 4);
    System.out.println(graph.checkPath(1, 5));
  }
}
