def UCS(self):
    expanded = 0
    generated = 1
    popped = 0
    node = (0, self.start, [self.start])
    frontier = [node]
    explored = set()
    route_exists = False

    while frontier:
        curr, cost, path = min(frontier, key=lambda x: x[1])
        # print(curr, cost, list(map(lambda x: (x[1], x[0]), fringe)),'\n')
        frontier.remove((curr, cost, path))
        popped += 1

        if curr == self.goal:
            route_exists = True
            print(popped, expanded, generated, cost, ' -> '.join(path))
            break
        
        explored.add(curr)
        expanded += 1
        
        for action in self.graph[curr]:
            generated += 1
            child, step_cost = action
            if child not in explored and child not in map(lambda x: x[0], frontier):
                frontier.append((child, cost + step_cost, path + [child + ' (' + str(step_cost) + ')']))
            elif child in map(lambda x: x[0], frontier):
                fringe_child = list(filter(lambda x: x[0] == child, frontier))[0]
                if fringe_child[1] > cost + step_cost:
                    frontier.remove(fringe_child)
                    frontier.append((child, cost + step_cost, path + [child + ' (' + str(step_cost) + ')']))
    
    if not route_exists:
        print(popped, expanded, generated)
    return None

def A_star(self):
    heuristics = self.read_heuristic_from_file(self.heuristic_file_path)
    expanded = 0
    generated = 1
    popped = 0
    node = (self.start, 0, [self.start])
    frontier = [node]
    explored = set()

    while frontier:
        curr, cost, path = min(frontier, key=lambda x: x[1] + heuristics[x[0]])
        print(curr, cost, list(map(lambda x: (x[1], x[0]), frontier)),'\n')
        frontier.remove((curr, cost, path))
        popped += 1

        if curr == self.goal:
            print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: {float(cost)} km\nRoute: {' -> '.join(path)}''')
            return True
        
        explored.add(curr)
        expanded += 1
        
        for action in self.graph[curr]:
            generated += 1
            child, step_cost = action
            if child not in explored and child not in map(lambda x: x[0], frontier):
                frontier.append((child, cost + step_cost, path + [child + ' (' + str(step_cost) + ')']))
            elif child in map(lambda x: x[0], frontier):
                fringe_child = list(filter(lambda x: x[0] == child, frontier))[0]
                if fringe_child[1] > cost + step_cost:
                    frontier.remove(fringe_child)
                    frontier.append((child, cost + step_cost, path + [child + ' (' + str(step_cost) + ')']))
    
    print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: Infinity\nRoute:\nNone''')
    return False

    # heuristics = self.read_heuristic_from_file(self.heuristic_file_path)
    # expanded = 0
    # generated = 1
    # popped = 0
    # node = (self.start, 0, [self.start])
    # fringe = [node]
    # explored = set()

    # while fringe:
    #     curr, cost, path = min(fringe, key=lambda x: x[1] + heuristics[x[0]])
    #     # print(curr, cost, list(map(lambda x: (x[1], x[0]), fringe)),'\n')
    #     fringe.remove((curr, cost, path))
    #     popped += 1

    #     if curr == self.goal:
    #         print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: {float(cost)} km\nRoute: {self.print_path(path)}''')
    #         return True
        
    #     explored.add(curr)
    #     expanded += 1
        
    #     for action in self.graph[curr]:
    #         generated += 1
    #         child, step_cost = action
    #         if child not in explored and child not in map(lambda x: x[0], fringe):
    #             fringe.append((child, cost + step_cost, path + [child + ' (' + str(step_cost) + ')']))
    #         elif child in map(lambda x: x[0], fringe):
    #             fringe_child = list(filter(lambda x: x[0] == child, fringe))[0]
    #             if fringe_child[1] > cost + step_cost:
    #                 fringe.remove(fringe_child)
    #                 fringe.append((child, cost + step_cost, path + [child + ' (' + str(step_cost) + ')']))
    
    # print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: Infinity\nRoute:\nNone''')
    # return False

    # heuristic = self.read_heuristic_from_file(self.heuristic_file_path)
    # expanded = 0
    # generated = 1
    # popped = 0
    # node = (0, self.start, [self.start], 0)
    # frontier = [node]
    # explored = set()

    # while frontier:
    #     cost, curr, path, distance = heappop(frontier)
    #     print(curr, cost, list(map(lambda x: (x[1], x[0]), frontier)),'\n')
    #     popped += 1

    #     if curr == self.goal:
    #         # print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: {distance} km\nRoute: {self.print_path(path)}''')
    #         print(popped, expanded, generated, distance, path)
    #         return True
        
    #     if curr not in explored:
    #         explored.add(curr)
    #         expanded += 1

    #         for successor in self.graph[curr]:
    #             generated += 1
    #             child, step_cost = successor
    #             if child not in explored:
    #                 total_cost = step_cost + heuristic.get(child, float('inf'))
    #                 heappush(frontier, (total_cost, child, path + [child + ' (' + str(step_cost) + ')'], distance + step_cost))
    
    # print(f'''Nodes Popped: {popped}\nNodes Expanded: {expanded}\nNodes Generated: {generated}\nDistance: Infinity\nRoute:\nNone''')
    # return False