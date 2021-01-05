
def get_phonenum(prefix, k,used=set()):

    global total_count
    

    if (k == 0) :
        print(prefix) 
        total_count += 1
        return 
  
    for i in range(10):
        if i not in used:
            used.add(i) 
            newPrefix = prefix + str(i)

            get_phonenum(newPrefix, k - 1,used)
        used =set()
    return 
  
# Driver Code 
if __name__ == "__main__":
    total_count = 0

    k = 3

    get_phonenum("",k)
    print(total_count)


      

