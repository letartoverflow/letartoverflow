import os

try:
   os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
   os.system("python manage.py runserver")
except:
   print("setUpError")
