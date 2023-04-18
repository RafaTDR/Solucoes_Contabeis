import xml.etree.ElementTree as ET
import pandas as pd
import os
import threading
from django.http import HttpResponse
from .consultacnpj import consultacnpj


def xmlnfe(pathxml,consultacnpjs):


    path = pathxml


    savefile = pathxml

    linha = 0
    linhasid = {'id': range(0, 20000)}

    numeronfe = ""
    data = ""
    cnpjemit = ""
    chNFe = ""
    vLiq = 0
    df = pd.DataFrame(linhasid)

    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        parser = ET.XMLParser(encoding='iso-8859-5')
        tree = ET.parse(fullname, parser=parser)

        doc = tree.getroot()
        nodefind = doc.find \
            ('{http://www.portalfiscal.inf.br/nfe}NFe/{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}det')

        infAdFisco = ""
        infCpl = ""
        vpisret = 0
        vcofinsret = 0
        vLiq = 0
        cnpjdest = ""
        inscricao_estadual = ""
        ufdest = ""

        for ide in doc.iter('{http://www.portalfiscal.inf.br/nfe}nNF'):

            numeronfe = ide.text

        for ide in doc.iter('{http://www.portalfiscal.inf.br/nfe}dhEmi'):

            data = ide.text

        for idDest in doc.iter('{http://www.portalfiscal.inf.br/nfe}idDest'):
            idDest = idDest.text

        for indFinal in doc.iter('{http://www.portalfiscal.inf.br/nfe}indFinal'):
            indFinal = indFinal.text

        for indPres in doc.iter('{http://www.portalfiscal.inf.br/nfe}indPres'):
            indPres = indPres.text


        for emit in doc.iter('{http://www.portalfiscal.inf.br/nfe}emit'):

            for CNPJ in emit.iter('{http://www.portalfiscal.inf.br/nfe}CNPJ'):

                cnpjemit = CNPJ.text
                if consultacnpjs == 1:
                    simples, principais, secundarias = consultacnpj(cnpjemit)
                else:
                    simples, principais, secundarias = "", "", ""

        for dest in doc.iter('{http://www.portalfiscal.inf.br/nfe}dest'):

            for CNPJ in dest.iter('{http://www.portalfiscal.inf.br/nfe}CNPJ'):
                cnpjdest = CNPJ.text

            for UF in dest.iter('{http://www.portalfiscal.inf.br/nfe}UF'):
                ufdest = UF.text

            for IE in dest.iter('{http://www.portalfiscal.inf.br/nfe}IE'):
                inscricao_estadual = IE.text

        for cobr in doc.iter('{http://www.portalfiscal.inf.br/nfe}cobr'):
            for fat in cobr.iter ('{http://www.portalfiscal.inf.br/nfe}fat'):
                for vLiq in fat.iter('{http://www.portalfiscal.inf.br/nfe}vLiq'):
                    vLiq = vLiq.text

        for infProt in doc.iter('{http://www.portalfiscal.inf.br/nfe}infProt'):

            for chNFe in infProt.iter('{http://www.portalfiscal.inf.br/nfe}chNFe'):
                chNFe = chNFe.text

        for vRetPIS in doc.iter('{http://www.portalfiscal.inf.br/nfe}vRetPIS'):
            vpisret = vRetPIS.text

        for vRetCOFINS in doc.iter('{http://www.portalfiscal.inf.br/nfe}vRetCOFINS'):
            vcofinsret = vRetCOFINS.text

        for vNF in doc.iter('{http://www.portalfiscal.inf.br/nfe}vNF'):

            vnf = vNF.text


            for det in doc.iter ('{http://www.portalfiscal.inf.br/nfe}det'):

                nprod = det.attrib

                for xProd in det.iter('{http://www.portalfiscal.inf.br/nfe}xProd'):

                    codprod = xProd.text

                    # VARIAVEIS PRODUTOS
                    # ICMS SN
                    csosn = ""
                    pcredsn = 0
                    icmssn = 0
                    orig = ""
                    # ICMS NORMAL
                    vICMSDeson = 0
                    csticms = ""
                    vbcicms = 0
                    picms = 0
                    icmsnorm = 0
                    # ICMS ST
                    vbcst = 0
                    pst = 0
                    vst = 0
                    pmvast = 0
                    # FCP ST
                    vBCFCPST = 0
                    pFCPST = 0
                    vFCPST = 0
                    # FCP
                    pfcp = 0
                    vfcp = 0
                    # ICMS EFET
                    vbcefet = 0
                    pefet = 0
                    vefet = 0

                    # ICMS RET
                    vbcicmsret = 0
                    picmsret = 0
                    vICMSSubstituto = 0
                    vICMSSTRet = 0

                    # IPI
                    cstipi = ""
                    vbcipi = 0
                    pipi = 0
                    vipi = 0

                    # PIS
                    cstpis = ""
                    vbcpis = 0
                    ppis = 0
                    vpis = 0

                    # COFINS
                    cstcofins = ""
                    vbccofins = 0
                    pcofins = 0
                    vcofins = 0

                    # ICMS DIFAL
                    vBCUFDest = 0
                    pICMSUFDest = 0
                    vICMSUFDest = 0

                    # FRETES - DESCONTOS - OUTRAS
                    vFrete = 0
                    vDesc = 0
                    vOutro = 0
                    vSeg = 0
                    eXTIPI = ""
                    cfop = ""

                    for NCM in det.iter('{http://www.portalfiscal.inf.br/nfe}NCM'):

                        ncm = NCM.text

                    for EXTIPI in det.iter('{http://www.portalfiscal.inf.br/nfe}EXTIPI'):
                        eXTIPI = EXTIPI.text

                    for cProd in det.iter('{http://www.portalfiscal.inf.br/nfe}cProd'):
                        cProd = cProd.text

                    for CFOP in det.iter('{http://www.portalfiscal.inf.br/nfe}CFOP'):

                        cfop = CFOP.text

                    for vProd in det.iter('{http://www.portalfiscal.inf.br/nfe}vProd'):
                        vProd = vProd.text

                    for vFrete in det.iter('{http://www.portalfiscal.inf.br/nfe}vFrete'):
                        vFrete = vFrete.text

                    for vDesc in det.iter('{http://www.portalfiscal.inf.br/nfe}vDesc'):
                        vDesc = vDesc.text

                    for vOutro in det.iter('{http://www.portalfiscal.inf.br/nfe}vOutro'):
                        vOutro = vOutro.text

                    for vSeg in det.iter('{http://www.portalfiscal.inf.br/nfe}vSeg'):
                        vSeg = vSeg.text

                    for ICMS in det.iter ('{http://www.portalfiscal.inf.br/nfe}ICMS'):

                        # ICMS SN
                        for CSOSN in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}CSOSN'):

                            csosn = CSOSN.text

                        for pCredSN in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}pCredSN'):

                            pcredsn = pCredSN.text

                        for vCredICMSSN in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}vCredICMSSN'):

                            icmssn = vCredICMSSN.text

                        for orig in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}orig'):

                            orig = orig.text

                        # ICMS NORMAL
                        for CST in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}CST'):

                            csticms = CST.text

                        for vBC in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vBC'):

                            vbcicms = vBC.text

                        for pICMS in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}pICMS'):

                            picms = pICMS.text

                        for vICMS in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vICMS'):

                            icmsnorm = vICMS.text

                        for vICMSDeson in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}vICMSDeson'):
                            vICMSDeson = vICMSDeson.text

                        # ICMS ST
                        for vBCST in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vBCST'):

                            vbcst = vBCST.text

                        for pICMSST in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}pICMSST'):

                            pst = pICMSST.text

                        for vICMSST in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vICMSST'):

                            vst = vICMSST.text

                        for pMVAST in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}pMVAST'):

                            pmvast = pMVAST.text

                        # FCP ST
                        for vBCFCPST in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}vBCFCPST'):
                            vBCFCPST = vBCFCPST.text

                        for pFCPST in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}pFCPST'):
                            pFCPST = pFCPST.text

                        for vFCPST in ICMS.iter('{http://www.portalfiscal.inf.br/nfe}vFCPST'):
                            vFCPST = vFCPST.text

                        # ICMS EFET
                        for vBCEfet in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vBCEfet'):

                            vbcefet = vBCEfet.text

                        for pICMSEfet in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}pICMSEfet'):

                            pefet = pICMSEfet.text

                        for vICMSEfet in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vICMSEfet'):

                            vefet = vICMSEfet.text

                        # ICMS RET
                        for vBCSTRet in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vBCSTRet'):

                            vbcicmsret = vBCSTRet.text

                        for pST in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}pST'):

                            picmsret = pST.text

                        for vICMSSubstituto in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vICMSSubstituto'):

                            vICMSSubstituto = vICMSSubstituto.text

                        for vICMSSTRet in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vICMSSTRet'):

                            vICMSSTRet = vICMSSTRet.text

                        # FCP
                        for pFCP in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}pFCP'):

                            pfcp = pFCP.text

                        for vFCP in ICMS.iter ('{http://www.portalfiscal.inf.br/nfe}vFCP'):

                            vfcp = vFCP.text

                    for IPI in det.iter ('{http://www.portalfiscal.inf.br/nfe}IPI'):

                        for CST in IPI.iter ('{http://www.portalfiscal.inf.br/nfe}CST'):

                            cstipi = CST.text

                        for vBC in IPI.iter ('{http://www.portalfiscal.inf.br/nfe}vBC'):

                            vbcipi = vBC.text

                        for pIPI in IPI.iter ('{http://www.portalfiscal.inf.br/nfe}pIPI'):

                            pipi = pIPI.text

                        for vIPI in IPI.iter ('{http://www.portalfiscal.inf.br/nfe}vIPI'):

                            vipi = vIPI.text

                    for PIS in det.iter ('{http://www.portalfiscal.inf.br/nfe}PIS'):

                        for CST in PIS.iter ('{http://www.portalfiscal.inf.br/nfe}CST'):

                            cstpis = CST.text

                        for vBC in PIS.iter ('{http://www.portalfiscal.inf.br/nfe}vBC'):

                            vbcpis = vBC.text

                        for pPIS in PIS.iter ('{http://www.portalfiscal.inf.br/nfe}pPIS'):

                            ppis = pPIS.text

                        for vPIS in PIS.iter ('{http://www.portalfiscal.inf.br/nfe}vPIS'):

                            vpis = vPIS.text

                    for COFINS in det.iter ('{http://www.portalfiscal.inf.br/nfe}COFINS'):

                        for CST in COFINS.iter ('{http://www.portalfiscal.inf.br/nfe}CST'):

                            cstcofins = CST.text

                        for vBC in COFINS.iter ('{http://www.portalfiscal.inf.br/nfe}vBC'):

                            vbccofins = vBC.text

                        for pCOFINS in COFINS.iter ('{http://www.portalfiscal.inf.br/nfe}pCOFINS'):

                            pcofins = pCOFINS.text

                        for vCOFINS in COFINS.iter ('{http://www.portalfiscal.inf.br/nfe}vCOFINS'):

                            vcofins = vCOFINS.text

                    for ICMSUFDest in det.iter ('{http://www.portalfiscal.inf.br/nfe}ICMSUFDest'):


                        for vBCUFDest in ICMSUFDest.iter ('{http://www.portalfiscal.inf.br/nfe}vBCUFDest'):

                            vBCUFDest = vBCUFDest.text

                        for pICMSUFDest in ICMSUFDest.iter ('{http://www.portalfiscal.inf.br/nfe}pICMSUFDest'):

                            pICMSUFDest = pICMSUFDest.text

                        for vICMSUFDest in ICMSUFDest.iter ('{http://www.portalfiscal.inf.br/nfe}vICMSUFDest'):

                            vICMSUFDest = vICMSUFDest.text

                    for infCpl in doc.iter ('{http://www.portalfiscal.inf.br/nfe}infCpl'):
                        infCpl = infCpl.text

                    for infAdFisco in doc.iter ('{http://www.portalfiscal.inf.br/nfe}infAdFisco'):
                        infAdFisco = infAdFisco.text



                    df.loc[df['id'] == linha , 'NF'] = (numeronfe)
                    df.loc[df['id'] == linha , 'CNPJ'] = str(cnpjemit)
                    df.loc[df['id'] == linha , 'DATA'] = (data)
                    df.loc[df['id'] == linha , 'VALOR'] = float(vnf)
                    df.loc[df['id'] == linha , 'PRODUTO'] =str(nprod) + '-' + str(codprod)
                    df.loc[df['id'] == linha, 'NCM'] = str(ncm)
                    df.loc[df['id'] == linha, 'CFOP'] = (cfop)
                    df.loc[df['id'] == linha, 'ICMS CST'] = (csticms)
                    df.loc[df['id'] == linha, 'BC ICMS'] = float(vbcicms)
                    df.loc[df['id'] == linha, 'ALIQ ICMS'] = float(picms)
                    df.loc[df['id'] == linha, 'VALOR ICMS'] = float(icmsnorm)
                    df.loc[df['id'] == linha, 'ICMS CSOSN'] = (csosn)
                    df.loc[df['id'] == linha, 'ALIQ ICMS SN'] = float(pcredsn)
                    df.loc[df['id'] == linha, 'VALOR ICMS SN'] = float(icmssn)
                    df.loc[df['id'] == linha, 'BC ICMS ST'] = float(vbcst)
                    df.loc[df['id'] == linha, 'ALIQ ICMS ST'] = float(pst)
                    df.loc[df['id'] == linha, 'VALOR ICMS ST'] = float(vst)
                    df.loc[df['id'] == linha, 'ALIQ FCP/ FCP ST'] = float(pfcp) + float(pFCPST)
                    df.loc[df['id'] == linha, 'VALOR FCP / FCP ST'] = float(vfcp) + float(vFCPST)
                    df.loc[df['id'] == linha, 'BC ICMS EFET'] = float(vbcefet)
                    df.loc[df['id'] == linha, 'ALIQ ICMS EFET'] = float(pefet)
                    df.loc[df['id'] == linha, 'VALOR ICMS EFET'] = float(vefet)
                    df.loc[df['id'] == linha, 'BC ICMS RET'] = float(vbcicmsret)
                    df.loc[df['id'] == linha, 'ALIQ ICMS RET'] = float(picmsret)
                    df.loc[df['id'] == linha, 'VALOR ICMS SUBSTITUTO'] = float(vICMSSubstituto)
                    df.loc[df['id'] == linha, 'VALOR ICMS RET'] = float(vICMSSTRet)
                    df.loc[df['id'] == linha, 'IPI CST'] = (cstipi)
                    df.loc[df['id'] == linha, 'BC IPI'] = float(vbcipi)
                    df.loc[df['id'] == linha, 'ALIQ IPI'] = float(pipi)
                    df.loc[df['id'] == linha, 'VALOR IPI'] = float(vipi)
                    df.loc[df['id'] == linha, 'VALOR PRODUTO'] = float(vProd) + float(vFrete) + float(vOutro) - float(
                        vDesc) + float(vSeg) - float(vICMSDeson)
                    df.loc[df['id'] == linha, 'BC PIS'] = float(vbcpis)
                    df.loc[df['id'] == linha, 'ALIQ PIS'] = float(ppis)
                    df.loc[df['id'] == linha, 'VALOR PIS RET'] = float(vpisret)
                    df.loc[df['id'] == linha, 'COFINS CST'] = (cstcofins)
                    df.loc[df['id'] == linha, 'BC COFINS'] = float(vbccofins)
                    df.loc[df['id'] == linha, 'ALIQ COFINS'] = float(pcofins)
                    df.loc[df['id'] == linha, 'VALOR COFINS RET'] = float(vcofinsret)
                    df.loc[df['id'] == linha, 'BC DIFAL'] = float(vBCUFDest)
                    df.loc[df['id'] == linha, 'ALIQ DIFAL'] = float(pICMSUFDest)
                    df.loc[df['id'] == linha, 'VALOR DIFAL'] = float(vICMSUFDest)
                    df.loc[df['id'] == linha, 'ORIGEM ICMS'] = (orig)
                    df.loc[df['id'] == linha, 'COD PROD'] = str(cProd)
                    df.loc[df['id'] == linha, 'CHAVE'] = str(chNFe)
                    df.loc[df['id'] == linha, 'VALOR FATURA'] = float(vLiq)
                    df.loc[df['id'] == linha, 'EX Da TIPI'] = str(eXTIPI)
                    df.loc[df['id'] == linha, 'DESTINO DA OPERACAO'] = str(idDest)
                    df.loc[df['id'] == linha, 'CONSUMIDOR FINAL'] = str(indFinal)
                    df.loc[df['id'] == linha, 'PRESENCA DO COMPRADOR'] = str(indPres)
                    df.loc[df['id'] == linha, 'INFORMACOES FISCO'] = str(infAdFisco)
                    df.loc[df['id'] == linha, 'INFORMACOES COMPLEMENTARES'] = str(infCpl)
                    df.loc[df['id'] == linha, 'CNPJ DESTINATARIO'] = str(cnpjdest)
                    df.loc[df['id'] == linha, 'INSCRICAO ESTADUAL DESTINATARIO'] = str(inscricao_estadual)
                    df.loc[df['id'] == linha, 'SIMPLES'] = str(simples)
                    df.loc[df['id'] == linha, 'ATIVIDADE PRINCIPAL'] = str(principais)
                    df.loc[df['id'] == linha, 'ATIVIDADES SECUNDARIAS'] = str(secundarias)
                    df.loc[df['id'] == linha, 'UF DESTINATARIO'] = str(ufdest)
                    df.loc[df['id'] == linha, 'VALOR MVA ST'] = float(pmvast)

                    linha = linha + 1

    df.to_excel(str(savefile) + ".xlsx", index=False)


