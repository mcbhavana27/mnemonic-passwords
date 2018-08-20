import random
import fire
import math
import sys

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

