try:

    file = open("data.txt","w")
    file.write("Data informations")
    file.close()


    file = open("data.txt","r")
    content = "data informations"
    print(content)

except FileNotFoundError:

    print("File Not Found.")

else:

    print("File found successfully!")