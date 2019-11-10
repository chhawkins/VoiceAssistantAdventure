import os
import VAA_Site.VAA_Site.wsgi as wsgi

if __name__ == "__main__":
    os.system("manage.py runserver")

app = wsgi.application