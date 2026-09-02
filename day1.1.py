try:
    with open("count.txt", "r") as f:
        count=f.read()

except FileNotFoundError:
    count=0

count=str(int(count)+1)
print(count)
with open("count.txt", "w") as f:
    f.write(count)

