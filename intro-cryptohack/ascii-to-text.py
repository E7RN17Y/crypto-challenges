import sys

if sys.version_info.major ==2:
    print("You are running python 2 which is no longer supported.Please upgrade to python 3")

ascii_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("".join(chr(x) for x in ascii_list))