import sys

for line in sys.stdin:
	if line == '\n' or line[0] == '#':
		sys.stdout.write(line)
		continue

	full = line
	line = line.split('\t')
	morph = line[5]
	out = []
	try:
		morph = {a.split("=")[0]: a.split("=")[1] for a in morph.split('|')}
		for key in sorted(morph):
			out.append("{}={}".format(key, morph[key]))

		morph = "|".join(out)
		

	except:
		morph = '_'

	try:
		sys.stdout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*line[:5],
																  morph, *line[6:]))

	except:
		sys.stdout.write(full)
