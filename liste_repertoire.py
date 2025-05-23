from os import listdir
from os.path import isfile, join

fichiers = [f for f in listdir("monRepertoire") if isfile(join("monRepertoire", f))]
