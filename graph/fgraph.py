def parse_graph(data):
    d={}
    with open(data,'r')as f:
        for c in f:
            r=c.strip().split(',')
            if r[0] in d:
                d[r[0]][r[1]]=int(r[2])
            else:
                d[r[0]]={r[1]:int(r[2])}
    return d


def number_vertices(graph):
    s=set()
    for c in graph.keys():
        s.add(c)
    for c in graph.values():
        for j in c.keys():
            s.add(j)
    return len(s)

gr=parse_graph('graph.csv')
#print(number_vertices(gr),gr)

def attain(key,graph,ens=set()):
    if key in graph:
        for m in graph[key].keys():
            if m not in ens:
                ens.add(m)
                ens=attain(m,graph,ens)
    return ens

#greach=parse_graph('reach.csv')
#print(attain('f',greach))

def shortest_distance(graph,v1,v2):
    paths={v1:(0,[v1])}
    visited=set()

    while paths!={}:
        min=float('inf')
        for key in paths.keys():
            if paths[key][0]<min:
                min=paths[key][0]
                gmin=key
        if gmin==v2:
            return paths[v2]
        
        if gmin not in visited:
            visited.add(gmin)
            if gmin in graph:
                for m in graph[gmin].keys():
                    if m not in visited:
                        if m not in paths:
                            paths[m]=(graph[gmin][m]+min, paths[gmin][1] + [m])
                        else:
                            r=graph[gmin][m]+min
                            if r<paths[m][0]:
                                paths[m]=(r,paths[gmin][1] + [m])
        del paths[gmin]
    return None
gr3=parse_graph('graph2.csv')
#print(shortest_distance(gr,'a','f'))
#print(shortest_distance(gr3,'v1','v6'))


thrones=parse_graph('thrones.csv')
#print(len(thrones))
#print(number_vertices(thrones))
#print(len(attain('Eddard', thrones)))
#print(shortest_distance(thrones,'Eddard', 'Doran'))