def xmlcte(pathxml, consultacnpjs):

    path = pathxml


    savefile = pathxml

    linha = 0
    linhasid = {'id': range(0, 20000)}

    numerocte = ""
    data = ""
    cnpjemit = ""
    vcte = 0
    df = pd.DataFrame(linhasid)

    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        parser = ET.XMLParser(encoding='iso-8859-5')
        tree = ET.parse(fullname, parser=parser)

        doc = tree.getroot()
        nodefind = doc.find(
            '{http://www.portalfiscal.inf.br/nfe}NFe/{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}det')

        infCpl = ""
        chave = ""
        for ide in doc.iter('{http://www.portalfiscal.inf.br/cte}nCT'):
            numerocte = ide.text

        for ide in doc.iter('{http://www.portalfiscal.inf.br/cte}dhEmi'):
            data = ide.text

        for emit in doc.iter('{http://www.portalfiscal.inf.br/cte}emit'):

            for CNPJ in emit.iter('{http://www.portalfiscal.inf.br/cte}CNPJ'):
                cnpjemit = CNPJ.text
                if consultacnpjs == 1:
                    simples, principais, secundarias = consultacnpj(cnpjemit)
                else:
                    simples, principais, secundarias = "", "", ""


        for vRec in doc.iter('{http://www.portalfiscal.inf.br/cte}vRec'):
            vcte = vRec.text

            # VARIAVEIS PRODUTOS

            # ICMS NORMAL
            csticms = ""
            vbcicms = 0
            picms = 0
            icmsnorm = 0

            vBCOutraUF = 0
            pICMSOutraUF = 0
            vICMSOutraUF = 0

        for CFOP in doc.iter('{http://www.portalfiscal.inf.br/cte}CFOP'):
            cfop = CFOP.text

        for ICMS in doc.iter('{http://www.portalfiscal.inf.br/cte}ICMS'):

            # ICMS NORMAL
            for CST in ICMS.iter('{http://www.portalfiscal.inf.br/cte}CST'):
                csticms = CST.text

            for vBC in ICMS.iter('{http://www.portalfiscal.inf.br/cte}vBC'):
                vbcicms = vBC.text

            for pICMS in ICMS.iter('{http://www.portalfiscal.inf.br/cte}pICMS'):
                picms = pICMS.text

            for vICMS in ICMS.iter('{http://www.portalfiscal.inf.br/cte}vICMS'):
                icmsnorm = vICMS.text

            # ICMS OUTRA UF

            for vBCOutraUF in ICMS.iter('{http://www.portalfiscal.inf.br/cte}vBCOutraUF'):
                vBCOutraUF = vBCOutraUF.text

            for pICMSOutraUF in ICMS.iter('{http://www.portalfiscal.inf.br/cte}pICMSOutraUF'):
                pICMSOutraUF = pICMSOutraUF.text

            for vICMSOutraUF in ICMS.iter('{http://www.portalfiscal.inf.br/cte}vICMSOutraUF'):
                vICMSOutraUF = vICMSOutraUF.text

        busca = doc.find(
            '{http://www.portalfiscal.inf.br/cte}CTe/{http://www.portalfiscal.inf.br/cte}infCte/{http://www.portalfiscal.inf.br/cte}infCTeNorm/{http://www.portalfiscal.inf.br/cte}infDoc/{http://www.portalfiscal.inf.br/cte}infNFe/{http://www.portalfiscal.inf.br/cte}chave')
        if busca is not None:
            for infDoc in doc.iter('{http://www.portalfiscal.inf.br/cte}infDoc'):

                for chave in infDoc.iter('{http://www.portalfiscal.inf.br/cte}chave'):
                    chave = chave.text

                    df.loc[df['id'] == linha, 'CTE'] = (numerocte)
                    df.loc[df['id'] == linha, 'CNPJ'] = str(cnpjemit)
                    df.loc[df['id'] == linha, 'DATA'] = (data)
                    df.loc[df['id'] == linha, 'VALOR'] = float(vcte)
                    df.loc[df['id'] == linha, 'CFOP'] = (cfop)
                    df.loc[df['id'] == linha, 'ICMS CST'] = (csticms)
                    df.loc[df['id'] == linha, 'BC ICMS'] = float(vbcicms) + float(vBCOutraUF)
                    df.loc[df['id'] == linha, 'ALIQ ICMS'] = float(picms) + float(pICMSOutraUF)
                    df.loc[df['id'] == linha, 'VALOR ICMS'] = float(icmsnorm) + float(vICMSOutraUF)
                    df.loc[df['id'] == linha, 'CHAVE'] = str(chave)
                    df.loc[df['id'] == linha, 'SIMPLES'] = str(simples)

                    linha = linha + 1
        else:

            df.loc[df['id'] == linha, 'CTE'] = (numerocte)
            df.loc[df['id'] == linha, 'CNPJ'] = str(cnpjemit)
            df.loc[df['id'] == linha, 'DATA'] = (data)
            df.loc[df['id'] == linha, 'VALOR'] = float(vcte)
            df.loc[df['id'] == linha, 'CFOP'] = (cfop)
            df.loc[df['id'] == linha, 'ICMS CST'] = (csticms)
            df.loc[df['id'] == linha, 'BC ICMS'] = float(vbcicms) + float(vBCOutraUF)
            df.loc[df['id'] == linha, 'ALIQ ICMS'] = float(picms) + float(pICMSOutraUF)
            df.loc[df['id'] == linha, 'VALOR ICMS'] = float(icmsnorm) + float(vICMSOutraUF)
            df.loc[df['id'] == linha, 'CHAVE'] = str(chave)
            df.loc[df['id'] == linha, 'SIMPLES'] = str(simples)

            linha = linha + 1

    df.to_excel(str(savefile) + ".xlsx", index=False)


