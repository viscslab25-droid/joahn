def find_cubed_sum(arr:list[int])->list[int]:
    l:list[int]=[]
    for i in arr:
        sum=0
        i=j=str(i)
        for k in i:
            c=int(k)**3
            sum+=c
        if sum == int(j):
            l.append(int(j))
    #!print(l)
    return l
#!print(max(find_cubed_sum([1,2,3,4,5,6,76,77,8,9,5777,153,370])),min(find_cubed_sum([1,2,3,4,5,6,76,77,8,9,5777,153,370])))
def segregator(arr:list[int])->tuple[list[int],list[int],list[int]]:
    neg:list[int]=[]
    pos:list[int]=[]
    for i in arr:
        if i>0:
            pos.append(i)
        elif i<0:
            neg.append(i)
    print(pos,"\n",neg,"\n",arr)
    return pos,neg,arr
def grade_calc(tup:tuple[int])->list[str]:
    f:list[str]=[]
    for i in tup:
        if i>=75:
            f.append("A")
        elif 60<i<75:
            f.append("B")
        elif 50<i<60:
            f.append("C")
        elif i<50:
            f.append("D")
    return f
def counter(txt:str)->dict[str,int]:
    d:dict[str,int]={}
    for i in txt:
        d[i] = d.get(i,0)+1
    return d
print (1) if 5>2 else print(2)
print([x for x in range(20)])