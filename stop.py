import os

try:
   os.system("pg_ctl -D $PREFIX/var/lib/postgresql stop")
except:
   print("setUpError")
