import sys

class Node:
    def __init__(self, parent, current, action):
        self.parent = parent
        self.current = current
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.empty():
            raise Exception("No solution exists.")
        else: # a temp node (last) then slice; first to last-1 (just before node) following STACK LIFO DFS
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
    
    def contains_state(self, state): #in frontier check if node/state is already present.
        return any(node.current == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("No solution exists.")
        else: # a temp node (first) then slice; second to last (just after node) following QUEUE FIFO BFS
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

    

class Visited:
    def __init__(self):
        self.visited = set()
    
    def add(self, node):
        self.visited.add(node.current)




class Maze():

    def __init__(self, filename):

        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")

        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()

        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []

        for i in range(self.height):

            row = []

            for j in range(self.width):

                try:

                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)

                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)

                    elif contents[i][j] == " ":
                        row.append(False)

                    else:
                        row.append(True)

                except IndexError:
                    row.append(False)

            self.walls.append(row)

        self.solution = None
        self.explored = set()
        self.num_explored = 0

    def print(self):

        solution = self.solution[1] if self.solution is not None else None

        print()
        # i is number of row (vertical position), row is list of columns (horizontal position)
        for i, row in enumerate(self.walls):
            # j is number of column, col is boolean value (wall ture or not)
            for j, col in enumerate(row): 

                if col:
                    print("█", end="")

                elif (i, j) == self.start:
                    print("A", end="")

                elif (i, j) == self.goal:
                    print("B", end="")

                elif solution is not None and (i, j) in solution:
                    print("*", end="")

                else:
                    print(" ", end="")

            print()

        print()

    def neighbors(self, state):

        row, col = state

        # All possible actions
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # Ensure actions are valid
        result = []

        for action, (r, c) in candidates:

            try:

                if not self.walls[r][c]:
                    result.append((action, (r, c)))

            except IndexError:
                continue

        return result


    def solve(self):
        start = Node(parent=None, current=self.start, action=None)
        # frontier = StackFrontier()
        frontier = QueueFrontier()
        frontier.add(start)

        self.explored = set()
        self.num_explored = 0

        while True:
            if frontier.empty():
                raise Exception("No solution")
            
            node = frontier.remove()
            self.num_explored += 1

            if node.current == self.goal: # condition if we found answer/goal
                actions = []
                cells = []
                while node.parent != None:
                    actions.append(node.action)
                    cells.append(node.current)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            
            self.explored.add(node.current)

            for action, state in self.neighbors(node.current):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(parent=node, current=state, action=action)
                    frontier.add(child)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")
    
    m = Maze(sys.argv[1])
    print("Maze:")
    m.print()

    m.solve()
    print(f"Solution found in {len(m.solution[0])} moves.")
    print(f"States explored: {m.num_explored}")
    print("Solution:")
    m.print()