def get_phonenum(prefix, k):

    global total_count
    adjacent_nums = {
        1: {2, 4},
        2: {1, 3, 5},
        3: {2, 6},
        4: {1, 5, 7},
        5: {2, 4, 6, 8},
        6: {5, 9},
        7: {4, 8},
        8: {5, 7, 9, 0},
        9: {6, 8},
        0: {8}
    }
    if (k == 0):
        if len(set(prefix)) == len(prefix):
            # print(prefix)
            total_count += 1
        return

    for i in range(10):
        if(prefix is "" or i in adjacent_nums[int(prefix) % 10]):
            newPrefix = prefix + str(i)
            get_phonenum(newPrefix, k - 1)
    return

# Driver Code
if __name__ == "__main__":
    total_count = 0
    k = 1
    get_phonenum("",k)
    print("Total possibilities with length %d are %d "%(k,total_count))


      

