import random
import datetime

def parse(file):
    list=[]
    with open(file,'r') as f:
        for line in f:
            r=line.split()
            dict={}
            dict['prenom']=r[0]
            dict['nom']=r[1]
            dict['naissance']=r[2::]
            list.append(dict)
    return list


def randname(firstnames,lastnames):
    list=[]
    firsts=[]
    lasts=[]
    with open(firstnames,'r') as f:
        for c in f:
            firsts.append(c.strip())
    with open(lastnames,'r') as w:
        for c in w:
            lasts.append(c.strip())
    n=len(firsts)
    m=len(lasts)
    s=set()
    i=0
    while i !=10000:
        dict={}
        dict['firstname']=firsts[random.randint(0,n-1)]
        dict['lastname']=lasts[random.randint(0,m-1)]
        dict['birthday']=str(random.randint(1,31))+'/'+str(random.randint(1,12))+'/'+str(random.randint(2000,2004))
        p=dict['firstname']+dict['lastname']
        if p in s:
            pass
        else:
            list.append(dict)
            s.add(p)
            i+=1
    with open('data-big.txt','w') as f:
        for c in list:
            f.write(c['firstname']+' '+c['lastname']+' '+ (c['birthday']+'\n'))
    return list
    

p=randname('indexing-struct/first_names.txt','indexing-struct/last_names.txt')
def nomsdistincts(m):
    ens=set()
    for c in m:
        ens.add(c['firstname'])
    print(len(ens))
nomsdistincts(p)