# Submitter: edtrinh(Trinh, Eric)
import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    friends = defaultdict(set)
    for line in open_file:
        peeps = line.rstrip().split(';')
        if len(peeps) <= 1:
            friends[peeps[0]] = set()
        else:
            friends[peeps[0]].add(peeps[1])
            friends[peeps[1]].add(peeps[0])
    return dict(friends)


def graph_as_str(graph : {str:{str}}) -> str:
    return ''.join(sorted([f'  {rel} -> {sorted(list(graph[rel]))}\n'for rel in graph]))


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    infl_dict = {}
    for person in graph:
        infl_dict[person] = []
        if len(graph[person]) == 0: infl_dict[person].append(-1)
        else: infl_dict[person].append(len(graph[person])-ceil(len(graph[person])/2))
        infl_dict[person].append(len(graph[person]))
        infl_dict[person].append(person)
    while True:
        candidates = [tuple(infl_dict[person]) for person in infl_dict if infl_dict[person][0] >= 0]
        if trace:
            print(f'\ninfluencer dictionary = {infl_dict}')
            print(f'removal candidates = {candidates}')
        if candidates == []: break
        else:
            removed = min(candidates)
            del infl_dict[removed[2]]
            for friend in graph[removed[2]]:
                if friend in infl_dict:
                    infl_dict[friend][0] -= 1
                    infl_dict[friend][1] -= 1
            if trace:
                print(f'{removed} is the smallest candidate')
                print(f"Removing {removed[2]} as key from influencer dictionary, also subtracting 1 from every friend's value")
    return set(infl_dict)


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    for i in influencers: 
        if i not in graph: raise ValueError
    followed = {}
    initial_len = len(influencers)
    index = len(influencers)
    for friend in graph:
        if friend in influencers: followed[friend] = True
        else: followed[friend] = False
    while True:
        for friend in followed:
            if followed[friend] == False and len(graph[friend]) != 0:
                n = 0
                for person in graph[friend]:
                    if followed[person] == True: n += 1
                if (n/len(graph[friend])) >= 0.5:
                    index += 1
                    followed[friend] = True
        if initial_len == index: break
        else: initial_len = index
    return set([friend for friend in followed if followed[friend] == True])


if __name__ == '__main__':
    # Write script here
    g_file = input('Furnish any file name containing a friendship graph: ')
    print('Graph: person -> [friends of person]')
    graph = read_graph(open(g_file))
    print(graph_as_str(graph))
    trace = eval(input('\nFurnish Trace of Execution[True]: ').rstrip())
    result = find_influencers(graph,trace)
    print(f'The influencers set is {result}')
    while True:
        try:
            sub = input(f"\nFurnish any subset (or enter done to stop)[{result}]: ").rstrip()
            if sub == 'done': break
            elif sub == '':
                influenced = all_influenced(graph,set(graph))
                print(f'People influenced by furnished subset ({100*len(influenced)/len(graph)}% of graph) = {influenced}')
            else:
                influenced = all_influenced(graph,eval(sub))
                print(f'People influenced by furnished subset ({100*len(influenced)/len(graph)}% of graph) = {influenced}')
        except:
            print(f"  Entry Error: '{sub}';\n  Please enter a legal String")
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

