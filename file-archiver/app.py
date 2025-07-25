# nome e cognome: Miriam
# matricola: Raimondi
#
# path: /home/miriam.rai/file-archiver/app.py

import argparse
import os
import sys
import time
import shutil

def walk(basepath, seconds, archive_path):
    for filename in os.listdir(basepath):
        path=os.path.join(basepath,filename)
        if os.path.isfile(path):
            file_age_seconds= time.time() - os.path.getmtime(path)
            if file_age_seconds >= seconds:
                shutil.move(path, archive_path)
                print(f"moved {path} to {archive_path}")
        elif os.path.isdir(path):
            walk(path,seconds, archive_path)

def main():
    parser=argparse.ArgumentParser(description="Archivitore di file")
    parser.add_argument("--path", type=str, required=True, help="Percorso assoluto della directory da controllare")
    parser.add_argument("--seconds", type=int, required=True, help="Età massima oltre la quale i file devono essere spostati")
    args=parser.parse_args()

    if not os.path.isabs(args.path):
        print(f"error: {args.path} deve essere un path assoluto", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.path):
        print(f"error: {args.path} deve esistere", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(args.path):
        print(f"error: {args.path} deve essere una directory", file=sys.stderr)
        sys.exit(1)

    if args.seconds <= 0:
        print(f"error: {args.seconds} deve essere un intero positivo", file=sys.stderr)
        sys.exit(1)
    
    archive_path=os.path.expanduser("~/archive")
    os.makedirs(archive_path, exist_ok=True)
    walk(args.path, args.seconds, archive_path)

if __name__ == "__main__":
    main()