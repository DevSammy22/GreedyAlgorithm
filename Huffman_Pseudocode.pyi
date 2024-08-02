def Huffman(S, f):
    while len(S) > 1:
        x, y = lowest_frequency_symbol(S, f) #find the symbol with the lowest frequency

        # Create a new symbol with the combined frequency of x1 and x2
        z = (x,y) # introduce new symbol which is the addition of x and y
        f[z] = f[x] + f[y] # frequency of a new symbol z is the sum of frequency of x and y

        # Replace x and y in the set with the new symbol
        S.remove(x)
        S.remove(y)
        S.add(z)

    # Return the tree
    return S

def lowest_frequency_symbol(S, f):
    # Sort symbols by their frequencies and return the two smallest ones
    sorted_symbols = sorted(S, key=lambda x:x[f])
    return sorted_symbols[0], sorted_symbols[1]