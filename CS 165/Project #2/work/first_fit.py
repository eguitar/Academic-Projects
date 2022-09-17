
from zip_tree import ZipTree
from CFloat import CFloat


def first_fit(items: [float], assignment: [int], free_space: [float]):
	bin_index = 0

	tree = ZipTree()
	tree.insert_sub(bin_index, CFloat(1.0))

	free_space.append(1.0)

	for i in range(len(items)):

		fit_id = tree.find_first(CFloat(items[i]))

		if fit_id == -1:
			bin_index += 1
			tree.insert_sub(bin_index, CFloat(1.0 - items[i]))
			assignment[i] = bin_index
			free_space.append(1.0 - items[i])
		else:
			fit_cap = tree.find(fit_id)
			tree.remove_sub(fit_id)
			new_cap = fit_cap - CFloat(items[i])
			tree.insert_sub(fit_id, new_cap)
			assignment[i] = fit_id
			free_space[fit_id] = fit_cap.val - items[i]


def first_fit_decreasing(items: [float], assignment: [int], free_space: [float]):
	first_fit(sorted(items, reverse = True), assignment, free_space)
	# pass