# Defined below is a special exception for use with the Graph class methods
# Use it like any exception: e.g., raise GraphError('Graph.method" ...error indication...')
 
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
        pass


    # Put all other methods here




 
if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test DictList before doing bsc tests

    print('Start simple testing')
    g = Graph( (lambda x : type(x) is int), ('a','b',1),('a','c',3),('b','a',2),('d','b',2),('d','c',1),'e')
    print(g)
    print(g['a'])
    print(g['a','b'])
    print(g.node_count())
    print(len(g))
    print(g.out_degree('c'))
    print(g.in_degree('a'))
    print('c' in g)
    print(('a','b') in g)
    print(('a','b',1) in g)
    print(g('c'))
    print(g.reverse())
    print(g.natural_subgraph('a','b','c'))
    print()    
     
    import driver
    driver.default_file_name = 'bscp22W21.txt'
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
