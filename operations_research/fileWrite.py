def writeQuestion(ques, constraints, variables):
   fp = open("new1.txt", 'w')
   fp.write("Question:\nMaximize:\n\tZ = " + ques + "\nSubject to:\n\t")
   for i in constraints:
       fp.write(i + '\n\t')
   fp.write('Where: ')
   for i in variables:
       if not variables.index(i) == len(variables) - 1:
           fp.write(i + ', ')
       else:
           fp.write(i)
   fp.write('>=0')
   fp.close()


def writeIterations(coeff, cost, xb, bv, av, mr, deltas, Z): #mr = ov
   global itercount
   fp = open('new1.txt', 'a')
   fp.write('\n\nIteration ' + str(itercount) +' :\n')
   fp.write('\t{0:^6}\t{1:^6}\t{2:^6}\t'.format('bv', 'Cb', 'Xb'))
   for i in av:
       fp.write('{0:^6}\t'.format(i))
   fp.write('Min Ratio\n\t')
   for i in bv:
       fp.write('{0:^6}\t{1:^6.2f}\t{2:^6.2f}\t'.format(i, cost[i], xb[bv.index(i)]))
       for j in av:
           fp.write('{0:^6.2f}\t'.format(coeff[j][bv.index(i)]))
       if not mr[bv.index(i)] == '-':
           fp.write('{0:^9.2f}\n\t'.format(mr[bv.index(i)]))
       else:
           fp.write('{0:^9}\n\t'.format(mr[bv.index(i)]))
   fp.write('{0:^4}\t{1:^6}\t{2:^6}\t'.format('deltas', '', ''))
   for j in av:
       fp.write('{0:^6.2f}\t'.format(deltas[j]))
   fp.write('\n\n{0:^{1}}'.format('Z = ' + str(Z), 27 + 6 * len(av) + len('Z = ' + str(Z)) * 2))
   fp.close()
   itercount += 1


def writeAnswer(zmax, xb, av, bv):
   fp = open('new1.txt', 'a')
   fp.write('\n\n\nFINAL ANSWER:\n')
   fp.write((' ' * 10) + 'Zmax = ' + str(zmax) + '     when:\n')
   for i in av:
       if 's' not in i:
           fp.write((' ' * 10) + i + " = " + str(xb[bv.index(i)] if i in bv else 0) + '\n')
   fp.close()

itercount = 1
