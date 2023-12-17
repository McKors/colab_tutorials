import itertools
import pandas as df

polymers = ["*CC*", "*CCO*"]
enzymes = ["PETase", "LCC", "TfH","ThC_Cut1","ThC_Cut2","HiC","FsC","PET2","PET5","Cut190"]

# https://docs.python.org/3/library/itertools.html

pr = itertools.product(polymers, enzymes)
times = range(0, 1000, 24)
my_list = []

for pol, enz in pr:
    for time in times:
        xc = random.randint(50,70)
        my_list.append({"time": time, "pol": pol, "enz": enz, "xc": xc})
df.DataFrame(my_list)
