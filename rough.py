from functools import reduce

if __name__ == '__main__':
fact = lambda n: reduce(lambda x,y:x*y,range(1,n+1))if n>0 else 1
print(fact(int(input())))

