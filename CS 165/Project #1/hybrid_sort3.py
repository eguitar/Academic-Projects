from insertion_sort import insertion_sort

def hybrid_sort3(nums):
    h = int(len(nums)**(1/6))
    merge_sort_32(nums,h)
    

def merge_sort_32(nums,h):
    if len(nums) > h:
        mid = int(len(nums)/2)

        left = nums[:mid]
        right = nums[mid:]

        merge_sort_32(left,h)
        merge_sort_32(right,h)

        k = 0
        while len(left) != 0 and len(right) != 0:
            if left[0] <= right[0]:
                nums[k] = left[0]
                left.pop(0)
            else:
                nums[k] = right[0]
                right.pop(0)
            k += 1

        while len(left) != 0:
            nums[k] = left[0]
            left.pop(0)
            k += 1

        while len(right) != 0:
            nums[k] = right[0]
            right.pop(0)
            k += 1
    else:
        insertion_sort(nums)


# if __name__ == "__main__":
# 	arr = [37, 24, 40, 63, 58, 80,  1, 95, 30, 57, 65, 92, 32, 20,  9,  5, 82, 79, 51, 72, 11, 22, 34, 94, 99, 29, 81, 17, 19, 89, 66,  8, 36, 43, 97, 67, 46, 56, 14, 59, 21, 12, 44, 27, 73, 42,  4, 96, 93,  7,  2, 87, 83,100, 77, 69, 60, 49, 41, 75, 64, 68, 74, 85, 76, 88, 53,  6, 16, 45, 62, 86, 38, 61, 54, 70, 91, 15, 39, 98, 25, 48, 90, 71, 26, 50, 13, 35, 23, 18, 52, 10,  3, 55, 33, 28, 78, 84, 47, 31]
# 	hybrid_sort3(arr)
# 	for i in range(0,len(arr)):
# 		print(arr[i])