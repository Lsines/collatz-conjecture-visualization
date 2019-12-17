
def collage_pairs(x):
   
    checker = {}  # dictionary to store  values1

     # the maximum number in the Collatz algorithm check 
    for x in range(2,x+1):                            # loop from 2 to the input number
        counter = 0
        y = x
        while y > 1:                                       # while Loop to find the number of steps
            if y in checker:
                counter = checker[y] + counter
                break

            while y % 2 == 1:
                y = (3*y+1)/2
                counter +=2
            while y%2 == 0:
                y= y/2
                counter+=1 
        checker[x] = counter
   
    return checker





