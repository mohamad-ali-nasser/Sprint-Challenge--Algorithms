'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if len(word) == 1 or len(word) == 0:
        return 0

    if word[0] == 't' and word[1] == 'h':
        return count_th(word[1:]) + 1

    return count_th(word[1:])
    



print(count_th('abcthxyHThthz'))



    # count = count_th(word) + count_th(word)
    
    # return count
    
    


# listy = list(word)


