#! /usr/bin/env python

import dendropy

pdm = dendropy.PhylogeneticDistanceMatrix.from_csv(
        src=open("pythonidae.mle.weighted.pdm.csv"),
        delimiter=",")
nj_tree = pdm.nj_tree()
print(nj_tree.as_string("newick"))
