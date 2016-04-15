
# Join all .md's into a single document.


lst = [
    'anonymity',
    'fiction',
    'forgetting',
    'koolhaas',
    'krier',
    'mannerism',
    'nature',
    'reading',
    'recursion',
    'specifity',
    'taste',
    'truth',
    'typology',
    ]

unfinished = [
    'evolution',
    'formalism',
    'ideas',
    'language',
    'story',
    ]

def join():
    s = ''
    for item in lst:
        fn = item + ".md"
        sf = open(fn).read()
        s += sf
        s += '\n\n\n\n'
    
    f = open('zzz.md', 'w')
    f.write(s)
    f.close()
        
        


def main():
    join()


if __name__ == "__main__":
    main()
        
