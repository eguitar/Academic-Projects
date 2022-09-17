
from CFloat import CFloat


def next_fit(items: [float], assignment: [int], free_space: [float]):
	bin_index = 0
	free_space.append(CFloat(1.0).val)
	for i in range(len(items)):
		new_float = CFloat(items[i])
		old_float = CFloat(free_space[bin_index])
		if new_float > old_float:
			bin_index += 1
			free_space.append(CFloat(1.0 - items[i]).val)
		else:
			free_space[bin_index] -= CFloat(items[i]).val
		assignment[i] = bin_index