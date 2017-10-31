import sys, re
init = re.compile(r'^\|')
mult = re.compile(r'\|+')
finl = re.compile(r'\|$')

def cleanup(feats):
	feats =  init.sub('', feats)
	feats = mult.sub('|', feats)
	feats =  finl.sub('', feats)
	return feats

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
			 'sg': 'Number=Sing', 'pl': 'Number=Plur', 'dist': 'Distance=Dist',
			 'prox': 'Distance=Prox', 'indef': 'PronType=Ind', 'excl': 'Clusivity=Excl',
		  'incl': 'Clusivity=Incl', 'mf': '', 'mfn': '', 'p1': '', 'p2': '', 'p3': '',
		  'p123': '', 'obl': 'Case=Obl', 'nom': 'Case=Nom', 'acc': 'Case=Acc',
		  'sp': ''}

	out = do_stuff(table, feats)
	if not "PronType" in out:
		out = "PronType=Dem|" + out
	return out

def adj_lookup(feats):
	table = {'m': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
			 'mf': '', 'mfn': '',
			 'sg': 'Number=Sing', 'pl': 'Number=Plur', 'sp': '',
			 'nom': 'Case=Nom', 'obl': 'Case=Obl'}

	out = do_stuff(table, feats)
	if "Case" not in out:
		out += "|Case=Nom"

	return out

def gen_lookup(feats):

	table = {'m': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
			 'mf': '', 'mfn': '',
			 'sg': 'Number=Sing', 'pl': 'Number=Plur', 'sp': '',
			 'nom': 'Case=Nom', 'obl': 'Case=Obl'}

	out = do_stuff(table, feats)

	return out

