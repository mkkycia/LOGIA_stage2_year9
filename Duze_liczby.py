def icp(x):
    x = sorted(set(x))
    if len(x) == 2:
        if x[1] == '2' or x[1] == '3' or x[1] == '5' or x[1] == '7':
            return True
    return False

print(icp('11111111111111111111111111111111111111111111111156789'))
