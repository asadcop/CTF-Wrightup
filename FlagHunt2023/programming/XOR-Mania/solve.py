import hashlib
import copy

info = open('out.txt', 'r').read().split('\n')
xored, hash = info[:-1], info[-1]

xored = [bytes.fromhex(xor) for xor in xored]
flag_len = len(xored[0])
opts = set(c for c in range(128))

possible_pos = dict()
problematic = []
ans = []

for pos in range(flag_len):
    found = set()
    for itr in range(len(xored)):
        found.add(xored[itr][pos])
    remaining = opts.difference(found)
    sz = len(remaining)
    if sz == 1:
        ans.append(list(remaining)[0])
    else:
        ans.append(0)
        problematic.append(pos)
        possible_pos[pos] = list(remaining)

print(problematic)
print(possible_pos)

def dfs(idx, cur_arr):
    if idx == len(problematic):
        H = hashlib.sha256(bytes(cur_arr)).hexdigest()
        if hash == H:
            print(bytes(cur_arr))
            exit(2)
        return
    else:
        for pos in possible_pos[problematic[idx]]:
            nw_arr = copy.deepcopy(cur_arr)
            nw_arr[problematic[idx]] = pos
            dfs(idx + 1, nw_arr)

dfs(0, ans)
