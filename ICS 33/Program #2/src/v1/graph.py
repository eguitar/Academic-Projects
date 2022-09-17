# Submitter: edtrinh(Trinh, Eric)
# Defined below is a special exception for use with the Graph class methods
# Use it like any exception: e.g., raise GraphError('Graph.method" ...error indication...')
from goody import type_as_str

class GraphError(Exception):
    pass # Inherit all methods, including __init__
 
 
class Graph:
    # HELPER METHODS: used for checking legal arguments to methods below
    def legal_tuple2(self,t):
        return type(t) is tuple and len(t) == 2 and\
               type(t[0]) is str and type(t[1]) is str

    def legal_tuple3(self,t):
        return type(t) is tuple and len(t) == 3 and\
               type(t[0]) is str and type(t[1]) is str and self.is_legal_edge_value(t[2])
        
 
    # __str__ and many bsc tests use the name self.edges for the outer/inner-dict.
    # So __init__ should use self.edges for the name for this dictionary
    # self should store NO other attributes: compute all results from self.edges ONLY
    # Each value in an edges tuple represents either a 
    #   (a) str    : origin node, or
    #   (b) 3-tuple: (origin node, destination node, edge value) 
    def __init__(self,legal_edge_value_predicate,*edges):
#         print(edges)
        self.edges = {}
        self.is_legal_edge_value = legal_edge_value_predicate
        for e in edges:
            if type(e) == str:
                if e in self.edges:
#                     print(self.edges)
#                     print(e)
                    raise GraphError
                self.edges[e] = {}
            elif type(e) == tuple:
                try:
                    if self.is_legal_edge_value(e[2]):
                        if e[0] in self.edges and e[1] in self.edges[e[0]]:
#                             print(2)
                            raise GraphError
                        if e[0] not in self.edges:
                            self.edges[e[0]] = {}
                        self.edges[e[0]][e[1]]= e[2]
                        if e[1] not in self.edges:
                            self.edges[e[1]] = {}
                    else:
#                         print(3)
                        raise GraphError
                except:
#                     print(4)
                    raise GraphError
            else:
