import sys
import time

print ("Inicio : %s" % time.ctime())
print ("Espera de %s segundos..." % int(sys.argv[1]))
time.sleep( int(sys.argv[1]))
print("Termino : %s" % time.ctime())