def xmlnfs(pathxml):

    path = pathxml

    savefile = pathxml

    linha = 0
    linhasid = {'id': range(0, 20000)}

    numerocte = ""
    data = ""
    cnpjemit = ""
    df = pd.DataFrame(linhasid)

    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        parser = ET.XMLParser(encoding='iso-8859-5')
        tree = ET.parse(fullname, parser=parser)

        doc = tree.getroot()
        nodefind = doc.find(
            '{http://www.portalfiscal.inf.br/nfe}NFe/{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}det')

        for NFS in doc.iter('NFS-e'):

            vserv = 0
            vtnf = 0
            vtliq = 0
            vretir = 0
            vretpis = 0
            vretcofins = 0
            vretcsll = 0
            vretinss = 0
            viss = 0
            vstiss = 0

            for Id in NFS.iter('nNFS-e'):
                numeronfs = Id.text

            for Id in NFS.iter('dEmi'):
                data = Id.text

            for prest in NFS.iter('prest'):

                for CNPJ in prest.iter('CNPJ'):
                    cnpjemit = CNPJ.text

            for total in NFS.iter('total'):

                for vtNF in total.iter('vtNF'):
                    vtnf = vtNF.text

                for vtLiq in total.iter('vtLiq'):
                    vtliq = vtLiq.text

            cLCServ = 0

            for det in NFS.iter('det'):

                for vServ in det.iter('vServ'):
                    vserv = vServ.text

                for cLCServ in det.iter('cLCServ'):
                    cLCServ = cLCServ.text

                for vRetIR in det.iter('vRetIR'):
                    vretir = vRetIR.text

                for vRetPISPASEP in det.iter('vRetPISPASEP'):
                    vretpis = vRetPISPASEP.text

                for vRetCOFINS in det.iter('vRetCOFINS'):
                    vretcofins = vRetCOFINS.text

                for vRetCSLL in det.iter('vRetCSLL'):
                    vretcsll = vRetCSLL.text

                for vRetINSS in det.iter('vRetINSS'):
                    vretinss = vRetINSS.text

                for vISS in det.iter('vISS'):
                    viss = vISS.text

                for vISSST in det.iter('vISSST'):
                    vstiss = vISSST.text

                df.loc[df['id'] == linha, 'NFS'] = (numeronfs)
                df.loc[df['id'] == linha, 'CNPJ'] = str(cnpjemit)
                df.loc[df['id'] == linha, 'DATA'] = (data)
                df.loc[df['id'] == linha, 'CODIGO SERVIÇO'] = str(cLCServ)
                df.loc[df['id'] == linha, 'VALOR SERVIÇO'] = float(vserv)
                df.loc[df['id'] == linha, 'VALOR NOTA'] = float(vtnf)
                df.loc[df['id'] == linha, 'VALOR LIQUIDO'] = float(vtliq)
                df.loc[df['id'] == linha, 'IR'] = float(vretir)
                df.loc[df['id'] == linha, 'PIS'] = float(vretpis)
                df.loc[df['id'] == linha, 'COFINS'] = float(vretcofins)
                df.loc[df['id'] == linha, 'CSLL'] = float(vretcsll)
                df.loc[df['id'] == linha, 'INSS'] = float(vretinss)
                df.loc[df['id'] == linha, 'ISS'] = float(viss)
                df.loc[df['id'] == linha, 'STISS'] = float(vstiss)

                linha = linha + 1

    df.to_excel(str(savefile) + ".xlsx", index=False)


# def processo(processo):
#     loading_process = threading.Thread(target=processo)
#     loading_process.start()
#     loading()
#     while loading_process.is_alive():
#         tkWindow.config(cursor="circle")
#         tkWindow.update()
#     else:
#         messagebox.showinfo('Processo', 'Processo concluido')
#         tkWindow.config(cursor="")
#         tkWindow.update()
#
#
# def loading():
#     messagebox.showinfo('Processando', 'Aguarde!')
#
#
# def executarnfe():
#     processo(xmlnfe)
#
#
# def executarcte():
#     processo(xmlcte)
#
#
# def executarnfs():
#     processo(xmlnfs)

