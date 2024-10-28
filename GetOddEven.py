# Both use this to iterate a range and return a list.
get_s2_iteration_list = lambda first,last: [i for i in range(first,last+1,2)] #+1 to include last



### GETS EVEN NUMBERS
def get_even(first,last):
    # If the 1st isnt even, the step=2 will give odd numbers
    if(first%2!=0): first+=1 # To fix that, increase 1

    #returns list
    return get_s2_iteration_list(first,last)
##



### GETS ODD NUMBERS
def get_odd(first,last):
    # If the 1st isnt odd, the step=2 will give even numbers
    if(first%2==0): first+=1 # To fix that, increase 1

    #returns list
    return get_s2_iteration_list(first,last)
##