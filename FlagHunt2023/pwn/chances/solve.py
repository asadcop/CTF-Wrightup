corr_bits = ''

distorted = open('out.txt', 'r').read().split('\n')
sz = len(distorted[0])

for pos in range(sz):
    cnt0, cnt1 = 0, 0
    for i in range(50):
        if distorted[i][pos] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
    if cnt0 > cnt1:
        corr_bits += '0'
    else:
        corr_bits += '1'

flag = ''
for i in range(0, len(corr_bits), 8):
    c = corr_bits[i: i + 8]
    flag += chr(int(c, 2))
    
print(flag)