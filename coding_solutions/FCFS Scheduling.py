
def fcfs(p,a,b):
    aorg = [q for q in a]
    a.sort()

    p1 = []; b1 = []; ct = []; tt = []; wt = []

    for r in a:
        i = aorg.index(r)
        p1.append(p[i])
        b1.append(b[i])

    k = int(b1[0])
    ct.append(k)
    for e in range(1,len(b1)):
        ct.append(k + int(b1[e]))
        k += int(b1[e])

    for e in range(len(a)):
        tt.append(int(ct[e]) - int(a[e]))

    for e in range(len(a)):
        wt.append(int(tt[e]) - int(b[e]))

    print('\n[Processid , Arival time ,Burst time, Complition time, Turn around time ,Wait time]\n')
    for r in range(len(a)):
        print(f'Pid: {p1[r]}, At: {a[r]}, Bt: {b1[r]}, Ct: {str(ct[r])}, Tt: {str(tt[r])}, Wt: {str(wt[r])}')


p = [x for x in input('Enter Process Id\'s : ').split()]
a = [int(x) for x in input('Enter their arrival time : ').split()]
b = [x for x in input('Enter their burst times : ').split()]
if len(p) == len(a) and len(a) == len(b):
    fcfs(p, a, b)
else:
    print('Process , Arival time,Burst times don\'t match....')
