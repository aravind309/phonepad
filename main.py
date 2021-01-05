def get_phonenum(prefix, k, used=set()):

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
        print(prefix)
        total_count += 1
        return

    for i in range(10):
        if(prefix is "" or i in adjacent_nums[int(prefix) % 10]):
            newPrefix = prefix + str(i)
            get_phonenum(newPrefix, k - 1, used)
    return


# Driver Code
if __name__ == "__main__":
    total_count = 0
    k = 3
    get_phonenum("",k)
    print(total_count)


      

