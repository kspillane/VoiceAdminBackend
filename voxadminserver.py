import flask

def do_logging(url):
	#some code to handle logging goes here
	return

@app.route('/<path:path>')
# Main redirect handler

def main_spi_handler():



# Wrapper in case the script is called directly
if __name__ == '__main__':

bind_addr = "127.0.0.1"
listen_port = "5000"


    def signal_handler(signal, frame):
    #Generic SIGINT catcher   
       print "You pressed Ctrl+C"
       print "Exiting PyRedirector..."
       sys.exit()

    signal.signal(signal.SIGINT, signal_handler)
    print "You are running without a WSGI proxy. This isn't recommended for production."
    print "If you change the bind address or port you will have to manually restart tge server."
    print ""

    app.run(host=bind_addr, port=int(listen_port))
