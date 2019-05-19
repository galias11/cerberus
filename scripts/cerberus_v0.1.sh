##############################################################
### Cerberus installer 0.2                                 ###
### requires mongodb server installed                      ###
##############################################################

# Clones repo
echo downloading app data...
git clone https://github.com/galias11/cerberus.git
echo data downloaded

# setup app
echo running app setup
cd cerberus
pip install -r requirements.txt --no-cache
python3 -m spacy download es_core_news_md
python3 ./manage.py collectstatic
cp ./scripts/config/web.main.config ../web.config
cp ./scripts/config/web.static.config ./static/web.config
python3 ./manage.py migrate
python3 ./scripts/nlp_setup.py
python3 manage.py createsuperuser
echo app setup successful