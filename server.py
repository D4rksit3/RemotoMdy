
from http.server import HTTPServer, BaseHTTPRequestHandler



class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=UTF-8')
        
        output = f'''
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" lang="es" xml:lang="es">

            
            <body h1="green">
                <center><h1 >Registro de usuarios IPCC</h1></center>
                
                </br>

                <table border="2px">
                    <tr>
                        <th><strong>Direcion IP</strong></th>
                        <th><strong>Hostname</strong></th>
                        <th><strong>Horario</strong></th>
                    </tr>

                    <tr>
                    <th>{ip_equipo}  </th>
                    
                    <th>{nombre_equipo}  </th>
                    
                    <th>{now}  </th>
                    </tr>

            </table>
                
            </body>
        </html>
        
        
        '''
        self.end_headers()
        #output += '<html><body>'
        #output += '<center><h1>Registro de usuarios IPCC</h1></center>'
        
        #for task in tasklist:
        #output += f'<tr><td>{nombre_equipo}</td></tr>'
        #output += f'<table class="default"><tr><td>{ip_equipo}</td></tr></table>'
        #output += '</br>'
        #output += '</body></html>'
        self.wfile.write(output.encode())
        
       
        
def main():
    
    PORT = 8080
    server_address= ('localhost',PORT)
    server = HTTPServer(server_address, requestHandler)
    print(f'Corriendo ServerWeb en el puerto {PORT}')
    server.serve_forever()
    
if __name__ =='__main__':
    main()
    