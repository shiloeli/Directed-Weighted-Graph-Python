package test;

import Classes.DWGraph_Algo;
import Classes.DWGraph_DS;
import Classes.NodeData;
import api.directed_weighted_graph;
import api.dw_graph_algorithms;
import api.edge_data;
import api.node_data;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Test_Java_VS_Python {

    @Test
    public void test_shortest_path() {
        dw_graph_algorithms wga = new DWGraph_Algo();
//        int limit1 = 0;
        wga.load("data/G_10_80_0.json");
        wga.shortestPathDist(0, 1);
        System.out.println("Graph G_10_80_0 done!");
////        for (node_data n : wga.getGraph().getV()) {
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
//
        wga.load("data/G_100_800_0.json");
        wga.shortestPathDist(0, 1);
        System.out.println("Graph G_100_800_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            if (limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            } else {
////                break;
////            }
////        }
//
        wga.load("data/G_1000_8000_0.json");
        wga.shortestPathDist(0, 1);
        System.out.println("Graph G_1000_8000_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
//
        wga.load("data/G_10000_80000_0.json");
        wga.shortestPathDist(0, 1);
        System.out.println("Graph G_10000_80000_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            limit1 += 1;
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
//
        wga.load("data/G_20000_160000_0.json");
        wga.shortestPathDist(0, 1);
        System.out.println("Graph G_20000_160000_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            limit1 += 1;
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
////        System.out.println("limit is: "+limit1);
////
        wga.load("data/G_30000_240000_0.json");
        wga.shortestPathDist(0, 1);
        System.out.println("Graph G_30000_240000_0 done!");
//
//        for (node_data n : wga.getGraph().getV()) {
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
//
//        wga.load("data/G_100_800_0.json");
//        wga.shortestPathDist(0, 1);
//        System.out.println("Graph G_100_800_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            if (limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            } else {
////                break;
////            }
////        }
//
//        wga.load("data/G_1000_8000_0.json");
//        wga.shortestPathDist(0, 1);
//        System.out.println("Graph G_1000_8000_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
//
//        wga.load("data/G_10000_80000_0.json");
//        wga.shortestPathDist(0, 1);
//        System.out.println("Graph G_10000_80000_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            limit1 += 1;
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
//
//        wga.load("data/G_20000_160000_0.json");
//        wga.shortestPathDist(0, 1);
//        System.out.println("Graph G_20000_160000_0 done!");
////        limit1 = 0;
////        for (node_data n : wga.getGraph().getV()) {
////            limit1 += 1;
////            if(limit1 < 100) {
////                wga.shortestPathDist(0, n.getKey());
////            }else{
////                break;
////            }
////        }
////        System.out.println("limit is: "+limit1);
////
//        wga.load("data/G_30000_240000_0.json");
//        wga.shortestPathDist(0, 1);
//        System.out.println("Graph G_30000_240000_0 done!");
//        limit1 = 0;
//        for (node_data n : wga.getGraph().getV()) {
//            limit1 += 1;
//            if(limit1 < 100) {
//                wga.shortestPathDist(0, n.getKey());
//            }else{
//                break;
//            }
//        }
//        System.out.println("limit is: "+limit1);
//        System.out.println("Graph G_30000_240000_0 done!");

//        -------------------------------------------
//        wga.load("data/A0");
//        for (node_data n : wga.getGraph().getV()) {
//            for (node_data n1 : wga.getGraph().getV()) {
////                System.out.println("shortest_path between " + n.getKey() + " to " + n1.getKey() + ":" + wga.shortestPathDist(n.getKey(), n1.getKey()));
//                wga.shortestPathDist(n.getKey(), n1.getKey());
//            }
//        }
//        System.out.println("Graph A0 done!");
//
//        wga.load("data/A1");
//        for (node_data n : wga.getGraph().getV()) {
//            for (node_data n1 : wga.getGraph().getV()) {
//                wga.shortestPathDist(n.getKey(), n1.getKey());
//            }
//        }
//        System.out.println("Graph A1 done!");
//
//        wga.load("data/A2");
//        for (node_data n : wga.getGraph().getV()) {
//            for (node_data n1 : wga.getGraph().getV()) {
//                wga.shortestPathDist(n.getKey(), n1.getKey());
//            }
//        }
//        System.out.println("Graph A2 done!");
//
//        wga.load("data/A3");
//        for (node_data n : wga.getGraph().getV()) {
//            for (node_data n1 : wga.getGraph().getV()) {
//                wga.shortestPathDist(n.getKey(), n1.getKey());
//            }
//        }
//        System.out.println("Graph A3 done!");
//
//        wga.load("data/A4");
//        for (node_data n : wga.getGraph().getV()) {
//            for (node_data n1 : wga.getGraph().getV()) {
//                wga.shortestPathDist(n.getKey(), n1.getKey());
//            }
//        }
//        System.out.println("Graph A4 done!");
//
//        wga.load("data/A5");
//        for (node_data n : wga.getGraph().getV()) {
//            for (node_data n1 : wga.getGraph().getV()) {
//                wga.shortestPathDist(n.getKey(), n1.getKey());
//            }
//        }
//        System.out.println("Graph A5 done!");
//
//        wga.load("data/A5");
//        for (node_data n : wga.getGraph().getV()) {
//            for (node_data n1 : wga.getGraph().getV()) {
//                wga.shortestPathDist(n.getKey(), n1.getKey());
//            }
//        }
//        System.out.println("Graph A5 done!");

    }

    @Test
    public void test_connectedComponent() {
        DWGraph_Algo ga = new DWGraph_Algo();
        List<Integer> expected;
        List<Integer> actual;
        ga.load("data/G_10_80_0.json");
        expected = new ArrayList<>();
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.add(i);
        }
        actual = ga.connectedComponent(0);
        assertEquals(expected, actual);

        ga.load("data/G_100_800_0.json");
        expected = new ArrayList<>();
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.add(i);
        }
        actual = ga.connectedComponent(0);
        assertEquals(expected, actual);

        ga.load("data/G_1000_8000_0.json");
        expected = new ArrayList<>();
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.add(i);
        }
        actual = ga.connectedComponent(0);
        assertEquals(expected, actual);

        ga.load("data/G_10000_80000_0.json");
        expected = new ArrayList<>();
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.add(i);
        }
        actual = ga.connectedComponent(0);
        assertEquals(9989, actual.size());

        ga.load("data/G_20000_160000_0.json");
        expected = new ArrayList<>();
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.add(i);
        }
        actual = ga.connectedComponent(0);
        assertEquals(19985, actual.size());

        ga.load("data/G_30000_240000_0.json");
        expected = new ArrayList<>();
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.add(i);
        }
        actual = ga.connectedComponent(0);
        assertEquals(29971, actual.size());
    }

    @Test
    public void test_connectedComponents() {
        DWGraph_Algo ga = new DWGraph_Algo();
        List<List<Integer>> expected;
        List<List<Integer>> actual;

        ga.load("data/G_10_80_0.json");
        expected = new ArrayList<>();
        expected.add(new ArrayList<>());
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.get(0).add(i);
        }
        actual = ga.connectedComponents();
        assertEquals(expected, actual);

        ga.load("data/G_100_800_0.json");
        expected = new ArrayList<>();
        expected.add(new ArrayList<>());
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.get(0).add(i);
        }
        actual = ga.connectedComponents();
        assertEquals(expected, actual);

        ga.load("data/G_1000_8000_0.json");
        expected = new ArrayList<>();
        expected.add(new ArrayList<>());
        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
            expected.get(0).add(i);
        }
        actual = ga.connectedComponents();
        assertEquals(expected, actual);

        ga.load("data/G_10000_80000_0.json");
        actual = ga.connectedComponents();
        assertEquals(12, actual.size());

        ga.load("data/G_20000_160000_0.json");
        actual = ga.connectedComponents();
        assertEquals(16, actual.size());

        ga.load("data/G_30000_240000_0.json");
        actual = ga.connectedComponents();
        assertEquals(30, actual.size());

