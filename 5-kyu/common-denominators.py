from math import lcm
def convert_fracts(lst):
    ls = lcm(*[x[1] for x in lst])
    return [[n[0]*(ls//n[1]), ls] for n in lst]
