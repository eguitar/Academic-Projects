
from zip_tree import ZipTree
from CFloat import CFloat


def best_fit(items: [float], assignment: [int], free_space: [float]):
	# pass
	bin_index = 0

	tree = ZipTree()
	tree.insert(CFloat(1.0), bin_index)

	free_space.append(1.0)

	for i in range(len(items)):

		fit_key = tree.find_best(CFloat(items[i]))

		if fit_key == None:
			bin_index += 1
			tree.insert(CFloat(1.0 - items[i]), bin_index)
			assignment[i] = bin_index
			free_space.append(1.0 - items[i])
		else:
			bin_id = tree.find(fit_key)
			tree.remove(fit_key)
			new_key = fit_key - CFloat(items[i])
			tree.insert(new_key, bin_id)
			assignment[i] = bin_id
			free_space[bin_id] = fit_key.val - items[i]

		# print(items[i])
		# print(assignment)
		# print(free_space)
		# print()


def best_fit_decreasing(items: [float], assignment: [int], free_space: [float]):
	best_fit(sorted(items, reverse = True), assignment, free_space)