#                 print(5)
                raise GraphError

    # Put all other methods here
    def __str__(self):
        output = '\nGraph:'
        for origin in sorted(self.edges):
            output += f'\n  {origin}:'
            for end in sorted(self.edges[origin]):
                if end == sorted(self.edges[origin])[-1]:
                    output += f' {end}({self.edges[origin][end]})'
                else:
                    output += f' {end}({self.edges[origin][end]}),'
        return output
    
    def __getitem__(self,item):
        if type(item) is str:
            try:
                return self.edges[item]
            except:
                raise GraphError('Key does not exist')
        elif type(item) is tuple and len(item) == 2:
            try:
                return self.edges[item[0]][item[1]]
            except:
                raise GraphError('Origin or destination node does not exist')
        else:
            raise GraphError('Invalid argument passed')
        
    def __setitem__(self,item,value):
        if type(item) is tuple and len(item) == 2 and type(value) is int:
            if not(type(item[0]) is str and type(item[1]) is str):
                raise GraphError('Invalid item parameter')
            try:
                self.edges[item[0]][item[1]] = value
            except:
                self.edges[item[0]] = {}
                self.edges[item[0]][item[1]] = value
            finally:
                try:
                    if self.edges[item[1]]: pass
                except:
                    self.edges[item[1]] = {}
        else:
            raise GraphError('Invalid node or edge value')

    def node_count(self):
        count = 0
        for edge in self.edges:
            count += 1
        return count
    
    def __len__(self):
        count = 0
        for node in self.edges:
            for edge in self.edges[node]:
                count += 1
        return count
    
    def out_degree(self,node):
        if not type(node) is str:
            raise GraphError('Node parameter is not a string')
        try:
            return len(self.edges[node])
        except:
            raise GraphError('Node is not in the graph')

    def in_degree(self,node):
        if not type(node) is str:
            raise GraphError('Node parameter is not a string')
        if not node in self.edges:
            raise GraphError('Node is not in the graph')
        try:
            count = 0
            for n in self.edges:
                for edge in self.edges[n]:
                    if edge == node:
                        count += 1
            return count
        except:
            raise GraphError('Node is not in the graph')
        
    def __contains__(self,item):
        try:
            if type(item) is str:
                return item in self.edges
            elif type(item) is tuple and len(item) == 2:
                try:
                    if self.edges[item[0]][item[1]]:
                        return True
                except:
                    return False
            elif type(item) is tuple and len(item) == 3:
                try:
                    if self.edges[item[0]][item[1]] == item[2]:
                        return True
                except:
                    return False
            else:
                raise GraphError('Not a valid item parameter')
        except:
            raise GraphError('Not a valid item parameter')
    
    def __delitem__(self,item):
        if type(item) is str:
            i = 1
            while i != 0:
                i = 0
                for node in self.edges:
                    if node == item:
                        del self.edges[node]
                        i = 1
                        break
                    else:
                        for edge in self.edges[node]:
                            if edge == item:
                                del self.edges[node][edge]
                                i = 1
                                break
        elif type(item) is tuple and len(item) == 2:
            if not(type(item[0]) is str and type(item[1]) is str):
                raise GraphError('Not a tuple')
            try:
                del self.edges[item[0]][item[1]]
            except:
                pass
        else:
            raise GraphError('Not a valid item parameter')
        
    def __call__(self,d):
        if type(d) is str and d in self.edges:
            return dict([(node,self.edges[node][edge]) for node in self.edges for edge in self.edges[node] if edge == d])
        else:
            raise GraphError('Argument is not a node in the graph')
    
    def clear(self):
        while self.edges != {}:
            for node in self.edges:
                del self.edges[node]
                break
    
    def dump(self,open_file,sep,convert=str):
        for node in self.edges:
            if self.edges[node] == {}:
                open_file.write(f'{node}\n')
            else:
                open_file.write(f'{node}')
                for edge in self.edges[node]:
                    open_file.write(f'{sep}{edge}{sep}{convert(self.edges[node][edge])}')
                open_file.write('\n')
      
    def load(self,open_file,sep,convert=int):
        self.clear()
        for line in open_file:
            line = line.rstrip('\n').split(sep)
            if len(line) == 1:
                if line[0] not in self.edges:
                    self.edges[line[0]] = {}
            else:
                if line[0] not in self.edges:
                    self.edges[line[0]] = {}
                for node,value in zip(line[1::2],line[2::2]):
                    self.edges[line[0]][node]= convert(value)
                    if node not in self.edges:
                        self.edges[node] = {}
     
    def reverse(self):
        new_edge = []
        index = True
        for node in self.edges:
            if self.edges[node] == {}:
                new_edge.append(node)
            else:
                for edge in self.edges[node]:
                    new_edge.append((node,edge,self.edges[node][edge]))
        for i in range(len(new_edge)):
            if type(new_edge[i]) is tuple:
                new_edge[i] = (new_edge[i][1],new_edge[i][0],new_edge[i][2])
        return Graph(lambda x: True,*tuple(sorted(new_edge,key=lambda x: len(x))))
     
    def natural_subgraph(self,*nodes):
        for n in nodes:
            if not type(n) is str:
                raise GraphError('Invalid node argument')
        new_list = []
        for node in self.edges:
            if node in nodes:
                if self.edges[node] == {}:
                    new_list.append(node)
                else:
                    
                    index = False
                    for edge in self.edges[node]:
                        if edge in nodes:
                            new_list.append((node,edge,self.edges[node][edge]))
                            index = True
                    if not index:
                        new_list.append(node)
        return Graph(lambda x: True,*tuple(sorted(new_list,key=lambda x: len(x))))
     
    def __iter__(self):  
        class Graph_iter:
            def __init__(self,edges):
                self.edges = []
                for node in edges:
                    if edges[node] == {}:
                        test = True
                        for name in edges:
                            if node in edges[name]:
                                test = False
                        if test: self.edges.append(node)
                    else:
                        for edge in edges[node]:
                            self.edges.append((node,edge,edges[node][edge]))
                self.edges = sorted(self.edges, key = lambda x: x[0])
                self.n = 0                 
            
            def __next__(self):
                if self.n == len(self.edges):
                    raise StopIteration
                index = self.edges[self.n]
                self.n += 1
                return index
            
            def __iter__(self):
                return self  
                     
        return Graph_iter(self.edges)
         
    def __eq__(self,right):
        return self.edges == right.edges
     
    def __ne__(self,right):
        return self.edges != right.edges
     
    def __le__(self,right):
        try:
            for node in self.edges:
                if self.edges[node] == {}:
                    if right.edges[node][edge] != {}:
                            return False
                else:
                    for edge in self.edges[node]:
                        if self.edges[node][edge] != right.edges[node][edge]:
                            return False
            return True
        except:
            return False
     
    def __add__(self,right):
        try:
            new_edge = []
            index = True
            for node in self.edges:
                if self.edges[node] == {}:
                    new_edge.append(node)
                else:
                    for edge in self.edges[node]:
                        new_edge.append((node,edge,self.edges[node][edge]))
        except:
            raise GraphError('Could not add two arguments')
        
        if type_as_str(self) == type_as_str(right):
            for node in right.edges:
                if right.edges[node] == {} and not(node in self.edges):
                    new_edge.append(node)
                else:
                    for edge in right.edges[node]:
                        try:
                            if self.edges[node][edge]: pass
                        except:
                            new_edge.append((node,edge,right.edges[node][edge]))        
            return Graph(lambda x: True,*tuple(sorted(new_edge,key=lambda x: len(x))))
        
        elif type_as_str(self) == 'graph.Graph' and type(right) is str:
            index = True
            for n in new_edge:
                if n == right or right in n:
                    index = False
            if index:
                new_edge.append(right)
            return Graph(lambda x: True,*tuple(sorted(new_edge,key=lambda x: len(x))))
        
        elif type_as_str(self) == 'graph.Graph' and type(right) is tuple:
            g = Graph(lambda x: True,*tuple(sorted(new_edge,key=lambda x: len(x))))
            g[right[0],right[1]] = right[2]
            return g
        
        else:
            raise GraphError('Could not add two arguments')
     
    def __radd__(self,right):
        try:
            new_edge = []
            index = True
            for node in self.edges:
                if self.edges[node] == {}:
                    new_edge.append(node)
                else:
                    for edge in self.edges[node]:
                        new_edge.append((node,edge,self.edges[node][edge]))
        except:
            raise GraphError('Could not add two arguments')
        
        if type_as_str(self) == type_as_str(right):
            for node in right.edges:
                if right.edges[node] == {} and not(node in self.edges):
                    new_edge.append(node)
                else:
                    for edge in right.edges[node]:
                        try:
                            if self.edges[node][edge]: pass
                        except:
                            new_edge.append((node,edge,right.edges[node][edge]))        
            return Graph(lambda x: True,*tuple(sorted(new_edge,key=lambda x: len(x))))
        
        elif type_as_str(self) == 'graph.Graph' and type(right) is str:
            index = True
            for n in new_edge:
                if n == right or right in n:
                    index = False
            if index:
                new_edge.append(right)
            return Graph(lambda x: True,*tuple(sorted(new_edge,key=lambda x: len(x))))
        
        elif type_as_str(self) == 'graph.Graph' and type(right) is tuple:
            g = Graph(lambda x: True,*tuple(sorted(new_edge,key=lambda x: len(x))))
            g[right[0],right[1]] = right[2]
            return g
        
        else:
            raise GraphError('Could not add two arguments')
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
    def __iadd__(self,right):
        try:
            new_edge = []
            index = True
            for node in self.edges:
                if self.edges[node] == {}:
                    new_edge.append(node)
                else:
                    for edge in self.edges[node]:
                        new_edge.append((node,edge,self.edges[node][edge]))
        except:
            raise GraphError('Could not add two arguments')
        
        if type_as_str(self) == type_as_str(right):
            for node in right.edges:
                if node in self.edges:
                    for edge in right.edges[node]:
                        self.edges[node][edge] = right.edges[node][edge]
                else:
                    self.edges[node] = {}
                    for edge in right.edges[node]:
                        self.edges[node][edge] = right.edges[node][edge]
                
                
                
                
                
