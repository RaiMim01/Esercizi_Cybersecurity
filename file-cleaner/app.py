# first and last name: Miriam Raimondi 
# serial number: 176474
#
# path: /home/miriam.rai/file-cleaner/app.py

import argparse
import os
import sys

def walk(basepath, extension):
    for filename in os.listdir(basepath):
        path = os.path.join(basepath, filename)

        if os.path.isfile(path) and path.endswith(extension):
            print(f"removing {path}")
            os.remove(path)
        elif os.path.isdir(path):
            walk(path, extension)


def main():
    parser=argparse.ArgumentParser(description="file cleaner")

    parser.add_argument("--path", type=str, required=True, help="Path dove cercare i file da pulire")
    parser.add_argument("--extension", type=str, required=True, help="Estensione dei file da pulire")
    args=parser.parse_args()

    if not os.path.isabs(args.path):
        print(f"error: {args.path} deve essere assoluto", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.path):
        print(f"error: {args.path} deve esistere", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(args.path):
        print(f"error: {args.path} non è una directory", file=sys.stderr)
        sys.exit(1)

    if not args.extension.startswith("."):
        print(f"error: {args.extension} deve iniziare con il punto", file=sys.stderr)
        sys.exit(1)

    walk(args.path, args.extension)




if __name__ == "__main__":
    main()