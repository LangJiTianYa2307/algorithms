def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
def _not_disvisible(n):
    return lambda x:x%n > 0
def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        it = filter(_not_disvisible(n),it)
        yield n
'''--------------------'''
'''测试'''
for n in prime():
    if n < 1000:
        print(n)
    else:
        break