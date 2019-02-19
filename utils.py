def CDM(x,y):
    import zlib
    return float(len(zlib.compress(x + y))) / float(len(zlib.compress(x)) + len(zlib.compress(y)))