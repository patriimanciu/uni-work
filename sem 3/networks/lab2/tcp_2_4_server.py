import socket
# Intoarce cuvantul cu cele mai multe vocale
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()
array = []
n = int(cs.recv(10).decode())
print(n)
for i in range(n):
    array.append(cs.recv(10).decode())
print(array)

arr = []

for i in range(n):
    j = count_vowels(array[i])
    arr.append(j)

maxx = 0
for i in range(n):
    if arr[i] > maxx:
        maxx = arr[i]

for i in range(n):
    if arr[i] == maxx:
        cs.send(array[i].encode())
        break
cs.close()
