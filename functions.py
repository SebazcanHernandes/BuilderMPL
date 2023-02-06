def check_number(x):
    a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(a)):
        if x == a[i]:
            return True
    return False
