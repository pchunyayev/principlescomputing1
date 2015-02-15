def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    for iteration in range(0, 26):
        sum = lst[-1] + lst[-2] + lst[-3]
        lst.append(sum)
        
sum_three = [0, 1, 2]
appendsums(sum_three)
print "10: ", sum_three[10]
print "20: ", sum_three[20]