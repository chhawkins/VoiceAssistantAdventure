import os
from VAA_Site import wsgi

if __name__ == "__main__":
    os.system("manage.py runserver")
    os.system("python -m textblob.download_corpora lite")

app = wsgi.application