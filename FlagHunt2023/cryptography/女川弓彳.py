with open('sub.txt', 'r', encoding='utf-8') as file:
    ciphertext = file.read()

substitution_map = {
    "女": "a", "川": "b", "弓": "c", "彳": "d", "己": "e", "廾": "f",
    "马": "g", "大": "h", "口": "i", "广": "j", "巛": "k", "飞": "l",
    "辶": "m", "艹": "n", "山": "o", "彐": "p", "宀": "q", "巾": "r",
    "屮": "s", "寸": "t", "门": "u", "彑": "v"
}


plaintext = ""
for char in ciphertext:
    if char in substitution_map:
        plaintext += substitution_map[char]
    else:
        plaintext += char

print(plaintext)
