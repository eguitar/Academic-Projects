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

    def __check_annotation__(self, check,param,value,check_history):
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
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        def check_list_tuple():
            assert isinstance(value,type(annot)), '??????'
            if len(annot) == 1:
                for i in range(len(value)):
                    self.check(param,annot[0],value[i],check_history)
            elif len(annot) > 1:
                assert len(annot) == len(value), '??????'
                for i in range(len(value)):
                    self.check(param,annot[i],value[i],check_history)
        
        def check_dict():
            assert isinstance(value,dict), '??????'
            if len(annot) > 1:
                raise AssertionError('??????????')
            elif len(annot) == 1:
                key_annot,val_annot = next(iter(annot.keys())),next(iter(annot.values()))
                for key,val in value.items():
                    self.check(param,key_annot,key,check_history)
                    self.check(param,val_annot,val,check_history)
        
        def check_set_frozenset():
            assert isinstance(value,type(annot)), '??????'
            if len(annot) == 1:
                ann = next(iter(annot))
                for val in value:
                    self.check(param,ann,val,check_history)
            elif len(annot) > 1:
                assert len(annot) == len(value), '??????'
                for ann,val in zip(annot,value):
                    self.check(param,ann,val,check_history)
        
        def check_function():
            assert len(inspect.signature(annot).parameters) == 1, '??????????'
            try:
                assert annot(value), '??????????'
            except:
                raise AssertionError('??????????')
            
        def check_str(input):
            print(input)
            print()
            print(param,annot,value)
#             try:
#                 assert eval(annot), '??????????'
#             except:
#                 raise AssertionError('??????????')


#         def check_other():
#             if not hasattr(annot,'__check_annotation__'):
#                 raise AttributeError('??????????????')
#             try:
#                 annot.__check_annotation__()
#             except:
#                 raise AssertionError('??????????')
        # Start with matching check's function annotation with its arguments
        if annot is None:
            pass
        elif type(annot) is type:
            assert isinstance(value,annot), '?????????????????????'
        elif isinstance(annot,list) or isinstance(annot,tuple):
            check_list_tuple()
        elif isinstance(annot,dict):
            check_dict()
        elif isinstance(annot,set) or isinstance(annot,frozenset):
            check_set_frozenset()
        elif inspect.isfunction(annot):
            check_function()
        elif isinstance(annot,str):
            check_str(input_param)
        else:
            pass
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
        input_param = param_arg_bindings()
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if not (self._checking_on and self.checking_on):
            return self._f(*args,**kargs)
        try:
            # For each detected annotation, check if the parameter satisfies it
            print(self._f.__annotations__)
            for para in self._f.__annotations__:
                if not para == 'return':
                    self.check(para,self._f.__annotations__[para],input_param[para])
            # Compute/remember the value of the decorated function
            output = self._f(*args,**kargs)
            # If 'return' is in the annotation, check it
            if 'return' in self._f.__annotations__:
                self.check('_return',self._f.__annotations__['return'],output)
            # Return the decorated answer
            return output
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
            raise #AssertionError






  
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
