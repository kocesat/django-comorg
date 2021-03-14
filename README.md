# django-comorg (Communication for Organizations)

This is a template app an organization who owns a central system (api, payment systems etc.) with participants can use to communicate its participants.

Participants can manage their staff who need to access to all kind of resources with different roles and permissions in the app.

This app implements a CustomUser model extended by AbstractUser model provided by Django. UI is created by sb admin bootstrap

This app require django version 3.1.7

To start with:
Clone the project and cd into 

pip install -r requirements.txt

cd into src
python manage.py runserver

create some participants and create some users associated with those participants
