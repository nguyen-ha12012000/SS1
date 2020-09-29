def abb():
    full_name = input("Enter your fullname: ")
    arr1 = full_name.split()
    for arr in arr1:
        for i in arr[0]:
            if i == arr[0]:
                i = arr[0].upper()
                print(i, end='.', sep='.')

abb()
