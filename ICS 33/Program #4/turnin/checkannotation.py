# Submitter: edtrinh(Trinh, Eric)
from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self,check,param,value,check_history):
        failed = 0
        for annot in self._annotations:
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 


class Check_Annotation:
    # Start with binding the class attribute to True allowing checking to occur
    #   (but only it the object's attribute self._checking_on is bound to True)
    checking_on  = True
  
    # To check the decorated function f, first bind self._checking_on as True
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        self._args = {}
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        def check_list_tuple(check_history):
            assert isinstance(value,type(annot)), f"\'{param}\' failed annotation check(wrong type): " + \
              f"value = {value}\n  was type {type_as_str(value)} ...should be type {type_as_str(annot)}"
            if len(annot) == 1:
                for i in range(len(value)):
                    index = str(check_history)
                    check_history += f"\n{type_as_str(annot)}[{i}] check: {annot[0]}"
                    self.check(param,annot[0],value[i],check_history)
                    check_history = index
            elif len(annot) > 1:
                assert len(annot) == len(value), f"\'{param}\' failed annotation check(wrong number of elements): " + \
                  f"value = {value}\n  annotation had {len(annot)} element(s){annot}"
                for i in range(len(value)):
                    index = str(check_history)
                    check_history += f"\n{type_as_str(annot)}[{i}] check: {annot[i]}"
                    self.check(param,annot[i],value[i],check_history)
                    check_history = index
        
        def check_dict(check_history):
            assert isinstance(value,dict), f"\'{param}\' failed annotation check(wrong type): " + \
              f"value = {value}\n  was type {type_as_str(value)} ...should be type {type_as_str(annot)}"
            if len(annot) > 1:
                assert False, f"\'{param}\' annotation inconsistency: dict should have 1 item but had {len(annot)}" + \
                  f"\n  annotation = {annot}"
            elif len(annot) == 1:
                key_annot,val_annot = next(iter(annot.keys())),next(iter(annot.values()))
                for key,val in value.items():
                    index = str(check_history)
                    check_history += f"\ndict key check: {key_annot}"
                    self.check(param,key_annot,key,check_history)
                    check_history = index
                    index = str(check_history)
                    check_history += f"\ndict value check: {val_annot}"
                    self.check(param,val_annot,val,check_history)
                    check_history = index
        
        def check_set_frozenset(check_history):
            assert isinstance(value,type(annot)), f"\'{param}\' failed annotation check(wrong type): " + \
              f"value = {value}\n  was type {type_as_str(value)} ...should be type {type_as_str(annot)}"
            assert len(annot) == 1, f"\'{param}\' annotation inconsistency: {type_as_str(value)} should have 1 item but had {len(annot)}" + \
              f"\n  annotation = {annot}"
            ann = next(iter(annot))
            for val in value:
                index = str(check_history)
                check_history += f"\n{type_as_str(value)} value check: {ann}"
                self.check(param,ann,val,check_history)
                check_history = index
        
        def check_function(check_history):
            assert len(inspect.signature(annot).parameters) == 1, f"\'{param}\' annotation inconsistency: predicate should have 1 parameter" + \
              f" but had {len(inspect.signature(annot).parameters)}\n  predicate = {annot}"
            try:
                assert annot(value), f"\'{param}\' failed annotation check: value = {value}\n  predicate = {annot}" + check_history
            except AssertionError:
                raise
            except BaseException as e:
                assert False, f"\'{param}\' annotation predicate({annot}) raise exception\n  exception = " + \
                  f"{e.__class__.__name__}: {e}" + check_history
            
        def check_str(annot):
            try:
                org_annot = str(annot)
                arg_dict = {}
                for arg in self._args:
                    if arg in annot:
                        arg_dict[arg] = self._args[arg]
                        if type(self._args[arg]) is str:
                            index = "\'" + str(self._args[arg]) + "\'"
                        else:
                            index = str(self._args[arg])
                        annot = annot.replace(arg,index)
                assert eval(annot), f"\'{param}\' failed annotation check(str predicate: \'{org_annot}\')" + \
                  f"\n  args for evaluation: " + ', '.join([f"{arg}->{arg_dict[arg]}" for arg in arg_dict])
            except AssertionError:
                raise
            except BaseException as e:
                assert False, f"\'{param}\' annotation check(str predicate: \'{org_annot}\') raised exception" + \
                  f"\n  exception = {e.__class__.__name__}: {e}" + check_history
            
        def check_other(check_history):
            try:
                annot.__check_annotation__(self.check,param,value,check_history)
            except AttributeError:
                assert False, f"\'{param}\' annotation undecipherable: {annot}"
            except BaseException as e:
                raise
        # Start with matching check's function annotation with its arguments
        if annot is None:
            pass
        elif type(annot) is type:
            if type(value) is str: value = "\'" + value + "\'"
            assert isinstance(value,annot), f"\'{param}\' failed annotation check(wrong type): " + \
              f"value = {value}\n  was type {type_as_str(value)} ...should be type {annot.__name__}" + \
              check_history
        elif isinstance(annot,list) or isinstance(annot,tuple):
            check_list_tuple(check_history)
        elif isinstance(annot,dict):
            check_dict(check_history)
        elif isinstance(annot,set) or isinstance(annot,frozenset):
            check_set_frozenset(check_history)
        elif inspect.isfunction(annot):
            check_function(check_history)
        elif isinstance(annot,str):
            check_str(annot)
        else:
            check_other(check_history)
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return the parameter/argument bindings via an OrderedDict (derived
        #   from dict): it binds the function header's parameters in their order
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        self._args = param_arg_bindings()
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if not (self._checking_on and self.checking_on):
            return self._f(*args,**kargs)
        try:
            # For each detected annotation, check if the parameter satisfies it
            for para in self._f.__annotations__:
                if not para == 'return':
                    self.check(para,self._f.__annotations__[para],self._args[para])
            # Compute/remember the value of the decorated function
            self._args['_return'] = self._f(*args,**kargs)
            # If 'return' is in the annotation, check it
            if 'return' in self._f.__annotations__:
                self.check('return',self._f.__annotations__['return'],self._args['_return'])
            # Return the decorated answer
            return self._args['_return']
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
#     def f(x:int): pass
#     f = Check_Annotation(f)
#     f(3)
#     f('a')
               
    #driver tests    
    import driver
    driver.default_file_name = 'bscp4W21.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
