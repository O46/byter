import sys


def byter():
    mod_file = input("Please enter the name of the file you want to modify: ")
    with open(mod_file, "rb") as mf:
        with open(str(mod_file).rsplit(".", 1)[0] + "_eat." + str(mod_file).rsplit(".", 1)[1], "wb+") as to_file:
            my_byte = mf.read()
            cur_num = 0
            to_file.write(bytes([my_byte[cur_num]]))
            while True:
                try:
                    cur_num += 16
                    to_file.write(bytes([my_byte[cur_num]]))
                except:
                    break
    print("Finished auditing {0}\n".format(mod_file))


while True:
    option = input("Please choose an option\n[1] Byter\n[2] Exit Program\nSelection: ")
    try:
        if int(option) == 1:
            byter()
        elif int(option) == 2:
            sys.exit()
    except Exception as e:
        print(e)
