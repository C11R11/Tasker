import sys
import time
import os

print ("Inicio : %s" % time.ctime())
print ("Espera de %s segundos..." % int(sys.argv[1]))
time.sleep( int(sys.argv[1]))
with open('output_test_file.fake', 'wb') as fout:
    fout.write(os.urandom(1024))
print("Creando archivo %s" % fout.name)
print("Termino : %s" % time.ctime())