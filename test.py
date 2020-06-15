List = [5, 2, 3, 4, 2, 6, 2, 2, 2, 1]

print(sum(List)+List.count(1)+len(List)+List.index(2)+List.index(2,2)+min(List)+max(List))

x = 5.2
x **= 3
print(x)

# initializing list
li = [1, 3, 4, 4, 4, 6, 7]
import bisect
print ("Output = ", end="")
print (bisect.bisect(li, 4)+bisect.bisect_left(li, 4)+bisect.bisect_right(li, 4, 0, 4))


c1 = { 'A' : 'B', 'C' : 19 }
c2 = { 'ID' : 47 }
sequ = ('A', 'C', 'D')
c1.update(c2)
print (str(c1))
ct = dict.fromkeys(sequ,5)
print (str(ct))

print(float('1e-003'))

i = [12, 9, 14]
k = [7, 16, 11]
for j in i[:]:
   for m in k[:]:
      if(j%m == 0):
         j = j // 2
         m = m / 2
         print (j, m)
      else:
         j = j + m
         m = m - j
         print (j, m)

def country(*abc):
  if len(abc) == 1:
    item = abc[0]
    def f(obj):
      return obj[item]
  else:
    def f(obj):
      return tuple(obj[item] for item in abc)
  return f

selection = []
selection = country(slice(2, None))('AUSTRALIA')
print (selection)

ast = [2, 1, 3, 5, 3, 8]
ast.sort()
print (end="")
for i in range(0, len(ast)):
    print(ast[i]*2, end=" ")
print("\r")
ast.reverse()
print (end="")
for i in range(1, len(ast)):
    print(ast[i]+3, end=" ")


a = -10
b = 5.5
c = 15
d = 5
import math
print('\n')
print (math.copysign(6.5, -10))
print (end="")
print (math.gcd(5,15))

class X(object):
    def __init__(self,a):
        self.num = a
    def dbup(self):
        self.num *= 2

class Y(X):
    def __init__(self,a):
        X.__init__(self, a)
    def tpup(self):
        self.num*= 3

obj = Y(4)
print(obj.num*2/1)

obj.dbup()
print(obj.num*3/2)

obj.tpup()
print(obj.num/2*3)

List = [5, 12, 3, 4, 2, 16, 2, 2, 2, 11]
print('\n')
print(sum(List)+List.count(2)+min(List)+max(List)+List.pop())
del List[0]
del List[6]
print(List.pop(0)+len(List)+List.index(2)+List.index(2,2))
print('\n')
def comF(x, y):
    if x > y:
        sm = y
    else:
        sm = x
    for i in range(1, sm+1):
        if((x % i == 0) and (y % i == 0)):
            cf = i
    return cf
num1 = 84
num2 = 64
print(comF(num1, num2))

# from urllib import F
# from smtplib import FT
# from ftplib import FTP
# from http
print('\n')
result = []
import multiprocessing

def s_p(mp):
    global result
    for num in mp:
        result.append(num * num+1)
    print("{}".format(result))
if __name__ == "__main__":
    mp = [1,2,3,4]
    p1 = multiprocessing.Process(target=s_p, args=(mp,))
    p1.start()
    p1.join()
    print("{}".format(result))


def abc(n):
   if n <= 1:
       return n
   else:
       return(abc(n-1) + abc(n-2))
       print("1")
nterms = 13
if nterms <= 0:
   print("0")
else:
   for i in range(nterms):
       x=abc(i)
   print(x+11)

print('\n')
import multiprocessing

def enr(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print("{}".format(msg))
    conn.close()

def cer(conn):
    while 1:
        msg = conn.recv()
        if msg == "Hi":
            break
        print("{}".format(msg))

if __name__ == "__main__":
    msgs = ["hello", "hey", "hru?", "Hi"]
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=enr, args=(parent_conn,msgs))
    p2 = multiprocessing.Process(target=cer, args=(child_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

print('\n')


def prt2(n):
    y = 0
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            y = y + k
    return (y)


def prt3(m):
    if m > 1:
        for i in range(2, m):
            if (m % 3) == 0:
                print("failure")
                break
            else:
                print("success")
    else:
        print("failure")


n = 5
m = prt2(n)
k = prt3(m - 3)


class D:
    def __init__(self, l, c):
        self.l = l
        self.c = c

    def b(self):
        b = "1" * 2
        return b


print('\n')
if __name__ == "__main__":
    d = D(4, "0")
    b = d.b()
    print(b)

class St:
    stm = 'Y'
    stm = 'X'
    def __init__(self, r):
        self.r = r
    def setdd(self, dd):
        self.dd = dd
    def getdd(self):
        return self.dd

a = St(101)
a.setdd("Y, UP")
a.setdd("X")
print(a.getdd())

print('\n')
tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])












