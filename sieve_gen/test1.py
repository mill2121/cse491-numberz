import sieve

def test1():
    sve = sieve.sieve()
    i = iter(sve)
    nxt = i.next()
    print nxt
    assert nxt == 3

def test2():
    sve = sieve.sieve()
    i = iter(sve)
    nxt = i.next()
    print nxt
    nxt = i.next()
    print nxt
    assert nxt == 5

def test3():
    sve = sieve.sieve()
    i = iter(sve)
    nxt = i.next()
    print nxt
    nxt = i.next()
    print nxt
    nxt = i.next()
    print nxt
    assert nxt == 7

test1()
test2()
test3()
    
