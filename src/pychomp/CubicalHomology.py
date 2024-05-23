# CubicalHomology.py
# MIT LICENSE 2022 Marcio Gameiro
#
# Marcio Gameiro
# 2024-05-23

from pychomp._chomp import *

def CubicalHomology(cubes):
    """Compute homology of a collection (list) of top dimensional
    cubes and return the Betti numbers. Each cube in the list of
    cubes is represented by its minimum vertex.
    """
    # Space dimension
    dim = len(cubes[0])
    # Get grid size from the list of cubes
    grid_size = [max(cubes, key=lambda c: c[d])[d] + 1 for d in range(dim)]
    # Extended grid size for pyCHomP complex (to account for fringe cells)
    grid_size_ext = [grid_size[d] + 2 for d in range(dim)]
    # Create a pyCHomP cubical complex
    C = CubicalComplex(grid_size_ext)
    # Shape of top dimensional cells
    shape = 2**dim - 1
    # Get set of cells indices in the complex
    cells_indices = {C.cell_index(cube, shape) for cube in cubes}
    # Assign grading 0 to cells in the list of cubes
    def grading(cell):
        if any(c in cells_indices for c in C.topstar(cell)):
            return 0
        return 1
    # Create a pyCHomP graded complex
    graded_complex = GradedComplex(C, grading)
    # Compute the connection matrix
    cm = ConnectionMatrix(graded_complex)
    # Get the Betti numbers
    betti_numbers = cm.count()[0]
    return betti_numbers
