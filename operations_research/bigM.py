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
   z = sum([zee[i] * xb[i] for i in range(len(bv))])
   deltas = {}
   for i in av:
       deltas[i] = sum(coeff[i][j] * zee[j] for j in range(len(bv))) - cost[i]
   min, iv = 0, ''
   for i in deltas:
       if deltas[i] < min:
           min = deltas[i]
           iv = i
   if iv=='':
       print("Zmax = ", round(z, 2), " when:")
       for i in av:
           if 's' not in i and 'a' not in i:
               print(i, " = ", round(xb[bv.index(i)], 2) if i in bv else 0)
   else:
       ov = []
       for i in range(len(bv)):
           if coeff[iv][i] != 0:
               ov.append(xb[i] / coeff[iv][i])
           else:
               ov.append(-1)
       mr = 100000
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
num = n
while n > 0:
   constr = input()
   coeff[variables[0]].append(getCoefficient(constr[:constr.index(variables[0])]))
   for i in range(1, len(variables)):
       coeff[variables[i]].append(getCoefficient(constr[constr.index(variables[i - 1]) + 1: constr.index(variables[i])]))
   xb.append(getCoefficient(constr[constr.index(variables[len(variables) - 1]) + 1:]))
   if '<=' in constr:
       cost["s" + str(num - n + 1)] = 0
       coeff['s' + str(num - n + 1)] = [(lambda x, ind: 1 if x == ind - 1 else 0)(i, num - n + 1) for i in range(num)]
   elif '>=' in constr:
       cost["s" + str(num - n + 1)] = 0
       cost["a" + str(num - n + 1)] = -1 * 10 ** 6
       coeff['s' + str(num - n + 1)] = [(lambda x, ind: -1 if x == ind - 1 else 0)(i, num - n + 1) for i in range(num)]
       coeff['a' + str(num - n + 1)] = [(lambda x, ind: 1 if x == ind - 1 else 0)(i, num - n + 1) for i in range(num)]
   else:
       cost["a" + str(num - n + 1)] = -1 * 10 ** 6
       coeff['a' + str(num - n + 1)] = [(lambda x, ind: 1 if x == ind - 1 else 0)(i, num - n + 1) for i in range(num)]
   n -= 1
iterations(coeff, cost, xb, [(lambda n: 'a'+str(n) if 'a' + str(n) in cost else 's' + str(n))(i) for i in range(1,num+1)], [k for k in cost])


'''2x+3y+4z
3
3x+1y+4z<=600
2x+4y+2z>=480
2x+3y+3z=540
'''