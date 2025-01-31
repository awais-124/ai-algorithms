class Star:
    def __init__(self, _list):
        self.list=_list
    def get_parosi(self, n):
            return self.list[n]
    def h(self, i): return 1
    
    def khap(self, s, e):
        ol=set([s])
        cl=set([])
        g = {s:0}
        p = {s:s}
        
        while ol:
            n=None
            for v in ol:
                if n == None or g[v]+self.h(v) < g[n]+self.h(n):
                    n=v
                    
            if n == None: return None
            if n==e:
                path=[]  
                while p[n]!=n:
                    path.append(n)
                    n=p[n]
                    
                path.append(s)
                path.reverse()
                return path
            
            for (m,w) in self.get_parosi(n):
                if m not in cl and m not in ol:
                    ol.add(m)
                    g[m] = g[n] + w
                    p[m] = n
                    
                elif g[m] > g[n] + w:
                    g[m] = g[n] + w
                    p[m] = n
                    if m in cl:
                        cl.remove(m)
                        ol.add(m)
                        
            ol.remove(n)
            cl.add(n)            
        print("NOT FOUND")
        return None        
    
nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}

inst = Star(nodes)
print("PATH : ", inst.khap("A","J"))              