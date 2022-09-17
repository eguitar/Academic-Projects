# Submitter: edtrinh(Trinh, Eric)
import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    return {tuple([fq[i] for i in range(q)]) for q in range(len(fq)+1) if q != 0}


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    for pre_que in all_prefixes(new_query): prefix[pre_que].add(new_query)
    query[new_query] += 1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix_que, query_freq = defaultdict(set), defaultdict(int)
    for line in open_file:
        search = tuple(line.rstrip('\n').split(' '))
        query_freq[search] += 1
        for prefix in all_prefixes(search): prefix_que[prefix].add(search)
    return prefix_que, query_freq


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return ''.join(f'  {x} -> {d[x]}\n' for x in sorted([item for item in d],key=key,reverse=reverse))


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    return [search for search in sorted([que for que in query],key=lambda x:(-query[x],x)) if a_prefix in prefix and search in prefix[a_prefix]][:n]


# Script

if __name__ == '__main__':
    # Write script here
    file = input('Furnish any file name containing full queries: ')
    prefix,query = read_queries(open(file))
    print('\nPrefix dictionary:')
    print(dict_as_str(prefix,lambda x: (len(x),x)))
    print('Query dictionary:')
    print(dict_as_str(query,lambda x: (-query[x],len(x),x)))
    while True:
        a_prefix = tuple(input('Furnish any prefix sequence (or done to stop): ').rstrip().split(' '))
        if a_prefix == ('done',): break
        print(f'  Most frequent (up to 3) matching full queries (in order) = {top_n(a_prefix,3,prefix,query)}\n')
        search = tuple(input('Furnish any full query sequence (or done to stop): ').rstrip().split(' '))
        if search == ('done',): break
        add_query(prefix, query, search)
        print('\nPrefix dictionary:')
        print(dict_as_str(prefix,lambda x: (len(x),x)))
        print('Query dictionary:')
        print(dict_as_str(query,lambda x: (-query[x],len(x),x)))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
