
# Join all .md's into a single document.


lst = [
    'koolhaas',
    'krier',
    'anonymity',
    'fiction',
    'forgetting',
    'mannerism',
    'nature',
    'reading',
    'recursion',
    'specificity',
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
    
    f = open('z_final.md', 'w')
    f.write(s)
    f.close()
        
        


def main():
    join()


if __name__ == "__main__":
    main()
        
