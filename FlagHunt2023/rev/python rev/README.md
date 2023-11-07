
> python pyinstxtractor.py mugiwara

[+] Processing mugiwara 

[+] Pyinstaller version: 2.1+

[+] Python version: 3.8

[+] Length of package: 3046989 bytes

[+] Possible entry point: mugiwara.pyc

[+] Successfully extracted pyinstaller archive: mugiwara

> pycdc mugiwara.pyc


```
for egg in eggs:
    if catcher_rect.colliderect(egg['rect']):
        eggs.remove(egg)
        score += 10
        continue
        for egg in eggs:
            if egg['rect'].y >= canvas_height:
                egg_dropped(egg)
                continue
                pygame.display.flip()
                clock.tick(60)
                continue
                flag = ''
                flag_chars = list(flag)
                result = []
                for i in range(len(flag)):
                    if i > 0:
                        flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i - 1]))
                    flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 4)
                    flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 3)
                    flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 2)
                    flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 1)
                    result.append(format(ord(flag_chars[i]), '02x'))
                print(''.join(result))
                enc_flag = b'723c59047424672f481c723561265b02780067241b41163e680a4151475e3a'
                return None
"""


enc_flag = '723c59047424672f481c723561265b02780067241b41163e680a4151475e3a'

def generate_result(flag):
    flag_chars = list(flag)
    result = []
    for i in range(len(flag)):
        if i > 0:
            flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i - 1]))
        flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 4)
        flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 3)
        flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 2)
        flag_chars[i] = chr(ord(flag_chars[i]) ^ ord(flag_chars[i]) >> 1)
        result.append(format(ord(flag_chars[i]), '02x'))
    return ''.join(result)

head = 'CTF_BD{'

possible_flag_values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-_{}"

while True:
    for char in possible_flag_values:
        new_head = head + char
        result = generate_result(new_head)
        index = len(new_head)*2
        if result == enc_flag[:index]:
            print(new_head)
            head = new_head
            new_result = result
```
