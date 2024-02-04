def sum_pairs(arr, num):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pair = [arr[i], arr[j]]
            pairs.append(pair)
    sum_of_pairs = {}
    for i in pairs: 
        summation = sum(i)
        i = tuple(i)
        sum_of_pairs[i] = summation
    sums_that_match = []
    for pair, value in sum_of_pairs.items():
        if num == value:
            pair = list(pair)
            sums_that_match.append(pair)
    if len(sums_that_match) == 0: 
        return 'unable to find pairs'
    else: 
        return sums_that_match 
            


         

    #add the sum 
    #compare the sum to num 
    # if the sum is equal append to a new list
    # else statement if len of my list is false return "could not find pair"
    


print(sum_pairs([1,2,3,4,5], 9))