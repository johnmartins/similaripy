import lzma


def ncd_bytes(x: bytes, y: bytes) -> float:
    """
    Calculates the Normalized Compression Distance between two byte-arrays.
    :param x: A file
    :param y: File of the same format as x
    :return:
    """
    z_x = lzma.compress(x)
    z_y = lzma.compress(y)
    z_xy = lzma.compress(x + y)

    NCD = ( len(z_xy) - min(len(z_x), len(z_y)) )  / max(len(z_x), len(z_y))
    return NCD


def ncd(path_x: str, path_y: str) -> float:
    """
    Normalized compression distance between two files.
    :param path_x: Path to target file
    :param path_y: Path to file which we want to compare with file x
    :return:
    """
    with open(path_x, 'rb') as file_x, open(path_y, 'rb') as file_y:
        x = file_x.read()
        y = file_y.read()
        return ncd_bytes(x, y)
