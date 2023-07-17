
def longestChain(words):
    for i in range(len(words)):
        w = list(words[i])
        w.sort()
        words[i] = ''.join(w)

    tmp = words[:]
    t = words[:]

    chains = [1] * len(words)

    for i in range(len(words)- 2):
        for j in range(i+1, len(words)):
            if tmp[i] in tmp[j] :
                t[j] = t[j].replace(t[i], '')
                words[j] = tmp[j].replace(t[j], '')
                chains[j] += 1
    
    return max(chains)

print(longestChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']))
# print(longestChain(['zxb', 'bca', 'bda', 'bdca', 'zxbe']))
# print(longestChain(['a', 'zxb', 'ba', 'bca', 'bda', 'bdca','zxbe','azxbe', 'azxpbe']))
