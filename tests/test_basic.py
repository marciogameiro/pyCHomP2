import pychomp

def test_cubical():
    C = pychomp.CubicalComplex([3, 2])
    assert C.dimension() == 2
    assert C.size() == 24

def test_simplicial():
    simplices = [[0, 1], [1, 2], [2, 0], [3]]
    C = pychomp.SimplicialComplex(simplices)
    betti_numbers = pychomp.Homology(C).count()
    assert C.dimension() == 1
    assert betti_numbers == [2, 1]
