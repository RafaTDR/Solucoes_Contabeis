import smtplib
import datetime
import time
import pandas as pd
from email.message import EmailMessage
import sqlite3
from dateutil.relativedelta import relativedelta

conexao = sqlite3.connect('db.sqlite3')
c = conexao.cursor()
c.execute("SELECT cliente, email, assunto, mensagem, dia, setor FROM Customer WHERE active = True AND ativo = True")
base_email = c.fetchall()

conexao.commit()
conexao.close()


pd.set_option('display.max_colwidth', None)
base_email = pd.DataFrame(base_email,columns=['cliente','email','assunto','mensagem','dia', 'setor'])
base_email["mensagem"] = base_email["mensagem"].astype('string')


for cliente in base_email["cliente"]:

    if pd.isna(cliente):
        pass
    else:

        destinatario = base_email.loc[base_email['cliente'] == cliente, "email"]
        assunto = base_email.loc[base_email['cliente'] == cliente, "assunto"]
        mensagem = base_email.loc[base_email['cliente'] == cliente, "mensagem"]
        dia = base_email.loc[base_email['cliente'] == cliente, "dia"].fillna(0.0).astype(int)
        hora ="1" #base_email.loc[base_email['cliente'] == cliente, "HORA"].fillna(0.0).astype(int)
        setor = base_email.loc[base_email['cliente'] == cliente, "setor"]

        destinatario= str(destinatario).split()[1]
        assunto = str(assunto)[5:].replace("Name: assunto, dtype: object", "").splitlines()
        mensagem = str(mensagem)[5:].replace("Name: mensagem, dtype: string", "").splitlines()
        dia = str(dia).split()[1]
        competencia = datetime.datetime.today()-relativedelta(months=1)
        dia = datetime.datetime.strptime(dia,"%d").date().strftime("%d")
        now = datetime.datetime.now()
        setor = int(str(setor).split()[1])


        if setor == 2:
            gmail_user = 'email@email'
            gmail_password = '****'
        elif setor == 1:
            gmail_user = 'email1@email1'
            gmail_password = '******'
        else:
            print("Setor não cadastrado")

        smtp_server = smtplib.SMTP_SSL('email-ssl.com.br', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)


        if now.strftime("%d") == dia:
            if now.strftime("%H") ==now.strftime("%H"):
                x = 0
                for x in range(51):
                    try:
                        mensagem[x]
                    except IndexError:
                        mensagem.append("")

                msg = EmailMessage()
                msg['From']= gmail_user
                msg['To'] = '{}'.format(destinatario)
                msg['Bcc'] = gmail_user
                msg['Subject'] = '{}'.format(assunto[0]) + ' {}'.format(competencia.strftime('%m/%Y'))
                msg['Disposition-Notification-To'] = gmail_user
                #body = '{}'.format(mensagem)
                msg.set_content(f'''
                <!DOCTYPE html>
                <html>
                    <body>
                        <div>
                            <p>{mensagem[0]}</p>
                            <p>{mensagem[1]}</p>
                            <p>{mensagem[2]}</p>
                            <p>{mensagem[3]}</p>
                            <p>{mensagem[4]}</p>
                            <p>{mensagem[5]}</p>
                            <p>{mensagem[6]}</p>
                            <p>{mensagem[7]}</p>
                            <p>{mensagem[8]}</p>
                            <p>{mensagem[9]}</p>
                            <p>{mensagem[10]}</p>
                            <p>{mensagem[11]}</p>
                            <p>{mensagem[12]}</p>
                            <p>{mensagem[13]}</p>
                            <p>{mensagem[14]}</p>
                            <p>{mensagem[15]}</p>
                            <p>{mensagem[16]}</p>
                            <p>{mensagem[17]}</p>
                            <p>{mensagem[18]}</p>
                            <p>{mensagem[19]}</p>
                            <p>{mensagem[20]}</p>
                            <p>{mensagem[21]}</p>
                            <p>{mensagem[22]}</p>
                            <p>{mensagem[23]}</p>
                            <p>{mensagem[24]}</p>
                            <p>{mensagem[25]}</p>
                            <p>{mensagem[26]}</p>
                            <p>{mensagem[27]}</p>
                            <p>{mensagem[28]}</p>
                            <p>{mensagem[29]}</p>
                            <p>{mensagem[30]}</p>
                            <p>{mensagem[31]}</p>
                            <p>{mensagem[32]}</p>
                            <p>{mensagem[33]}</p>
                            <p>{mensagem[34]}</p>
                            <p>{mensagem[35]}</p>
                            <p>{mensagem[36]}</p>
                            <p>{mensagem[37]}</p>
                            <p>{mensagem[38]}</p>
                            <p>{mensagem[39]}</p>
                            <p>{mensagem[40]}</p>
                            <p>{mensagem[41]}</p>
                            <p>{mensagem[42]}</p>
                            <p>{mensagem[43]}</p>
                            <p>{mensagem[44]}</p>
                            <p>{mensagem[45]}</p>
                            <p>{mensagem[46]}</p>
                            <p>{mensagem[47]}</p>
                            <p>{mensagem[48]}</p>
                            <p>{mensagem[49]}</p>
                            <p>{mensagem[50]}</p>
                        </div>
                        <div style="padding:20px 0px">
                            <div style="height: 300px;width:500px">
                                <img src=""">
                                <img src=""">
                            </div>
                        </div>
                    </body>
                </html>
                ''', subtype='html')


                #email_text = ("""From: %s\r\nTo: %s\r\nSubject: %s\r\n\n  %s""" % (sent_from, to, subject, body.encode('utf-8')))

                try:
                    #smtp_server.sendmail(sent_from, to, email_text)
                    smtp_server.send_message(msg)
                    print(cliente)
                    print("Email enviado com sucesso!")
                    print(now)
                except Exception as ex:
                    print(cliente)
                    print("Algo deu errado, verificar….",ex)
                    print(now)

                time.sleep(5)

        smtp_server.close()

