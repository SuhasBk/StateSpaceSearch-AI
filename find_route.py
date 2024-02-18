#!/usr/local/bin/python3
import sys
from enum import Enum
from collections import defaultdict
from heapq import heappop, heappush

class StateSpaceSearch:

    '''Strategy definition'''
    class Strategy(Enum):
        UNINFORMED = 'UCS'
        INFORMED = 'A*'

    '''Constructor to initialize graph from input file and choose strategy based on arguments'''
    def __init__(self, input_file_path, source, destination, heuristic_file_path):    
        self.input_file_path = input_file_path
        self.heuristic_file_path = heuristic_file_path    
        self.start = source
        self.goal = destination
        self.strategy = self.Strategy.INFORMED if heuristic_file_path else self.Strategy.UNINFORMED

        self.graph = self.read_graph_from_file(input_file_path)
    
    '''Convert input file to a graph represented as a dictionary of lists, 
    where each key is a node and the value is a list of tuples 
    indicating (child node, step cost)'''
    def read_graph_from_file(self, input_file_path):
        graph = defaultdict(list)
        
        input_file = None
        try:
            input_file = open(input_file_path, "r")
        except FileNotFoundError:
            raise FileNotFoundError("\n\nPlease make sure INPUT file exists before running the program!\n")

        while True:
            curr_line = input_file.readline()
            
            if not curr_line or curr_line.startswith("END OF INPUT"):
                break
            
            source, dest, cost = curr_line.split()
            cost = int(cost)
            graph[source].append((dest, cost))
            graph[dest].append((source, cost))

        if self.start not in graph or self.goal not in graph:
            print(f"Nodes Popped: {0}\nNodes Expanded: {0}\nNodes Generated: {0}\nDistance: Infinity\nRoute:\nNone")
            exit()

        return graph

    '''Convert heuristic file to a dictionary with node as key and expected cost from any node to that node as value'''
    def read_heuristic_from_file(self, heuristic_file_path):
        self.heuristic = {}

        heuristic_file = None
        try:
            heuristic_file = open(heuristic_file_path, "r")
        except FileNotFoundError:
            raise FileNotFoundError("\n\nPlease make sure HEURISTIC file exists before running the program!\n")

        while True:
            curr_line = heuristic_file.readline()
            
            if not curr_line or curr_line.startswith("END OF INPUT"):
                break
            
            node, cost = curr_line.split()
            cost = int(cost)
            self.heuristic[node] = cost

        return self.heuristic

    '''Utility function to prettify path'''
    def print_path(self, path):
        s = f"\n"
        prev = path[0]
        for i in range(1, len(path)):
            node, dist = path[i].split()
            dist = dist[1:len(dist)-1]
            s += f"{prev} to {node}, {float(dist)} km\n"
            prev = node
        return s.rstrip()

    '''
    Uninformed Uniform Cost Search which only considers g(n) while popping nodes from the fringe
    '''
    def UCS(self):
        expanded = 0
        generated = 1
        popped = 0
        # fringe order based on: g(n) only
        node = (0, self.start, [self.start])
        fringe = [node]
        explored = set()

        while fringe:
            cost, node, path = heappop(fringe)
            # print(node, cost, list(map(lambda x: (x[0], x[1]), fringe)),'\n')
            popped += 1

            if node == self.goal:
                print(f"Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: {float(cost)} km\nRoute: {self.print_path(path)}")
                return True
        
            if node not in explored:
                explored.add(node)
                expanded += 1

                for successor in self.graph[node]:
                    generated += 1
                    child, step_cost = successor
                    cost_so_far = step_cost + cost
                    heappush(fringe, (cost_so_far, child, path + [child + ' (' + str(step_cost) + ')']))
        
        print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: Infinity\nRoute:\nNone''')
        return False

    '''
    Informed A* search which takes heuristic - h(n) (expected cost) into consideration while expanding nodes.
    '''
    def A_star(self):
        heuristic = self.read_heuristic_from_file(self.heuristic_file_path)
        expanded = 0
        generated = 1
        popped = 0
        # fringe order based on: f(n) = g(n) + h(n)
        node = (0 + heuristic[self.start], self.start, [self.start])
        fringe = [node]
        explored = set()

        while fringe:
            cost, node, path = heappop(fringe)
            # print(node, cost, list(map(lambda x: (x[0], x[1]), fringe)),'\n')
            popped += 1

            if node == self.goal:
                print(f"Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: {float(cost)} km\nRoute: {self.print_path(path)}")
                return True
        
            if node not in explored:
                explored.add(node)
                expanded += 1

                for successor in self.graph[node]:
                    generated += 1
                    child, step_cost = successor
                    cost_so_far = step_cost + heuristic[child] + cost - heuristic[node]
                    heappush(fringe, (cost_so_far, child, path + [child + ' (' + str(step_cost) + ')']))
        
        print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: Infinity\nRoute:\nNone''')
        return False
    
    '''Find route based on strategy'''
    def find_route(self):
        self.UCS() if self.strategy == self.Strategy.UNINFORMED else self.A_star()  


'''Program entrypoint'''
if __name__ == '__main__':
    # check for consistency of arguments
    n = len(sys.argv)
    if n < 4:
        raise IndexError("\n\nPlease follow this format: python find_route.py <input_file>* <source>* <destination>* <heuristic_file>\n")
    
    # unpack arguments
    input_file_path = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]
    heuristic_file_path = sys.argv[4] if n >= 5 else None

    # initialize state space search object with strategy
    stateSpaceSearch = StateSpaceSearch(input_file_path, source, destination, heuristic_file_path)

    # find route between source and destination
    stateSpaceSearch.find_route()