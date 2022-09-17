# Submitter: edtrinh(Trinh, Eric)
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for line_number, text_of_line in enumerate(s.split('\n'),1):     
            print(f' {line_number: >3} {text_of_line.rstrip()}')
    def unique(iterable):
        iterated = set()
        for i in iterable:
            if i not in iterated:
                iterated.add(i)
                yield i
    def test_name(arg,name):
        if not type(arg) is str:
            raise SyntaxError('{name} is not a string'.format(name = name))
        if arg in keyword.kwlist:
            raise SyntaxError('{name} is a Python keyword'.format(name = name))
        if re.match(r'^[A-Za-z](\w)*$', arg) == None:
            raise SyntaxError('{name} does not follow char specifications'.format(name = name))
    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    
    test_name(type_name,'type_name')
    
    if not type(field_names) in [list, str]:
        raise SyntaxError('field_names is not a list or string')
    elif type(field_names) is list:
        fields = [name for name in unique(field_names)]
    elif type(field_names) is str:
        print(field_names)
        fields = re.split(r'(,)(  )*',field_names)
        print(fields)
        if None in fields: raise SyntaxError('field_names is not legally split with mix of commas and spaces')
        fields = [i for i in fields if re.match(r'^(\w)+$',i)!=None]
    
    for field in fields:
        test_name(field,f'field_names {field}')
    
    for d in defaults:
        if d not in fields:
            raise SyntaxError('key(s) of defaults not in field_names')
    
    class_type = \
      'class {name}:\n    _fields = {fields}\n    _mutable = {mutable}'.format(name = type_name, fields = fields, mutable = mutable)   
      
    class_init = f'\n    def __init__(self):' 
    for field in fields:
        if field in defaults:
            class_init += '\n        self.{field} = {val}'.format(field = field, val = defaults[field])
        else:
            class_init += '\n        self.{field} = {field}'.format(field = field)
            
    class_repr = \
      f'\n    def __repr__(self):'
      
    class_method = \
      f''
    
    class_getitem = \
      f''
      
    class_asdict = \
      f''
    
    class_make = \
      f''
    
    class_replace = \
      f''
      
    class_setattr = \
      f''
    
    class_definition = class_type + class_init + class_repr + class_method + \
                       class_getitem + class_asdict + class_make + class_replace + class_setattr


    # Debugging aid: uncomment show_listing, displays source code for the class
    show_listing(class_definition)
    
    # Execute class_definition's str within name_space; followed by binding the
    #   attribute source_code to the class_definition; after the try+except
    #   return the created class object; if there were any syntax errors, show
    #   the class and also show the error in the except clause
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )            
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')

    #driver tests
    import driver  
    driver.default_file_name = 'bscp3W21.txt'
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
