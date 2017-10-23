import sys, re
def do_stuff(table, feats):
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

def det_lookup(feats):
    table = {'m': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
             'sg': 'Number=Sg', 'pl': 'Number=Pl', 'dist': 'Distance=Dist',
             'prox': 'Distance=Prox', 'indef': 'PronType=Ind', 'excl': 'Clusivity=Excl',
             'incl': 'Clusivity=Incl', 'mfn': ''}

    out = do_stuff(table, feats)
    out = "PronType=Dem|" + out
    return out

def adj_lookup(feats):
    table = {'m': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
             'mf': 'Gender=TODO', 'mfn': 'Gender=TODO',
             'sg': 'Number=Sing', 'pl': 'Number=Plur', 'sp': 'Number=TODO',
             'nom': 'Case=Nom', 'obl': 'Case=Obl'}

    out = do_stuff(table, feats)
    if "Case" not in out:
        out += "|Case=Nom"

    return out

def gen_lookup(feats):

    table = {'m': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
             'mf': 'Gender=TODO', 'mfn': 'Gender=TODO',
             'sg': 'Number=Sing', 'pl': 'Number=Plur', 'sp': 'Number=TODO',
             'nom': 'Case=Nom', 'obl': 'Case=Obl'}

    out = do_stuff(table, feats)

    return out

def post_lookup(feats):
    table = {
        'attr': 'COLLAPSE', 'f': '', 'sg': '', 'mfn': '', 'pl': '', 'sp': '',
        'adv': '_'
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

    post = "|".join(out)
    return post

def prn_lookup(feats):
    table = {
        'm': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
        'mfn': 'Gender=TODO', 'sp': 'Number=TODO', 'mf': '',
        'p1': 'Person=1', 'p2': 'Person=2', 'p3': 'Person=3',
        'sg': 'Number=Sing', 'pl': 'Number=Plur',
        'nom': 'Case=Nom', 'obl': 'Case=Obl', 'dat': 'Case=Dat',
        'loc': 'Case=Loc', 'erg': 'Case=Erg', 'acc': 'Case=Acc',
        'inst': 'Case=Inst', 'soc': 'Case=Soc', 'instr': 'Case=Inst',
        'abl': 'Case=Abl', 'rel': 'PronType=Rel', 'corel': 'PronType=Rel',
        'interr': 'PronType=Int', 'refl': 'PronType=Prs'
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

    post = "|".join(out)
    return post


def n_lookup(feats):
    table = {
        'm': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
        'sg': 'Number=Sing', 'pl': 'Number=Plur',
        'nom': 'Case=Nom', 'obl': 'Case=Obl', 'dat': 'Case=Dat',
        'loc': 'Case=Loc', 'erg': 'Case=Erg', 'acc': 'Case=Acc',
        'inst': 'Case=Inst', 'soc': 'Case=Soc', 'instr': 'Case=Inst',
        'abl': 'Case=Abl', 'cog': '', 'top': ''
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

    post = "|".join(out)
    return post

def vb_lookup(feats):
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
        'neg': 'Polarity=Neg',
        # oredering is important
        'hort': 'Mood=Imp',
        'mfn': '', 'p123': '', 'sp': '', 'mf': '', 'incl': '', 'dup': 'Case=Loc', 'pred':
        'VerbForm=Fin|Tense=Past|Aspect=Hab|Mood=Ind|CHECK|VerbForm=Part|Mood=Des'
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

    post = "|".join(out)
    #
    # cleanup (many of these are because some things are implicit in apertium)
    # that should also probably be fixed
    # but i'm lazy
    #
    # double impf -> hab
    post = re.sub(r"Aspect=Imp\|Aspect=Imp", "Aspect=Hab", post)
    # impf and perf -> perf
    post = re.sub(r"Aspect=Imp\|Aspect=Perf", "Aspect=Perf", post)
    # imperative fix
    post = re.sub(r"Person=2\|Person=1", "Person=1", post)
    post = re.sub(r"Person=2\|Person=2", "Person=2", post)
    # add default verbform
    if not "VerbForm" in post:
        post = "VerbForm=Fin|" + post

    return post

UPOS = 4
FEATS = 5
for line in sys.stdin:
    if line == "\n" or line[0] == "#":
        sys.stdout.write(line)
        continue

    cols = [i.rstrip("\n") for i in line.split("\t")]
    upos = cols[UPOS]
    old_feats = cols[FEATS].split("|")
    gen_str = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t_\t_\n"
    # start
    # VERB
    if upos == 'vblex':
        new_feats = []
        new_feats = vb_lookup(old_feats)

        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         'VERB',
                                                                         new_feats,
                                                                         *cols[6:]))
        continue

    if upos in ['vaux', 'vbmod']:
        new_feats = []
        new_feats = vb_lookup(old_feats)

        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         'AUX',
                                                                         new_feats,
                                                                         *cols[6:]))
        continue

    hack = {'n': 'NOUN', 'np': 'PROPN'}
    if upos in ['n', 'np']:
        new_feats = []
        new_feats = n_lookup(old_feats)

        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         hack[upos],
                                                                         new_feats,
                                                                         *cols[6:]))
        continue
    
    if upos == 'prn':
        new_feats = []
        new_feats = prn_lookup(old_feats)

        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         'PRON',
                                                                         new_feats,
                                                                         *cols[6:]))
        continue

    if upos == 'det':
        new_feats = []
        new_feats = det_lookup(old_feats)

        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         'DET',
                                                                         new_feats,
                                                                         *cols[6:]))
        continue


    
    if upos == 'post':
        new_feats = []
        new_feats = post_lookup(old_feats)
        
        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         'ADP',
                                                                         new_feats,
                                                                         *cols[6:]))

        continue
    
    if upos == 'gen':
        new_feats = []
        new_feats = gen_lookup(old_feats)
        
        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         'ADP',
                                                                         new_feats,
                                                                         *cols[6:]))

        continue



    if upos == 'adj':
        new_feats = []
        new_feats = adj_lookup(old_feats)
        
        sys.stdout.write(gen_str.format(*cols[0:4],
                                                                         'ADJ',
                                                                         new_feats,
                                                                         *cols[6:]))

        continue

    # trivial ones
    if upos == 'cnjcoo':
        sys.stdout.write(gen_str.format(*cols[0:4], 'CCONJ', '_', *cols[6:]))
        continue

    if upos == 'cnjsub' or upos == 'cnjadv':
        sys.stdout.write(gen_str.format(*cols[0:4], 'SCONJ', '_', *cols[6:]))
        continue

    if upos == 'adv':
        sys.stdout.write(gen_str.format(*cols[0:4], 'ADV', '_', *cols[6:]))
        continue

    if upos in ['ij', 'inj']:
        sys.stdout.write(gen_str.format(*cols[0:4], 'INTJ', '_', *cols[6:]))
        continue

    if upos in ['sent', 'qt', 'guio', 'cm']:
        sys.stdout.write(gen_str.format(*cols[0:4], 'PUNCT', '_', *cols[6:]))
        continue

    if upos in ['part', 'clit', 'emph']:
        sys.stdout.write(gen_str.format(*cols[0:4], 'PART', '_', *cols[6:]))
        continue

    if upos == 'num':
        sys.stdout.write(gen_str.format(*cols[0:4], 'NUM', '_', *cols[6:]))
        continue

    sys.stdout.write(line)


