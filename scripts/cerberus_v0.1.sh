##############################################################
### Cerberus installer 0.1                                 ###
### requires mongodb server installed                      ###
##############################################################

# Clones repo
echo downloading app data...
git clone https://github.com/galias11/cerberus.git
echo data downloaded

# Installs virtual env
echo installing virtualenv
pip3 install virtualenv
echo virtualenv succesfully installed

# Activating virtualenv...
cd cerberus
virtualenv venv -p python3
source venv/bin/activate
# virtualenv enabled

# setup app
echo running app setup
pip install -r requirements.txt
python3 -m spacy download es_core_news_md
python3 ./manage.py migrate
python3 ./scripts/nlp_setup.py
python3 manage.py createsuperuser
echo app setup successful