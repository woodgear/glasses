from os.path import basename
import pdbparse
import sys

def hex2guid(r):
    new = bytes([r[3],r[2],r[1],r[0],r[5],r[4],r[7],r[6],*r[8:]])
    hexstr = new.hex()
    return "{" +f"{hexstr[0:8].upper()}-{hexstr[8:12].upper()}-{hexstr[12:16].upper()}-{hexstr[16:20].upper()}-{hexstr[20:].upper()}"+"}"
    pass

def main(pdbfilepath):
    pdb = pdbparse.parse(pdbfilepath, fast_load=True)
    if len(sys.argv) > 2:
        streams = [pdb.streams[int(i)] for i in sys.argv[2:]]
    else:
        streams = pdb.streams
    print(pdbfilepath)
    for stream in streams:
        if stream.index == 1:
            raw = stream.data[12:28]
            print(hex2guid(raw))

        if stream.index == 1:
            break



if __name__ == "__main__":
    main(sys.argv[1])