//        ga.load("data/A0");
//        List<List<Integer>> expected = new ArrayList<>();
//        expected.add(new ArrayList<>());
//        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
//            expected.get(0).add(i);
//        }
//        List<List<Integer>> actual = ga.connectedComponents();
//        assertEquals(expected, actual);
//
//        ga.load("data/A1");
//        expected = new ArrayList<>();
//        expected.add(new ArrayList<>());
//        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
//            expected.get(0).add(i);
//        }
//        actual = ga.connectedComponents();
//        assertEquals(expected, actual);
//
//        ga.load("data/A2");
//        expected = new ArrayList<>();
//        expected.add(new ArrayList<>());
//        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
//            expected.get(0).add(i);
//        }
//        actual = ga.connectedComponents();
//        assertEquals(expected, actual);
//
//        ga.load("data/A3");
//        expected = new ArrayList<>();
//        expected.add(new ArrayList<>());
//        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
//            expected.get(0).add(i);
//        }
//        actual = ga.connectedComponents();
//        assertEquals(expected, actual);
//
//        ga.load("data/A4");
//        expected = new ArrayList<>();
//        expected.add(new ArrayList<>());
//        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
//            expected.get(0).add(i);
//        }
//        actual = ga.connectedComponents();
//        assertEquals(expected, actual);
//
//        ga.load("data/A5");
//        expected = new ArrayList<>();
//        expected.add(new ArrayList<>());
//        for (int i = 0; i < ga.getGraph().nodeSize(); i++) {
//            expected.get(0).add(i);
//        }
//        actual = ga.connectedComponents();
//        assertEquals(expected, actual);

    }

    @Test
    public void test_simple_connectedComponent() {
        directed_weighted_graph g = new DWGraph_DS();
        g.addNode(new NodeData(1));
        g.addNode(new NodeData(2));
        g.addNode(new NodeData(3));
        g.addNode(new NodeData(4));
        g.addNode(new NodeData(5));

        g.connect(1, 2, 1);
        g.connect(2, 3, 1);
        g.connect(3, 1, 1);
        g.connect(3, 4, 1);
        g.connect(4, 5, 1);

        DWGraph_Algo ga = new DWGraph_Algo();
        ga.init(g);

        List<Integer> component = ga.connectedComponent(4);
        System.out.println(component);
        System.out.println(ga.connectedComponents());
    }

    @Test
    public void test_100_vertices() {
        directed_weighted_graph g = graph_creator(100, 100);
        assertEquals(g.nodeSize(), 100);
    }

    @Test
    public void test_10000_vertices() {
        directed_weighted_graph g = graph_creator(10000, 10000);
        assertEquals(g.nodeSize(), 10000);
    }

    @Test
    public void test_1000000_vertices() {
        directed_weighted_graph g = graph_creator(1000000, 1000000);
        assertEquals(g.nodeSize(), 1000000);
    }

    @Test
    public void test_10000000_vertices() {
        directed_weighted_graph g = graph_creator(1000000, 10000000);
        assertEquals(g.nodeSize(), 1000000);
    }

    public static directed_weighted_graph graph_creator(int v_size, int e_size) {
        directed_weighted_graph g = new DWGraph_DS();
        for (int i = 0; i < v_size; i++) {
            g.addNode(new NodeData(i));
        }

        for (int i = 0; i < v_size; i++) {
            for (int j = 1; j < v_size; j++) {
                if (g.edgeSize() < e_size) {
                    g.connect(i, j, 4);
                }
            }
            if (g.edgeSize() >= e_size) {
                break;
            }
        }

        return g;
    }
}
