from GetOddEven import get_even,get_odd

### Function for showing examples
def examples(function,str_even_odd):
    print(f'\n\n---------{str_even_odd} Examples:')

    #examples
    for first in range(0,5):
        for last in range(10,14):
            print(f'({first},{last}): {function(first,last)}')
        print('') # Blank line, just to keep it clean
##


## PRINTS EXAMPLES
examples(get_even,"Even")
examples(get_odd,"Odd")