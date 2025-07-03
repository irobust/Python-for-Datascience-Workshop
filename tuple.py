
def get_info():
    rec = (1, "john", "doe", 25)
    return rec

def main():
    _ ,name,_, age = get_info()
    print(name) 
    print(age)

main()
