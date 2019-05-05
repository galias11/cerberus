import json
import spacy

from .myclasses import Modelo, ModeloEconomico, ModeloDrogas

#nlp_path = "es_core_news_md"
#nlp = spacy.load(nlp_path)

def get_nlp():
    return nlp

def get_nlp_version():
    return nlp_path

def model_factory(tipo):
    """Factory de modelos"""

    tipos = ['ECON','DRUG']

    if tipo == tipos[0]:
        return ModeloEconomico()
    elif tipo == tipos[1]:
        return ModeloDrogas()