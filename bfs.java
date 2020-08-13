import java.io.*;
import java.util.*;

class Graph {
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
    return bfs(getNode(s), getNode(d));
  }

  private Boolean bfs(Node s, Node d) {
    LinkedList<Node> nextToVisit = new LinkedList<Node>();
    HashSet<Integer> visited = new HashSet<Integer>();

    nextToVisit.add(s);

    while (!nextToVisit.isEmpty()) {
      Node current = nextToVisit.poll();

      if (visited.contains(current.value)) {
        continue;
      }

      if (current == d) {
        return true;
      }

      visited.add(current.value);

      for (Node n: current.adjacent) {
        nextToVisit.add(n);
      }
    }

    return false;
  }
}

public class bfs {
  public static void main(String[] args) {
    Graph graph = new Graph();
    graph.addNode(1);
    graph.addNode(2);
    graph.addNode(3);
    graph.addNode(4);
    graph.addNode(5);
    graph.connectNodes(1, 2);
    graph.connectNodes(1, 3);
    graph.connectNodes(3, 4);
    System.out.println(graph.checkPath(1, 4));
  }
}
