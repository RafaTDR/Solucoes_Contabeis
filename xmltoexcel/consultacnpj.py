import sys
import requests
from requests.structures import CaseInsensitiveDict
import json
import pandas as pd
import time
import datetime
import warnings
from datetime import date
from datetime import timedelta
import pyodbc

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
warnings.filterwarnings('ignore')


def consultacnpj(cnpj):


    principal = pd.DataFrame()
    secundario = pd.DataFrame()
    cnpjs = cnpj

    url = "https://comercial.cnpj.ws/cnpj/{}".format(cnpj)
    headers = CaseInsensitiveDict()
    headers["x_api_token"] = ""
    try:
        resp = requests.get(url, headers=headers).text
        y = json.loads(resp)
    except:
        pass

    try:
        principal2 = pd.json_normalize(y)
        #principal2["CNPJ"] = cnpj
        #principal2["Nome"] = y["razao_social"]
        #principal2["Simples"] = y["simples"]

        #principal2 = principal2[["Nome", "CNPJ", "Simples"]]
        principal = principal.append(principal2)

    except:
        pass


    # try:
    #     secundario2 = pd.json_normalize(y['estabelecimento']['atividades_secundarias'])
    #     secundario2["CNPJ"] = cnpj
    #     secundario2["Nome"] = y["razao_social"]
    #     secundario = secundario.append(secundario2)
    # except:
    #     continue

    secundarias = principal["estabelecimento.atividades_secundarias"].tolist()
    secundarias = [sub['id'] for sub in secundarias[0]]
    principais = principal["estabelecimento.atividade_principal.id"].tolist()

    try:

        principal = principal["simples.simples"].tolist()


        if principal[0] is None:
            simples = "Não"
        elif principal[0] == "Sim":
            simples = "Sim"
        else:
            simples = "Não"
    except:

        principal = principal["simples"].tolist()

        if principal[0] is None:
            simples = "Não"
        elif principal[0] == "Sim":
            simples = "Sim"
        else:
            simples = "Não"

    return simples, principais, secundarias

