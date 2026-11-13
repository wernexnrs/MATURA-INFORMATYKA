przeslanie = ""

with open("sygnaly.txt") as file:
    slowa = file.read().split()

for i in range(39, len(slowa), 40):
    przeslanie += slowa[i][9]

print(przeslanie)
