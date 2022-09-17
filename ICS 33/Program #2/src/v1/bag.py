# Submitter: edtrinh(Trinh, Eric)
from collections import defaultdict
from goody import type_as_str
import prompt

class Bag:
    
    def __init__(self,sequence=[]):
        self.bag = defaultdict(int)
        for item in sequence:
            self.bag[item] += 1

    def __repr__(self):
        bag = [key for key,val in self.bag.items() for i in range(val)]
        return f'Bag({bag})'
     
    def __str__(self):
        bag = tuple([f'{key}[{val}]' for key,val in self.bag.items()])
        return f'Bag{bag}'
 
    def __len__(self):
        return sum(self.bag.values())
     
    def unique(self):
        return len(self.bag)
     
    def __contains__(self,arg):
        return arg in self.bag
     
    def count(self,arg):
        if self.__contains__(arg) == False:
            return 0
        else:
            return self.bag[arg]
     
    def add(self,arg):
        if self.__contains__(arg) == False:
            self.bag[arg] = 1
        else:
            self.bag[arg] += 1
     
    def __add__(self,right):
        if type_as_str(self) == 'bag.Bag' and type_as_str(right) == 'bag.Bag':
            self_list = [key for key,val in self.bag.items() for i in range(val)]
            right_list = [key for key,val in right.bag.items() for i in range(val)]
            return Bag(self_list + right_list)
        else:
            raise NotImplemented
                 
    def remove(self,arg):
        if arg in self:
            self.bag[arg] -= 1
            if self.bag[arg] == 0:
                del self.bag[arg]
        else:
            raise ValueError('Argument not in bag.')
     
    def __eq__(self,right):
        if type_as_str(self) == 'bag.Bag' and type_as_str(right) == 'bag.Bag':
            return self.bag == right.bag
        else:
            return False
      
    def __ne__(self,right):
        if type_as_str(self) == 'bag.Bag' and type_as_str(right) == 'bag.Bag':
            return self.bag != right.bag
        else:
            return True
     
    def __iter__(self):  
        class Bag_iter:
            def __init__(self,bag):
                self.items = [item for item in bag for i in range(bag[item])]
                self.n = 0                 
            
            def __next__(self):
                if self.n == len(self.items):
                    raise StopIteration
                index = self.items[self.n]
                self.n += 1
                return index
            
            def __iter__(self):
                return self           
        return Bag_iter(self.bag)


if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)
  
    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    print()
    
    import driver
    driver.default_file_name = 'bscp21W21.txt'
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
