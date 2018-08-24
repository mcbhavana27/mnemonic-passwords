# coding: utf-8

import fire
import unidecode
import sys

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    raise Exception("Python version is %. Must be using at least Python 3.6." % sys.version_info)


def run(filename='list.txt',inputfile='wortliste.txt'):
    out=open(filename,"w")
    all = 0
    sel = 0
    with open(inputfile) as f :
        for l in f.readlines() :
            all += 1
            lo=l.lower()
            lo=unidecode.unidecode(lo.replace("ä","ae")
                                     .replace("ö","oe")
                                     .replace("ü","ue")
                                     .replace("ß","ss"))
            if len(lo)>2 and len(lo)<11:
                out.write(lo)
                sel += 1
    out.close()
    sys.stderr.write(f"read {all} from {inputfile}\nwrote {sel} to {filename}\n")


if __name__=='__main__':
    fire.Fire(run)

