import os, glob
import pandas as pd
import csv
import sqlite3
from django.conf import settings

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

def ret_recbto_febraban240(empresa, pathtxt):


    cod_empresa = str(empresa).replace("[", "").replace("(", "").replace("]", "").replace(")", "").split(',')[0]

    con = sqlite3.connect(str(settings.DATABASES['default']['NAME']))
    contas = pd.read_sql_query(f'SELECT * FROM empresa WHERE code = {cod_empresa} AND ativo = 1', con)
    contas = contas[["cod_banco", "conta"]]
    contas = contas.rename({"cod_banco":"portador - t"}, axis=1)



    data = pd.DataFrame()

    for filename in os.listdir(pathtxt):
        if not filename.endswith('.txt'): continue
        with open(os.path.join(pathtxt, filename), 'r') as f:

           data1 = pd.read_csv(f, header=None)
           data = pd.concat([data,data1])


    data["movimento"] = data[0].str.slice(15,17)
    data["segmento"] = data[0].str.slice(13,14)
    data["portador - t"] = data[0].str.slice(0,3) + data[0].str.slice(23,35)
    data["Cnpj - t"] = data[0].str.slice(134,148)
    data["Data - u"] = data[0].str.slice(145,153)
    data["Nome - t"] = data[0].str.slice(148,187)
    data["Nota - t"] = data[0].str.slice(58,72)
    data["valor - u"] = data[0].str.slice(92,107)
    data["juros - u"] = data[0].str.slice(17, 31)
    data["desconto - u"] = data[0].str.slice(32,46)
    datat = data[data.segmento == "T"]
    datat = datat[["movimento", "portador - t", "Cnpj - t", "Nome - t", "Nota - t"]]
    datat = datat.reset_index()
    datat = datat.drop(["index"], axis=1)


    datau = data[data.segmento == "U"]
    datau = datau[["Data - u", "valor - u", "juros - u", "desconto - u"]]
    datau = datau.reset_index()
    datau = datau.drop(["index"], axis=1)


    dataf = datat.join(datau)
    dataf = dataf[dataf.movimento == "06"]

    dataf = dataf.merge(contas, how='left', left_on='portador - t', right_on='portador - t')

    # dataf.to_csv("TESTE.csv")

    contabil = pd.DataFrame(columns=["CNPJ", "DATA", "CTA DEB", "CTA CRE", "VALOR", "HISTORICO", "NOTA", "CTA JUROS",
                                     "VLR JUROS", "HIST JUROS", "CTA DEB DESCONTOS", "CTA CRE DESCONTOS", "VLR DESCONTOS",
                                     "HIST DESCONTOS"])
    contabil["CNPJ"] = dataf["Cnpj - t"]
    contabil["DATA"] = dataf["Data - u"].str.strip().str[0:2] + "/" + dataf["Data - u"].str.strip().str[2:4] + "/" \
                       + dataf["Data - u"].str.strip().str[4:8]
    contabil["CTA DEB"] = dataf["conta"]
    contabil["CTA CRE"] = ""
    contabil["VALOR"] = dataf["valor - u"].str.strip().str[:-2] + "." + dataf["valor - u"].str.strip().str[-2:]
    contabil["VALOR"] = contabil["VALOR"].map(float).round(2)
    contabil["VALOR"] = contabil["VALOR"].map(str)
    contabil["VALOR"] = contabil["VALOR"].str.replace(".", ",", regex = False)
    nf = dataf["Nota - t"].str.split(r"/|-", expand=True)
    nf = nf[0]
    contabil["HISTORICO"] = "VLR REF DUPL " + nf.map(int).map(str) + " " + dataf["Nome - t"]
    contabil["NOTA"] = nf.map(int).map(str)
    contabil["CTA JUROS"] = "746"
    contabil["VLR JUROS"] = dataf["juros - u"].str.strip().str[:-2] + "." + dataf["juros - u"].str.strip().str[-2:]
    contabil["VLR JUROS"] = contabil["VLR JUROS"].map(float).round(2)
    contabil["VLR JUROS"] = contabil["VLR JUROS"].map(str)
    contabil["VLR JUROS"] = contabil["VLR JUROS"].str.replace(".", ",", regex = False)
    contabil.loc[contabil["VLR JUROS"] != "0,0", "HIST JUROS"] = "VLR REF JUROS S/ DUPL " + nf.map(int).map(str) + " "\
                                                                 + dataf["Nome - t"]
    contabil.loc[contabil["VLR JUROS"] == "0,0", "HIST JUROS"] = ""
    contabil["CTA DEB DESCONTOS"] = "1652"
    contabil["CTA CRE DESCONTOS"] = "745"
    contabil["VLR DESCONTOS"] = dataf["desconto - u"].str.strip().str[:-2] + "." + dataf["desconto - u"].str.strip().str[-2:]
    contabil["VLR DESCONTOS"] = contabil["VLR DESCONTOS"].map(float).round(2)
    contabil["VLR DESCONTOS"] = contabil["VLR DESCONTOS"].map(str)
    contabil["VLR DESCONTOS"] = contabil["VLR DESCONTOS"].str.replace(".", ",", regex = False)
    contabil.loc[contabil["VLR DESCONTOS"] != "0,0", "HIST DESCONTOS"] = "VLR REF DESCONTOS S/ DUPL " +\
                                                                         nf.map(int).map(str) + " " + dataf["Nome - t"]
    contabil.loc[contabil["VLR DESCONTOS"] == "0,0", "HIST DESCONTOS"] = ""

    contabil["FINAL"] = contabil["CNPJ"].map(str) + ";" + contabil["DATA"].map(str) + ";" + contabil["CTA DEB"].map(str) + ";" \
               + contabil["CTA CRE"].map(str) + ";" + contabil["VALOR"].map(str) + ";" +\
               contabil["HISTORICO"].map(str) + ";" + contabil["NOTA"].map(str) + ";" + contabil["CTA JUROS"].map(str) \
               + ";" + contabil["VLR JUROS"].map(str) + ";" + contabil["HIST JUROS"].map(str) + ";" + \
               contabil["CTA DEB DESCONTOS"].map(str) + ";" + contabil["CTA CRE DESCONTOS"].map(str) + ";" +\
               contabil["VLR DESCONTOS"].map(str) + ";" + contabil["HIST DESCONTOS"].map(str)
    contabil.reset_index(drop=True, inplace=True)
    contabil["FINAL"].to_csv(str(pathtxt) + ".txt", index=False, quoting=csv.QUOTE_NONE, sep='\t')