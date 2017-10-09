import sys

def lookup(feats):
    table = {
        'm': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
        'p1': 'Person=1', 'p2': 'Person=2', 'p3': 'Person=3',
        'sg': 'Number=Sing', 'pl': 'Number=Plur',
        'perf': 'Aspect=Perf', 'impf': 'Aspect=Imp', 'hab': 'Aspect=Hab',
        'past': 'Tense=Past', 'pres': 'Tense=Pres', 'fut': 'Tense=Fut',
        'trans': 'VerbForm=Conv', 'imp': 'Mood=Imp|Person=2', 'subj': 'Mood=Sub',
        'pros': 'Aspect=Prosp', 'inf': 'VerbForm=Inf|InfForm=Dict', 'incp':
        'VerbForm=Inf|InfForm=Incp', 'pprs': 'VerbForm=Part|Aspect=Imp', 
        'sup': 'VerbForm=Supine', 'ger':
        'VerbForm=Inf|InfForm=Dict', 'loc': 'Case=Loc', 'obl': 'Case=Obl',
        # oredering is important
        'hort': 'Mood=Imp',
        'mfn': '', 'p123': '', 'sp': '', 'mf': '', 'incl': '', 'dup': 'Case=Loc', 'pred':
        'VerbForm=Part|Tense=Past|Aspect=Hab|CHECK|VerbForm=Part|Mood=Des'
        }
    
    out = []
    for feat in feats:
        try:
            out.append(table[feat])
        except:
            out.append(feat)
    
    try:
        out.remove('')
    except:
        pass
    return "|".join(out)

UPOS = 4
FEATS = 5
for line in sys.stdin:
    if line == "\n" or line[0] == "#":
        sys.stdout.write(line)
        continue

    cols = [i.rstrip("\n") for i in line.split("\t")]
    upos = cols[UPOS]
    old_feats = cols[FEATS].split("|")
    # start
    # VERB
    if upos == 'vblex':
        new_feats = []
        new_feats = lookup(old_feats)

        sys.stdout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t_\t_\n".format(*cols[0:5],
                                                                     new_feats,
                                                                     *cols[6:]))
        continue
        
    sys.stdout.write(line)


