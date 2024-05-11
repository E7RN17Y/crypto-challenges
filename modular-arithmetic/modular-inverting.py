
def inverting_modular(a,p):
    for i in range(0,p):
        if (a*i)%p == 1:
            return i

print(inverting_modular(3,13))