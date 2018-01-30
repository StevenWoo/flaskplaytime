Just doing this to learn flask and put up personal website

my notes on setting this up

#activate environment
#source flaskprojectenv/bin/activate
# restart after changing source
#sudo systemctl restart flaskproject.service

#after adding new dependency
#pip3 freeze > requirements.txt
# new system install new dependency
pip3 install -r requirements.txt

starting new system
pip3 install virtualenv
 virtualenv flaskprojectenv
 
 source flaskprobjectenv/bin/activate


to run from osx
export FLASK_APP=flaskproject.py
 export FLASK_DEBUG=1
flask run
# or
add environment variables to ~/.bashrc
export APP_SETTINGS="config.DevelopmentConfig"
export APP_SETTINGS="config.ProductionConfig"
need to add variables to bash/script init
for production

replace variables with real values for setup script
export DATABASE_URL="postgresql://dbusername:password@localhost/rocket"
for localhost
