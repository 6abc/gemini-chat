 

1. Copy and activate virtual env
```
git clone https://github.com/6abc/gemini-chat.git && cd gemini-chat && rm -rf .git
python -m venv vr_env
source vr_env/bin/activate
pip install -r requirements.txt
```
# GET UR API KEY : https://aistudio.google.com/apikey
2. Update Gemini API KEY
```
mv .env.example .env
nano .env
```
3. Start Webapp
```
python manage.py collectstatic
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations chatbot_app
python manage.py migrate chatbot_app
python manage.py runserver 0.0.0.0:10000
```
