import fileWrite
def getCoefficient(eqn):
   co, sign = '', 1
   for i in eqn:
       if i == '-':
           sign = -1
       if i.isdigit():
           co += i
   return sign * int(co)

def iterations(coeff, cost, xb, bv, av):
   zee = [cost[i] for i in bv]
   z = sum([ zee[i] * xb[i] for i in range(len(bv))])
   deltas = {}
   for i in av:
       deltas[i] = sum(coeff[i][j] * zee[j] for j in range(len(bv))) - cost[i]
   min, iv = 0, ''
   for i in deltas:
       if deltas[i] < min:
           min = deltas[i]
           iv = i
   if iv=='':
       print("Zmax = ", z, " when:")
       for i in av:
           if 's' not in i:
               print(i, " = ", xb[bv.index(i)] if i in bv else 0)
       fileWrite.writeIterations(coeff, cost, xb, bv, av, ['-' for i in bv], deltas, z)
       fileWrite.writeAnswer(z, xb, av, bv)
   else:
       ov = []
       for i in range(len(bv)):
           if coeff[iv][i] != 0:
               ov.append(xb[i] / coeff[iv][i])
           else:
               ov.append(-1)
       mr = 100000
       fileWrite.writeIterations(coeff, cost, xb, bv, av, ov, deltas, z)
       for i in ov:
           mr = i if i < mr and i >= 0 else mr
       bv[ov.index(mr)] = iv
       key = coeff[iv][ov.index(mr)]
       xb[ov.index(mr)] = mr
       for i in coeff:
           coeff[i][ov.index(mr)] /= key
       for j in range(len(bv)):
           if j != ov.index(mr):
               c = coeff[iv][j]
               xb[j] -= c * xb[ov.index(mr)]
               for i in av:
                   coeff[i][j] -= c * coeff[i][ov.index(mr)]
       iterations(coeff, cost, xb, bv, av)


eqn = input("Enter the Objective function:(NOTE: Variable names as w, x, y, z etc)\n")
cost = {}
variables = [i for i in eqn if i.isalpha()]
cost[variables[0]] = getCoefficient(eqn[:eqn.index(variables[0])])
for i in range(1, len(variables)):
   cost[variables[i]] = getCoefficient(eqn[eqn.index(variables[i-1])+1: eqn.index(variables[i])])
coeff, xb = {}, []
for i in variables:
   coeff[i] = []
n = int(input("Enter the no of constraints:\n"))
print("Enter the constraints:")
constraints = []
num = n
while n > 0:
   constr = input()
   constraints.append(constr)
   coeff[variables[0]].append(getCoefficient(constr[:constr.index(variables[0])]))
   for i in range(1, len(variables)):
       coeff[variables[i]].append(getCoefficient(constr[constr.index(variables[i - 1]) + 1: constr.index(variables[i])]))
   xb.append(getCoefficient(constr[constr.index(variables[len(variables) - 1]) + 1:]))
   cost["s" + str(num - n + 1)] = 0
   coeff['s' + str(num - n + 1)] = [(lambda x, ind: 1 if x == ind - 1 else 0)(i, num - n + 1) for i in range(num)]
   n -= 1
fileWrite.writeQuestion(eqn, constraints, variables)
iterations(coeff, cost, xb, [k for k in cost if 's' in k], [k for k in cost])
'''Qn1.
10x+15y+20z
2
2x+4y+6z<=24
3x+9y+6z<=30
----------------
qn2.
3x+2y+5z
3
1x+1y+1z<=9
2x+3y+5z<=30
2x-1y-1z<=8
-----------------
qn3.
5x+3y+7z
3
1x+1y+2z<=26
3x+2y+1z<=26
1x+1y+1z<=18
-----------------
qn3b.(wrong)
5x+3y+7z
3
1x+1y+2z<=28
3x+2y+1z<=26
1x+1y+1z<=18
-----------------
qn4.
2w+1x-3y+5z
3
1w+7x+3y+7z<=46
3w-1x+1y+2z<=8
2w+3x-1y+1z<=10
------------------
qn5.
2w+4x+1y+1z
3
1w+3x+0y+1z<=4
2w+1x+0y+0z<=3
0w+1x+4y+1z<=3
------------------
qn6.(wrong)
1x-3y+2z
3
-3x+1y-2z<=-7
-2x+4y+0z<=12
-4x+3y+8z<=10
------------------
qn7.(wrong)
3w+4x+1y+5z
3
8w+3x+2y+2z<=10
2w+5x+1y+4z<=3
1w+4x+5y+2z<=7
------------------
qn8.
2w+3x+1y+7z
3
8w+3x+4y+1z<=6
2w+6x+1y+5z<=3
1w+4x+5y+2z<=7
--------------------
qn9.
4w+5x+9y+11z
3
1w+1x+1y+1z<=15
7w+5x+3y+2z<=120
3w+5x+10y+15z<=100
----------------------
qn10.
3x+2y
2
1x+1y<=4
1x-1y<=2
----------------------
qn11.
3x+2y+5z
3
1x+2y+1z<=430
3x+0y+2z<=460
1x+4y+0z<=420
------------------------
qn12.
3x+5y+4z
3
2x+3y+0z<=8
0x+2y+5z<=10
3x+2y+4z<=15
------------------------
qn13.
5x+3y
3
1x+1y<=2
5x+2y<=10
2x+8y<=12
-------------------------
qn14.
4x+10y
3
2x+1y<=50
2x+5y<=100
2x+3y<=90
---------------------
qn15.
10x+6y+11z
3
4x+6y+7z<=210
9x+1y+5z<=190
0x+13y+2z<=175
-------------------------
qn16.
2x+1y+1z(wrong)
3
4x+6y+3z<=8
3x-6y-4z<=1
2x+3y-5z<=4
----------------------
qn17.
30x+23y+29z
2
6x+5y+3z<=26
4x+2y+5z<=7
---------------------
qn18.
6x+7y+9z
3
3x+7y+6z<=254
5x+8y+9z<=424
11x+6y+8z<=235
--------------------------
qn19.
2x+1y
3
4x+3y<=12(wrong)
4x+1y<=8
4x-1y<=8
-------------------------
qn20.
1x+2y(only one of the answers)
3
-1x+2y<=8
1x+2y<=12
1x-2y<=3
-----------------------
qn21.
20x+25y
2
12x+16y<=100
16x+8y<=80
-----------------------
qn22.
30x+40y
3
60x+120y<=12000
8x+5y<=600
3x+4y<=500
--------------------------
qn23.
4x + 3y + 6z
3 
2x + 3y + 2z <= 440
4x + 0y + 3z <= 470
2x + 5y + 0z <= 430
-------------------------
qn24.
2x+5y
3
1x+4y<=24
3x+1y<=21
1x+1y<=9
---------------------------
qn25.
12x+15y+14z
3
-1x+1y+0z<=0
0x-1y+2z<=0
1x+1y+1z<=100
----------------------------
qn26.
2x+1y
4
1x+2y<=10
1x+1y<=6
1x-1y<=2
1x-2y<=1
--------------------------
qn27.
10x+15y+20z
2
2x+4y+6z<=24
3x+9y+6z<=30
--------------------
10x+6y+4z
3
1x+2y+3z<=100
10x+4y+5z<=600
2x+2y+6z<=300
---------------------
12x+15y+14z(wr)
3
-1x+1y+0z<=0
0x-1y+2z<=0
1x+1y+1z<=100'''