class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class Solver:
    WALL = 'W'
    PASSAGE = '.'

    def __init__(self, mz):
        maze = [list(line) for line in mz.splitlines()]
        self.maze_height = len(maze)
        self.maze_width = len(maze[0])
        print(f'{self.maze_height=}, {self.maze_width=}')

        if maze[0][0] == Solver.WALL:
            raise ValueError('Maze must have a starting point in the top left corner.')

        if maze[self.maze_height - 1][self.maze_width - 1] == Solver.WALL:
            raise ValueError('Maze must have an ending point in the bottom right corner.')

        self.maze_start = (0, 0)
        self.maze_goal = (self.maze_height - 1, self.maze_width - 1)

        self.maze_walls = []
        for h in range(self.maze_height):
            row = []
            for w in range(self.maze_width):
                try:
                    if maze[h][w] == Solver.WALL:
                        row.append(True)
                    else:
                        row.append(False)
                except IndexError:
                    row.append(False)
            self.maze_walls.append(row)

        self.explored = set()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.maze_height and 0 <= c < self.maze_width and not self.maze_walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve_maze(self):
        start = Node(self.maze_start, None, None)
        frontier = StackFrontier()
        frontier.add(start)

        while True:
            if frontier.empty():
                return False

            node = frontier.remove()
            if node.state == self.maze_goal:
                return True

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)


def path_finder(maze):
    solver = Solver(maze)
    return solver.solve_maze()
