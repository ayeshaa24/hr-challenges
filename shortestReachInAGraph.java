import java.io.*;
import java.util.*;

// To create an instance of graph/node from static main
// it has to be a seperate class, not a nested class
// alt: just make them both static classes but meh....

}

class Node {
    int value;
    int distance;
    List<Node> adjacent;

    public Node(int val) {
        value = val;
        distance = -1;
        adjacent = new ArrayList<Node>();
    }
}

class Graph {
    List<Node> nodes = new ArrayList<Node>();

    public Graph(int m) {
        for (int i = 1; i < m + 1; i++) {
            nodes.add(new Node(i));
        }
    }

    public void connectGraph(int a, int b) {
        Node one = nodes.get(a);
        Node two = nodes.get(b);
        one.adjacent.add(two);
        two.adjacent.add(one);
    }

    public void getShortestReach(int s) {
        Node source = nodes.get(s);
        source.distance = 0;

        LinkedList<Node> needToVisit = new LinkedList<Node>();
        needToVisit.add(source);

        while (!needToVisit.isEmpty()) {
            Node current = needToVisit.poll();

            for (Node n: current.adjacent) {
                if (n.distance == -1) {
                    n.distance = current.distance + 6;
                    needToVisit.add(n);
                }
            }
        }


        for (Node n: nodes) {
            if (n != source) {
                System.out.print(n.distance + " ");
            }
        }

    }

}

public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);

        int q = scanner.nextInt();

        for (int i = 0; i < q; i++) {
            Graph graph = new Graph(scanner.nextInt());

            int m = scanner.nextInt();

            for (int j = 0; j < m; j++) {
                graph.connectGraph(scanner.nextInt()-1, scanner.nextInt()-1);
            }

            int s = scanner.nextInt() - 1;

            graph.getShortestReach(s);

            System.out.println();
        }
    }
}
