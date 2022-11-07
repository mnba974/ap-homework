from pathlib import Path
from datetime import datetime as DateTime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('chaine')
parser.add_argument('ext')
args = parser.parse_args()
chaine=args.chaine
truc=args.ext


def func(chaine,truc):
    p=Path(chaine)
    p.resolve()
    for t in p.glob('**/*.'+truc):
        t=t.resolve()
        print(t)
        time=DateTime.fromtimestamp(t.stat().st_mtime)
        print(t.stat().st_size, time)
        with open(t,'r') as f:
            print(f.readline())

func(chaine,truc)