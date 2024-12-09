from reversible import *

def test_xy2natur():
    assert xy2natur(1,1) == 1
    assert xy2natur(2,1) == 2
    assert xy2natur(1,2) == 3
    assert xy2natur(3,1) == 4
    assert xy2natur(2,2) == 5
    assert xy2natur(1,3) == 6
    assert xy2natur(4,1) == 7  
    assert xy2natur(3,2) == 8
    assert xy2natur(2,3) == 9
    assert xy2natur(1,4) == 10
    assert xy2natur(5,1) == 11
    assert xy2natur(4,2) == 12  

def test_natur2xy():
    assert natur2xy(1) == (1,1)
    assert natur2xy(2) == (2,1)
    assert natur2xy(3) == (1,2)
    assert natur2xy(4) == (3,1)
    assert natur2xy(5) == (2,2)
    assert natur2xy(6) == (1,3)
    assert natur2xy(7) == (4,1)

def test_natur2xy2natur():
    for i in list(range(1000))[1:]:
        assert i == xy2natur(natur2xy(i)[0],natur2xy(i)[1])

def test_reversen():
    assert reversen(0) == 0
    assert reversen(12) == 21
    assert reversen(10) == 1
    assert reversen(438) == 834
    assert reversen(-1) == -1
    assert reversen(-12) == -21
    assert reversen(-10) == -1
    assert reversen(-438) == -834

def test_operat4():
    assert operat4((1,1),0) == 2
    assert operat4((1,2),0) == 3
    assert operat4((1,1),1) == "out err 0"
    assert operat4((1,2),1) == -1
    assert operat4((1,1),2) == "out err 1"
    assert operat4((1,2),2) == 2
    assert operat4((1,1),3) == "out err 1.0"
    assert operat4((1,2),3) == "out err 0.5"

def test_do_n():
    assert do_n(1) == []
    assert do_n(2) == []
    assert do_n(312) == []

#print(xy2natur(100,4100))