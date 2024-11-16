class Node:
    def __init__(self, state, parent, action, cost_from_start, cost_to_finish):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost_from_start = cost_from_start
        self.cost_to_finish = cost_to_finish
        self.total_cost = cost_from_start + cost_to_finish


class AStarFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def get_node_with_lowest_total_cost(self):
        sorted_frontier = sorted(self.frontier, key=lambda node: node.total_cost)
        return sorted_frontier[0]

    def remove(self):
        if self.empty():
            raise Exception('empty frontier')
        else:
            node = self.get_node_with_lowest_total_cost()
            self.frontier.remove(node)
            return node


class Solver:
    WALL = 'W'
    PASSAGE = '.'

    def __init__(self, mz):
        maze = [list(line) for line in mz.splitlines()]
        self.maze_height = len(maze)
        self.maze_width = len(maze[0])
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
        self.solution = []

    @staticmethod
    def calculate_cost_from_start(node_state):
        return sum(node_state)

    def calculate_cost_to_finish(self, node_state):
        height_cost = self.maze_height - node_state[0] - 1
        width_cost = self.maze_width - node_state[1] - 1
        return height_cost + width_cost

    def neighbours(self, state):
        row, col = state
        candidates = [
            Node((row - 1, col), parent=None, action='up',
                 cost_from_start=self.calculate_cost_from_start((row - 1, col)),
                 cost_to_finish=self.calculate_cost_to_finish((row - 1, col))),
            Node((row + 1, col), parent=None, action='down',
                 cost_from_start=self.calculate_cost_from_start((row + 1, col)),
                 cost_to_finish=self.calculate_cost_to_finish((row + 1, col))),
            Node((row, col - 1), parent=None, action='left',
                 cost_from_start=self.calculate_cost_from_start((row, col - 1)),
                 cost_to_finish=self.calculate_cost_to_finish((row, col - 1))),
            Node((row, col + 1), parent=None, action='right',
                 cost_from_start=self.calculate_cost_from_start((row, col + 1)),
                 cost_to_finish=self.calculate_cost_to_finish((row, col + 1))),
        ]

        def is_valid_node(node):
            if 0 <= node.state[0] < self.maze_height and 0 <= node.state[1] < self.maze_width \
                    and not self.maze_walls[node.state[0]][node.state[1]]:
                return True
            else:
                return False

        return filter(is_valid_node, candidates)

    def solve_maze(self):
        start = Node(self.maze_start, parent=None, action=None,
                     cost_from_start=self.calculate_cost_from_start(self.maze_start),
                     cost_to_finish=self.calculate_cost_to_finish(self.maze_start))
        frontier = AStarFrontier()
        frontier.add(start)

        while True:
            if frontier.empty():
                return False

            node = frontier.remove()
            if node.state == self.maze_goal:
                while node.parent is not None:
                    self.solution.append(node)
                    node = node.parent
                return len(self.solution)

            self.explored.add(node.state)

            for neighbour in self.neighbours(node.state):
                if not frontier.contains_state(neighbour.state) and neighbour.state not in self.explored:
                    child = Node(state=neighbour.state, parent=node, action=neighbour.action,
                                 cost_from_start=self.calculate_cost_from_start(neighbour.state),
                                 cost_to_finish=self.calculate_cost_to_finish(neighbour.state))
                    frontier.add(child)


def path_finder(maze):
    solver = Solver(maze)
    return solver.solve_maze()
