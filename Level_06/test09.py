# 크로아티아 알파벳

c1 = "c="
c2 = "c-"
dz = "dz="
d = "d-"
lj = "lj"
nj = "nj"
s = "s="
z = "z="

alphabet_list = [c1, c2, dz, d, lj, nj, s, z]

str = input()
first_len = len(str)

count = 0
minus_str = ""

for i in alphabet_list:
    while i in str:
        count += 1
        minus_str += i
        str = str.replace(i, "_", 1)
        
print(first_len - len(minus_str) + count)
