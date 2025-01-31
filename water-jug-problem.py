class WaterJugProblem:
    def __init__(self):
        self.visited = set()  # To keep track of visited states
        self.solutions = []   # To store the solutions

    def is_goal_state(self, state):
        # Check if we have exactly 2 gallons in the 4-gallon jug
        return state[0] == 2

    def get_neighbors(self, state):
        x, y = state
        neighbors = []

        # Fill the 4-gallon jug
        if x < 4:
            neighbors.append((4, y))

        # Fill the 3-gallon jug
        if y < 3:
            neighbors.append((x, 3))

        # Empty the 4-gallon jug
        if x > 0:
            neighbors.append((0, y))

        # Empty the 3-gallon jug
        if y > 0:
            neighbors.append((x, 0))

        # Pour water from the 4-gallon jug to the 3-gallon jug
        if x > 0 and y < 3:
            transfer = min(x, 3 - y)
            neighbors.append((x - transfer, y + transfer))

        # Pour water from the 3-gallon jug to the 4-gallon jug
        if y > 0 and x < 4:
            transfer = min(y, 4 - x)
            neighbors.append((x + transfer, y - transfer))

        return neighbors

    def dfs(self, state, path):
        if self.is_goal_state(state):
            self.solutions.append(path + [state])  # Store the complete path
            return True

        if state in self.visited:
            return False

        self.visited.add(state)

        for neighbor in self.get_neighbors(state):
            if self.dfs(neighbor, path + [state]):
                return True

        return False

    def solve(self):
        initial_state = (0, 0)  # Starting with both jugs empty
        self.dfs(initial_state, [])
        return self.solutions


if __name__ == "__main__":
    water_jug_problem = WaterJugProblem()
    solutions = water_jug_problem.solve()

    if solutions:
        print("Solution found:")
        for solution in solutions:
            print("Path to solution:", solution)
    else:
        print("No solution found.")