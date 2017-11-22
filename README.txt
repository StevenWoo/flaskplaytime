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
