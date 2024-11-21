def rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    
    return "{:02x}{:02x}{:02x}".format(r,g,b).upper()
