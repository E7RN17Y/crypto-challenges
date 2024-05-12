
def quadratic_residues(p):
    for i in range(1,p):
        if (i**2)%p in [14,6,11]:
            return i
       

print(quadratic_residues(29))