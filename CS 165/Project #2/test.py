from requirements import *


tree = ZipTree()



	

tree.insert(4, 'a', 0)
tree.insert(5, 'b', 0)
tree.insert(2, 'c', 2)
tree.insert(1, 'd', 1)


print(f'find(4): {tree.find(4)}, Expected: a')
print(f'find(5): {tree.find(5)}, Expected: b')
print(f'find(2): {tree.find(2)}, Expected: c')
print(f'find(1): {tree.find(1)}, Expected: d')

print('\n')

print(f'get_height(): {tree.get_height()}, Expected: 2')

print('\n')

# print(f'get_depth(4): {tree.get_depth(4)}, Expected: 2')
# print(f'get_depth(5): {tree.get_depth(5)}, Expected: 3')
# print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
# print(f'get_depth(1): {tree.get_depth(1)}, Expected: 1')