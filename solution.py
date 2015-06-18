from generate_problem import list_gen

listing = list_gen()

def uniques(lists):
    uniqs = []
    for listing in lists:
        for i in listing:
            if not i in uniqs:
                uniqs.append(i)
    return uniqs

def occurred(lists):
    occur = {}
    for ind,listing in enumerate(lists):
        for i in listing:
            if not i in occur.keys():
                occur[i] = [ind]
            else:
                if not ind in occur[i]:
                    occur[i].append(ind)
    return occur

#brute force solution
def pairs(occur):
    pairs = []
    potential_pairs = {}
    for key in occur.keys()[:len(occur)/2]:
        for other_key in occur:
            if key == other_key:
                continue
            for val in occur[key]:
                if val in occur[other_key]:
                    pot_key = key+"_"+other_key
                    if not pot_key in potential_pairs.keys():
                        potential_pairs[pot_key] = 1
                    else:
                        potential_pairs[pot_key] += 1
                    
    for keys in potential_pairs.keys():
        if potential_pairs[keys] >= 50:
            keyz = keys.split("_")
            if not (keyz[0],keyz[1]) in pairs:
                if not (keyz[1],keyz[0]) in pairs:
                    pairs.append((keyz[0],keyz[1]))
    return pairs

occur = occurred(listing)
print len(pairs(occur))