def post_lookup(feats):
	table = {
		'attr': 'COLLAPSE', 'f': '', 'sg': '', 'mfn': '', 'pl': '', 'sp': '',
		'adv': ''
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

def prn_lookup(word, feats):
	table = {
		'm': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
		'mfn': '', 'sp': '', 'mf': '',
		'p1': 'Person=1', 'p2': 'Person=2', 'p3': 'Person=3',
		'sg': 'Number=Sing', 'pl': 'Number=Plur',
		'nom': 'Case=Nom', 'obl': 'Case=Obl', 'dat': 'Case=Dat',
		'loc': 'Case=Loc', 'erg': 'Case=Erg', 'acc': 'Case=Acc',
		'inst': 'Case=Inst', 'soc': 'Case=Soc', 'instr': 'Case=Inst',
		'abl': 'Case=Abl', 'rel': 'PronType=Rel', 'corel': 'PronType=Rel',
		'interr': 'PronType=Int', 'refl': 'PronType=Prs', 'tot':
		'PronType=Tot', 'prox': '', 'dist': '', 'incl': 'Clusivity=Incl',
		'indef': 'PronType=Ind'
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
	if word in ["तो", "ती", "ते", "त्या"]:
		post += "|Distance=Dist"
	if word in ["हा", "ही", "हे", "ह्या"]:
		post += "|Distance=Prox"

	return post


def n_lookup(feats):
	table = {
		'm': 'Gender=Masc', 'f': 'Gender=Fem', 'nt': 'Gender=Neut',
		'sg': 'Number=Sing', 'pl': 'Number=Plur',
		'nom': 'Case=Nom', 'obl': 'Case=Obl', 'dat': 'Case=Dat',
		'loc': 'Case=Loc', 'erg': 'Case=Erg', 'acc': 'Case=Acc',
		'inst': 'Case=Inst', 'soc': 'Case=Soc', 'instr': 'Case=Inst',
		'abl': 'Case=Abl', 'cog': '', 'top': '', 'ant': '', 'voc': 'Case=Voc'
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
		'neg': 'Polarity=Neg', 'caus': 'Voice=Cau',
		# oredering is important
		'hort': 'Mood=Imp',
		'mfn': '', 'p123': '', 'sp': '', 'mf': '', 'incl': '', 'dup': 'Case=Loc', 'pred':
		'VerbForm=Fin|Tense=Past|Aspect=Hab|Mood=Ind|CHECK|VerbForm=Part|Mood=Des',
		'nom': 'Case=Nom'
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
blokk = ""
tekst = ""
for line in sys.stdin:
	if line == "\n" or line[0] == "#":
		if tekst:
			sys.stdout.write("# text = {}".format(tekst.rstrip(" ")))
			sys.stdout.write("\n")
		sys.stdout.write(blokk)
		sys.stdout.write(line)
		blokk = "" ; tekst = ""
		continue

	cols = [i.rstrip("\n") for i in line.split("\t")]
	upos = cols[UPOS]
	form = cols[1]
	if form != '_':
		tekst += form + " "

	old_feats = cols[FEATS].split("|")
	gen_str = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t_\t_\n"
	# start
	# VERB
	if upos == 'vblex':
		new_feats = []
		new_feats = cleanup(vb_lookup(old_feats))

		blokk += (gen_str.format(*cols[0:3], 'VERB', '_', new_feats, *cols[6:]))
		continue

	if upos in ['vaux', 'vbmod']:
		new_feats = []
		new_feats = cleanup(vb_lookup(old_feats))
		
		blokk += (gen_str.format(*cols[0:3], 'AUX', '_', new_feats, *cols[6:]))
		continue

	hack = {'n': 'NOUN', 'np': 'PROPN'}
	if upos in ['n', 'np']:
		new_feats = []
		new_feats = cleanup(n_lookup(old_feats))
		blokk += (gen_str.format(*cols[0:3], hack[upos], '_',  new_feats, *cols[6:]))
		continue
	
	if upos == 'prn':
		new_feats = []
		new_feats = cleanup(prn_lookup(cols[2], old_feats))

		blokk += (gen_str.format(*cols[0:3], 'PRON', '_', new_feats, *cols[6:]))
		continue

	if upos == 'det':
		new_feats = []
		new_feats = cleanup(det_lookup(old_feats))

		blokk += (gen_str.format(*cols[0:3], 'DET', '_', new_feats, *cols[6:]))
		continue


	
	if upos == 'post':
		new_feats = []
		new_feats = cleanup(post_lookup(old_feats))
		
		blokk += (gen_str.format(*cols[0:3], 'ADP', '_', new_feats, *cols[6:]))

		continue
	
	if upos == 'gen':
		new_feats = []
		new_feats = cleanup(gen_lookup(old_feats))
		
		blokk += (gen_str.format(*cols[0:3], 'ADP', '_', new_feats, *cols[6:]))

		continue



	if upos == 'adj':
		new_feats = []
		new_feats = cleanup(adj_lookup(old_feats))
		
		blokk += (gen_str.format(*cols[0:3], 'ADJ', '_', new_feats, *cols[6:]))

		continue

	# trivial ones
	if upos == 'cnjcoo':
		blokk += (gen_str.format(*cols[0:3], 'CCONJ', '_', '_', *cols[6:]))
		continue

	if upos == 'cnjsub' or upos == 'cnjadv':
		blokk += (gen_str.format(*cols[0:3], 'SCONJ', '_', '_', *cols[6:]))
		continue

	if upos == 'adv':
		blokk += (gen_str.format(*cols[0:3], 'ADV', '_', '_', *cols[6:]))
		continue

	if upos in ['ij', 'inj']:
		blokk += (gen_str.format(*cols[0:3], 'INTJ', '_', '_', *cols[6:]))
		continue

	if upos in ['sent', 'qt', 'guio', 'cm']:
		blokk += (gen_str.format(*cols[0:3], 'PUNCT', '_', '_', *cols[6:]))
		continue

	if upos in ['part', 'clit', 'emph']:
		blokk += (gen_str.format(*cols[0:3], 'PART', '_', '_', *cols[6:]))
		continue

	if upos == 'num':
		blokk += (gen_str.format(*cols[0:3], 'NUM', '_', '_', *cols[6:]))
		continue

	blokk += (line)


