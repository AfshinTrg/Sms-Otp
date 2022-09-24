```
source venv/bin/activate
pip install -r requirements.txt
mv .env-sample .env
fill .env
cd smsotp/
./manage.py createsuperuser
./manage.py runserver
```
