def problem_one():
    """Add all the natural numbers below 1000 that are multiples of 3 or 5.""" 
    print sum(x for x in xrange(1, 1000) if x % 3 == 0 or x % 5 == 0)
