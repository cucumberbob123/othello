from Board import Board


size = 6
b = Board(size, size)

w = 'w'
bl = 'b'

b.place(1, size, w)
print(b.toString())

for i in range(2, size):
    print(i)
    b.place(1, i, bl)

print(b.toString())

b.place(1, 1, w)

print(b.toString())

# b.place(1, 5, w)

# print(b.toString())
