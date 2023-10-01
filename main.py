from website import create_app

webApp = create_app()
if __name__ == '__main__':
    webApp.run(host='0.0.0.0', port=8443, debug=True)
