# Submitter: edtrinh(Trinh, Eric)
import goody


def read_fa(file : open) -> {str:{str:str}}:
    fa = {}
    for line in file:
        trans = line.rstrip('\n').split(';')
        fa[trans[0]] = dict(zip(trans[1::2],trans[2::2]))
    return fa


def fa_as_str(fa : {str:{str:str}}) -> str:
    return ''.join(sorted([f'  {trans} transitions: {sorted([(opt, fa[trans][opt]) for opt in fa[trans]])}\n' for trans in fa]))

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    transition = [state]
    index = state
    for i in inputs:
        try:
            transition.append((i,fa[index][i]))
        except:
            transition.append((i,None))
            break
        index = transition[-1][1]
    return transition


def interpret(fa_result : [None]) -> str:
    output = f'Start state = {fa_result[0]}\n'
    for i in range(1,len(fa_result)):
        if fa_result[i][1] == None:
            output += f'  Input = {fa_result[i][0]}; illegal input: simulation terminated\n'
            break
        else:
            output += f'  Input = {fa_result[i][0]}; new state = {fa_result[i][1]}\n'
    if output[-11:] == 'terminated\n':
        output += 'Stop state = None\n'
    else:
        output += f'Stop state = {fa_result[-1][1]}\n'
    return output


if __name__ == '__main__':
    # Write script here
    file_fa = input('Furnish any file name containing a Finite Automaton: ')
    print('\nThe Finite Automaton code as: states and lists of transitions')
    fa = read_fa(open(file_fa))
    print(fa_as_str(fa))
    file_input = input('Furnish any file name containing lines with a start-state and its inputs: ')
    for line in open(file_input):
        inputs = line.rstrip('\n').split(';')
        fa_result = process(fa, inputs[0], inputs[1:])
        print('\nStart tracing FA (from its start-state)')
        print(interpret(fa_result),end='')
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
