import sys

def eea(a, b,s1=1,s2=0,t1=0,t2=1):
    if b == 0:
        return [s1,t1]
    s = s1 - (s2*(a//b))
    t = t1 - (t2*(a//b))
    return eea(b, a%b,s2,s,t2,t)

if __name__ == '__main__':
    args = sys.argv[1:]
    if(len(args) == 2):
        val = eea(int(float(args[0])), int(float(args[1])))
        print(val)
        