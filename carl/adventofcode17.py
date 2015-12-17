s = [20, 15, 10, 5, 5]
s = [11 ,30 ,47 ,31 ,32 ,36 ,3 ,1 ,5 ,3 ,32 ,36 ,15 ,11 ,46 ,26 ,28 ,1 ,19 ,3]
s.sort()
print s


def count_possible(sizes, total, sum=0):
    count = 0
    c_idx = 0
    for i in sizes:
        c_idx += 1
        sum_tmp = sum + i
        if sum_tmp == total:
            count += 1
        elif sum_tmp > total:
            break
        count += count_possible(sizes[c_idx:], total, sum_tmp)
    return count

print count_possible(s, 150)

# solution 2 - also can be used for solution 1


# when you have {} as default param it is always pass by reference
# so this method will run just once with the correct results :)
# but is fast because no copying of the depth_counter
def count_possible_depth(sizes, total, sum=0, depth=0, depth_counter={}):
    depth += 1
    c_idx = 0
    for i in sizes:
        c_idx += 1
        sum_tmp = sum + i
        if sum_tmp == total:
            if depth not in depth_counter:
                depth_counter[depth] = 0
            depth_counter[depth] += 1
        elif sum_tmp > total:
            break
        count_possible_depth(sizes[c_idx:], total, sum_tmp, depth)
    return depth_counter


d = count_possible_depth(s, 150)
print sum(d.values())
print d[min(d.keys())]