#                 if right.edges[node] == {} and not(node in self.edges):
#                     self.edges[node] == {}
#                 else:
#                     for edge in right.edges[node]:
#                         if not edge in self.edges[node]:
#                             self.edges[node][edge] = right.edges[node][edge]
            return self
         
        elif type_as_str(self) == 'graph.Graph' and type(right) is str:
            for node in self.edges:
                if node == right:
                    return self
            self.edges[right] = {}
            return self
        
        elif type_as_str(self) == 'graph.Graph' and type(right) is tuple and self.is_legal_edge_value(right[2]):
            for node in self.edges:
                if node == right[0]:
                    if right[1] in self.edges[node]:
                        self.edges[right[0]][right[1]] = right[2]
                        break
                    else:
                        self.edges[right[0]][right[1]] = right[2]
                        self.edges[right[1]] = {}
                        break
            return self
        
        else:
            raise GraphError('Could not add two arguments')
     
    def __setattr__(self,name,value):
        try:
            if self.__dict__['is_legal_edge_value']: pass
        except:
            self.__dict__[name] = value
        else:
            raise AssertionError('Attributes already set')
 
if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test DictList before doing bsc tests

#     print('Start simple testing')
#     g = Graph( (lambda x : type(x) is int), ('a','b',1),('a','c',3),('b','a',2),('d','b',2),('d','c',1),'e')
#     print(g)
#     print(g['a'])
#     print(g['a','b'])
#     print(g.node_count())
#     print(len(g))
#     print(g.out_degree('c'))
#     print(g.in_degree('a'))
#     print('c' in g)
#     print(('a','b') in g)
#     print(('a','b',1) in g)
#     print(g('c'))
#     print(g.reverse())
#     print(g.natural_subgraph('a','b','c'))
#     print()    
     
    import driver
    driver.default_file_name = 'bscp22W21.txt'
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
