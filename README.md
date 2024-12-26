# These instruction are for linux OS only 

A. Start Webapp Linux 🐧
```
git clone https://github.com/6abc/gemini-chat.git && cd gemini-chat && rm -rf .git
python -m venv vr_env
source vr_env/bin/activate
pip install -r requirements.txt
mv .env.example .env
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations chatbot_app
python manage.py migrate chatbot_app
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:10000
```
B. Start Webapp Windows 🪟
```
git clone https://github.com/6abc/gemini-chat.git && cd gemini-chat && rm -rf .git
python -m venv vr_env
vr_env\Scripts\activate
pip install -r requirements.txt
ren .env.example .env
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations chatbot_app
python manage.py migrate chatbot_app
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:10000
```
# GET UR API KEY : https://aistudio.google.com/apikey
2. Update Gemini API KEY
```
nano .env
```
# Access : http://127.0.0.1:1000
