# Submitter: edtrinh(Trinh, Eric)
import re, traceback, keyword, inspect

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
    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    legal_pat = r'^[A-Za-z](\w)*$'
    if not type(type_name) is str:
        raise SyntaxError('type_name is not a string')
    if type_name in keyword.kwlist:
        raise SyntaxError('type_name is a Python keyword')
    if re.match(r'^[A-Za-z](\w)*$', type_name) == None:
        raise SyntaxError('type_name does not follow char specifications')

    if not type(field_names) in [list, str]:
        raise SyntaxError('field_names is not a list or string')
    elif type(field_names) is list:
        fields = [name for name in unique(field_names)]
    elif type(field_names) is str:
        fields = re.split(r'(?:, *| +)',field_names)
        if '' in fields: raise SyntaxError('field_names is not legally split with mix of commas and spaces')
    for field in fields:
        if field in keyword.kwlist:
            raise SyntaxError('field_names has a Python keyword')
        if re.match(r'^[A-Za-z](\w)*$', field) == None:
            raise SyntaxError('field_names does not follow char specifications')
    
    for d in defaults:
        if d not in fields:
            raise SyntaxError('key(s) of defaults not in field_names')

    class_type = 'import inspect\nclass {name}:\n    _fields = {fields}\n    _mutable = {mutable}\n'
    class_type = class_type.format(name = type_name, fields = fields, mutable = mutable)   
      
    class_init = '    def __init__(self, {para}):\n'.format(para = ', '.join(fields)) 
    for field in fields:
        if field in defaults:
            class_init += '        self.{field} = {val}\n'.format(field = field, val = defaults[field])
        else:
            class_init += '        self.{field} = {field}\n'.format(field = field)
            
    class_repr = "    def __repr__(self):\n        return '{name}({para})'.format({format})\n"
    fields_str = ','.join([f'{i}='+'{'+f'{i}'+'}' for i in fields])
    format_str = ','.join([f'{i} = self.{i}'for i in fields])
    class_repr = class_repr.format(name=type_name,para=fields_str,format = format_str)
     
    class_method = '\n'.join(['    def get_{field}(self):\n        return self.{field}'.format(field = i) for i in fields]) + '\n'
    
    class_getitem = '    def __getitem__(self,index):\n        try:\n            if type(index) is str:\n' + \
      "                return eval('self.get_{j}()'.format(j=index))\n            else:\n"
    for i in range(len(fields)):
        if i == 0:
            class_getitem += "                if index == {i}:\n".format(i=i) + \
              "                    return eval('self.get_{j}()'"+".format(j=self._fields[{i}]))\n".format(i=i)
        else:
            class_getitem += "                elif index == {i}:\n".format(i=i) + \
              "                    return eval('self.get_{j}()'"+".format(j=self._fields[{i}]))\n".format(i=i)
    class_getitem += '                else:\n                    raise IndexError\n'  
    class_getitem += "        except IndexError:\n            raise IndexError('Attribute index out of range')\n" + \
      "        except TypeError:\n            raise IndexError('Attribute index invalid type')\n" + \
      "        except:\n            raise IndexError('Attribute index does not exist in attributes')\n"
    
    class_eq = "    def __eq__(self,right):\n        return type(self) == type(right) " + \
      "and all([self.__getitem__(x) == right.__getitem__(y) for x,y in zip(self._fields,right._fields)])\n"
  
    class_asdict = \
      '    def _asdict(self):\n        return self.__dict__\n'
    
    class_make = "    def _make(iterable):\n        return eval('{type}'".format(type = type_name) + \
      "+'(*{para})'.format(para = iterable))\n"
    
    class_replace = '    def _replace(self,**kwargs):\n        for arg in kwargs:\n            ' + \
      'if not arg in self._fields:\n                raise TypeError\n'
    class_replace += \
      "        if self._mutable:\n            para = dict(self.__dict__)\n            " + \
      "for item in kwargs.items():\n                para[item[0]] = item[1]\n            self.__init__(*para.values())\n" + \
      "        else:\n            para = dict(self.__dict__)\n            for item in kwargs.items():\n            " + \
      "    para[item[0]] = item[1]\n            return {type}".format(type=type_name)+"(*para.values())\n"
          
    class_setattr = '    def __setattr__(self,attr,value):\n        ' + \
      'code_calling = inspect.currentframe().f_back.f_code.co_name\n        ' + \
      "if code_calling == '__init__' or self._mutable: self.__dict__[attr] = value\n        " + \
      "else: raise AttributeError('Attempting to setattr outside of __init__')\n"
    
    class_definition = class_type + class_init + class_repr + class_method + class_getitem + \
                       class_eq + class_asdict + class_make + class_replace + class_setattr

    # Debugging aid: uncomment show_listing, displays source code for the class
    # show_listing(class_definition)
    
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
