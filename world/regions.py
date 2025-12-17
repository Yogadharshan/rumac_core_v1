def region_of(pos, size=2):
    """
    groups grid into size x size regions
    """
    x, y = pos
    return (x // size, y // size)
