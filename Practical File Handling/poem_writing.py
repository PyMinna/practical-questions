poem = [
    "The sun rises in the sky,\n",
    "Birds sing as they fly high.\n",
    "Flowers bloom with colors bright,\n",
    "Nature shines in golden light.\n"
]


file = open("poem.txt", "w")
file.writelines(poem)
file.close()