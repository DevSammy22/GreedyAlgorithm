def huffman(S, f):
    Q = build_priority_queue(S)
    while Q.size > 1:
        # get first two minimum value in the S
        x = Q.extract_min()
        y = Q.extract_min()

        #let z be the new symbol introduced whose frequency is the sum of fx and fy
        z = (x, y)
        f[z] = f[x] + f[y]
        Q.insert(z, f[z])

    return Q.extract_min()