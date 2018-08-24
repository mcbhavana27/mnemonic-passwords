import random
import fire
import math
import sys

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    raise Exception("Python version is %. Must be using at least Python 3.6." % sys.version_info)

def run(passwords=10,length=3,wordlist="list.txt",exclude="exclude.txt"):
    words=list(set((a[:len(a)-1]
              for a in open(wordlist).readlines())).difference(
              set((a[:len(a)-1]
              for a in open(exclude).readlines()))
              ))
    sys.stderr.write("Word list from {wordlist} minus {exclude} contains {} strings.\nLength {length} passwords\nis equivalent to {:2} characters ASCII 33-127\n".format(
                        len(words),
                        math.log(len(words)**length,(127-33)),
                        **locals()
                    ))
    for x in range(0,passwords) :
        print("-".join((random.choice(words) for a in range(0,length))))


if __name__ == "__main__" :
    fire.Fire(run)

