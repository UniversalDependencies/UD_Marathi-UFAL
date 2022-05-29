# Summary

UD Marathi is a manually annotated treebank consisting primarily of stories from Wikisource, and parts of an article on Wikipedia.

# Introduction

UD Marathi is a manually annotated treebank consisting primarily of stories from Wikisource, and parts of an article on Wikipedia.

# Acknowledgements

The treebank has been manually annotated by Vinit Ravishankar. We thank Dan Zeman, Francis Tyers, Memduh Gökırmak and everyone actively helping with issues on Github for their input.

# Changelog

* 2022-11-15 v2.11
  * Fixed validation errors.
* 2021-05-15 v2.8
  * Fixed non-projective punctuation with Udapi ud.FixPunct.
  * Case=Obl was undocumented and causing validation errors.
    Changed (temporarily?) to Case=Abs.
  * Distance=Prox|Dist changed to Deixis=Prox|Remt, as in other treebanks.
  * Clusivity=Incl changed to correct Clusivity=In.
  * Instead of nsubj:own, we now annotate cop:own, as in other treebanks.
* 2018-04-15 v2.2
  * Repository renamed from UD_Marathi to UD_Marathi-UFAL.
* 2017-11-02 v2.1
  * First release in UD

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.1
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction wiki
Lemmas: manual native
UPOS: manual native
XPOS: not available
Features: manual native
Relations: manual native
Contributors: Ravishankar, Vinit
Contributing: here
Contact: vinit.ravishankar.16@um.edu.mt
===============================================================================
</pre>
