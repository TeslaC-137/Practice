def permutationHelper(string, word = '', container = set()):
    if string == '':
        container.add(word)
        return
    for i in range(len(string)):
        permutationHelper(string[:i]+string[i+1:], word+string[i], container)

def permutation(string):
    container  = set()
    permutationHelper(string, '', container)
    return container

permutation('CAT')
