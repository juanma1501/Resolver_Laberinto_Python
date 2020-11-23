###############################################################################
#   Name of the class: Wilson
#   Date of creation: 19/10/2020
#   Description:   This class is used to store Wilson´s algorithm, used to create
#                  a maze.
################################################################################

from random import choice


class Wilson:
    """Constructor"""

    def __init__(self):
        pass

    """ 
        Wilson's algorithm for generating mazes.

        The algorithm performs a random walk on the grid to create passages.
        Since every iteration we are performing a random
        walk from a random starting cell, and also erasing any loops in the
        process.
    """

    @staticmethod
    def create(grid):

        # This method is to choose a random element from a list, it easier to create this method inside another method
        # instead of doing it outside this one, because we don't have to create an instance to use it. In grid we have a
        # method to choose a random cell but is not static so we can't use it.
        def choose_random_element(lst):
            if len(lst) == 0:
                return None
            return choice(lst)

        # Create a database of unvisited cells. At this point this is all the cells in the grid
        unvisited_cells = []
        for cell in grid.all_cells():
            unvisited_cells.append(cell)

        # Choose a starting cell at random and mark it as visited
        starting_cell = choose_random_element(unvisited_cells)
        unvisited_cells.remove(starting_cell)

        # We have to do this until we have visited all the cells in the grid. Each
        # iteration we will first choose a random cell to start from in the
        # grid. We will then choose a random neighbor of that cell and add it
        # to run path. We then I randomly choose a neighbor of that neighbor and
        # add that to the run path and so on. We keep building a path this way
        # till we hit a visited cell. At that point we will link all the cells
        # that we have marked added to the run path.
        while len(unvisited_cells) > 0:

            # Choose a cell from the unvisited cells at random and add it to the run path.
            cell = choose_random_element(unvisited_cells)
            path = [cell]

            # Keep finding random neighbors till we find a visited cell
            while cell in unvisited_cells:
                neighbor = choose_random_element(cell.neighbors())
                if neighbor in path:
                    path = path[0:path.index(neighbor) + 1]
                else:
                    path.append(neighbor)
                cell = neighbor

            # Link all the cells we found in the run.
            visited_cells = None
            for cell in path:
                if visited_cells:
                    visited_cells.link(cell)
                    unvisited_cells.remove(visited_cells)
                visited_cells = cell
