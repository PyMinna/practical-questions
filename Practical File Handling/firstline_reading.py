introducing = ["I'm Kadeeja Minna\n",
                "I'm from malappuram\n"]

file = open("firstline.txt", "w")
file.writelines(introducing)
file.close()

file = open("firstline.txt", "r")
content = file.readline()
print(content)

