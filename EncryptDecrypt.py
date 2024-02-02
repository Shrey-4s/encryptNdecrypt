
def encrypt(src_file, target_file):
    x = open(src_file, "rt+")
    shrey = open(target_file, "wt+")
    backup = x.readlines()
    x.close()
    lst = []
    i = 0
    for line in backup:
        i += 1
        for word in line:
            word = ord(word) - 69
            lst.append(str(word)+"$#$")

    for k in lst:
        shrey.write(str(k))
    shrey.close()


def decrypt(src_file, target_file):
    x = open(src_file, "rt+")
    shrey = open(target_file, "wt+")
    backup = x.readlines()
    x.close()

    lst = []
    for line in backup:
        data = line.split("$#$")
        lst.append(data)

    for list in lst:
        for ele in list:
            if (ele==""):
                continue
            else:
                a = int(ele) + 69
                shrey.write(chr(a))

    shrey.close()


if __name__ == "__main__":

    print("\nChoose one of the following option.")
    print("1. Encryption\n"
          "2. Decryption")

    a = input("Enter your Response here ")

    if (a=="1"):
        encrypt(input("Enter Source address: "), input("Enter Destination address: "))
        print("Hey SHREYAS, Your Encryption is Done.")

    elif (a=="2"):
        decrypt(input("Enter Source address: "), input("Enter Destination address: "))
        print("Hey SHREYAS, Your Decryption is Done.")

    else:
        print("Error! Enter valid Number.")

