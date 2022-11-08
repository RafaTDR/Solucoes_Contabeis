from waitress import serve

from crm.wsgi import application

if __name__ == '__main__':
    serve(application, host ='srvperini', port='4433')
