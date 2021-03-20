import sys


def byter():
    mod_file = input("Please enter the name of the file you want to modify: ")
    by_bytes = 16
    while True:
        by_holder = input("Please enter the number of bytes to go by (leave blank for 16): ")
        if len(str(by_holder).strip()) != 0:
            try:
                by_bytes = int(by_holder)
                break
            except Exception as e:
                print("Didn't get empty input, or input with actionable number. Instead got ", str(by_bytes), " please retry entry.\n", e)
        else:
            break

    with open(mod_file, "rb") as mf:
        with open(str(mod_file).rsplit(".", 1)[0] + "_eat." + str(mod_file).rsplit(".", 1)[1], "wb+") as to_file:
            my_byte = mf.read()
            cur_num = 0
            to_file.write(bytes([my_byte[cur_num]]))
            while True:
                try:
                    cur_num += by_bytes
                    to_file.write(bytes([my_byte[cur_num]]))
                except:
                    break

    print("Used byte count: ", by_bytes)
    print("Finished auditing {0}\n".format(mod_file))


while True:
    option = input("Please choose an option\n[1] Byter\n[2] Exit Program\nSelection: ")
    try:
        if option == "1":
            byter()
        elif option == "2":
            sys.exit()
        else:
            print("\n")
    except Exception as e:
        print(e)
