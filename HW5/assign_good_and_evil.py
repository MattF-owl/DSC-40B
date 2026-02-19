
import dsc40graph

def assign_good_and_evil(G):
    
    def BFS(G,s,status = None, GE = None):
        IDX = 0
        GE_state = ['good','evil']
        if status is None:
            status = {node: 'undiscovered' for node in list(G.nodes)} 
        if GE is None:
            GE = {node:'' for node in list(G.nodes)}

        status[s] = 'pending'
        GE[s] = GE_state[IDX % 2]
        pending = [s]

        while pending:
            IDX += 1
            u = pending.pop(0)

            for v in G.neighbors(u):


                if status[v] == 'undiscovered':
                    GE[v] = GE_state[IDX % 2]
                    if GE[u] == GE[v]:
                        return status, None
                    status[v] = 'pending' 
                    pending.append(v)
            status[u] = 'visited'

        return status, GE
    
    status = {node: 'undiscovered' for node in list(G.nodes)}
    GE = {node:'' for node in list(G.nodes)}
    for node in list(G.nodes):

        if status[node] == 'undiscovered':
            status, GE = BFS(G, node, status = status, GE = GE)

        if GE is None:
            return None
        
    return GE