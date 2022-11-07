def postfix_eval(chaine):
    r=chaine.split()
    operateurs=['+',"-",'*','/']
    pile=[]
    s=0
    for c in r:
        if c not in operateurs:
            try:
                pile.append(int(c))
            except:
                return 'error-syntax'
        else:
            if len(pile)<2:
                return 'error-empty-stack'
            if c=='+':
                s=pile[-1]+pile[-2]
            if c=='-':
                s=pile[-2]-pile[-1]
            if c=='*':
                s=pile[-1]*pile[-2]
            if c=='/':
                s=pile[-2]//pile[-1]
            pile =pile[:-2:]
            pile.append(s)
        
    if len(pile)!=1:
        return 'error-unfinished'
    return pile[0]
    