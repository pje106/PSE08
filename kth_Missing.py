# Input: arr = [2,3,4,7,11], k = 5
# Output: 9

def kth_missing_positive_number(numbers, k):
    #k< first_number
    if k < numbers[0]:
        return k
    
    k = k - (numbers[0] -1)
    # k= 5 - (2-1) = 4

    for i in range(len(numbers)-1):
        if type(numbers[i]) != int:
            raise TypeError("Please input number list")
            
        missing = numbers[i+1]-numbers[i]-1
        
        #i = 3, missing = 4
        if missing >= k:
            return numbers[i] + k
            
            # i = 3, k = 2, missing = 3 
            
        else:
            k -= missing
            #i = 0, k = 4, missing = 0
            #i = 1, k = 4, missing = 0
            #i = 2, k = 2, missing = 3
    return numbers[-1] + k   


