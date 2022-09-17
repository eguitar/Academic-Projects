def almost_permut(n):
    nums = []
    for i in range(1, n+1):
        nums.append(i)
    return nums

def reverse_permut(n):
    nums = []
    for i in range(n):
        nums.append(n-i)
    return nums


if __name__ == "__main__":
    for i in almost_permut(10):
        print(i)
    print("\n")
    for i in reverse_permut(10):
        print(i)  