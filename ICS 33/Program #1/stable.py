# Submitter: edtrinh(Trinh, Eric)
import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    pref = {}
    for line in open_file:
        data = line.rstrip().split(';')
        pref[data[0]] = [None,data[1:]]
    return dict(zip([i for i in sorted(pref)],[pref[i] for i in sorted(pref)]))
        

def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    return ''.join(f'  {x} -> {d[x]}\n' for x in sorted([item for item in d],key=key,reverse=reverse))


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return [x for x in order if x==p1 or x==p2][0]


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return set([(man, men[man][0]) for man in men])


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    m_copy, w_copy = men.copy(), women.copy()
    if trace == True: print(f'Women Preferences\n{dict_as_str(w_copy)}\nMen Preferences\n{dict_as_str(m_copy)}')
    single = set(m_copy.keys())
    while True:
        if trace == True: print(f'unmatched men = {single}\n')
        m = single.pop()
        m_pick = m_copy[m][1].pop(0)
        if w_copy[m_pick][0] == None:
            w_copy[m_pick][0] = m
            m_copy[m][0] = m_pick
            if trace == True:
                print(f'{m} proposes to {m_pick}, who is currently unmatched and accepts the proposal')
                if single != set(): print(f'\n{dict_as_str(m_copy)}')
        elif w_copy[m_pick][1].index(m) < w_copy[m_pick][1].index(w_copy[m_pick][0]):
            single.add(w_copy[m_pick][0])
            m_copy[w_copy[m_pick][0]][0] = None
            w_copy[m_pick][0] = m
            m_copy[m][0] = m_pick
            if trace == True:
                print(f'{m} proposes to {m_pick}, who is currently matched and accepts the proposal (likes new match better)')
                if single != set(): print(f'\n{dict_as_str(m_copy)}')
        else:
            single.add(m)
            if trace == True:
                print(f'{m} proposes to {m_pick}, who is currently matched and rejects the proposal (likes current match better)')
                if single != set(): print(f'\n{dict_as_str(m_copy)}')
        if single == set(): break
    return extract_matches(m_copy)
  
    
if __name__ == '__main__':
    # Write script here
    m_file = input('Furnish any file name containing the preferences of the men: ')
    w_file = input('Furnish any file name containing the preferences of the women: ')
    m_pref = read_match_preferences(open(m_file))
    w_pref = read_match_preferences(open(w_file))
    print('\nMen Preferences')
    print(dict_as_str(m_pref))
    print('Women Preferences')
    print(dict_as_str(w_pref))
    trace = input('Furnish Trace of Execution[True]: ').rstrip()
    print()
    if trace == 'False':
        result = make_match(m_pref,w_pref,False)
        print(f'matches = {result}')
    else:
        result = make_match(m_pref,w_pref,True)
        print(f'\nExecution traced, the final matches = {result}')
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
