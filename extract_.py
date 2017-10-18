# Slighly modded from code @
# https://github.com/AlexAltea/cetrainer-unpacker/tree/a17a
import sys

# Unpackers
from unpackers import unpack_cet_mrantifun

# Decrypts the .CETRAINER file
def decrypt(pathin, pathout):
    """
    Decrypts the .CETRAINER file
    @param[in]  pathin   Path to the input .CETRAINER file
    @param[in]  pathout  Path to the output .CETRAINER file
    """
    # Read data
    fin = open(pathin, "rb")
    data = bytearray(fin.read())
    fin.close()

    result = None
    try:
        result = unpack_cet_mrantifun.decrypt(data[:])
        print("[*] Success!")
    except Exception as e:
        print("[*] Failed!")

    # Write data
    if not result:
        print("[!] Could not decrypt the CETRAINER file")
    else:
        print("[*] Writing: " + pathout)
        fout = open(pathout, "wb")
        fout.write(result)
        fout.close()


SCRIPT_USAGE = """CheatEngine Trainer Unpacker
About:    This program decrypts MrAntiFun's CheatEngine's .CETRAINER files
Version:  2017-03-12
Usage:    extract.py path/to/CET_TRAINER.CETRAINER
          will output to path/to/CET_TRAINER.CETRAINER.xml
"""

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(SCRIPT_USAGE)
    else:
        path = sys.argv[1]
        decrypt(path, path + ".xml")
