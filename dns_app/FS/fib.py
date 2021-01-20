from flask import Flask, request, jsonify
from socket import *

app = Flask(__name__)

@app.route('/fibonacci', methods = ['GET','POST'])
def calculateFib():
    try: 
        status_code = 200
        n = int(request.args['number'])
        if n==0:
            return 0
        y,x = 0,1
        for i in range(1,n):
            y, x = x, x+y
            Fibonacci_Number = str(x)
        response = {
            'status_code' : status_code,
            'Fibonacci Number' : Fibonacci_Number
        }
        return  jsonify(response)
    except ValueError:
        status_code = 400
        response = {
            'status_code' : status_code,
            'message' : 'Bad Request'
        }
        return jsonify(response)
@app.route('/register', methods =  ['PUT'])
def registration():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = data['as_port']

    # Create socket

    server_name = as_ip
    server_port = int(as_port)

    client_socket = socket(AF_INET, SOCK_DGRAM)
    message = 'TYPE=A \n NAME='+hostname+'\n VALUE='+ip+'\n TTL=10'
    client_socket.sendto(message.encode(), (server_name, server_port))

    # Receiver response back

    modified_message, server_address = client_socket.recvfrom(2048)

    status_code = str(modified_message.decode())
    response = {
        'status_code' : status_code,
        'message' : 'Registration was successful'
    }
    # Close the socket
    client_socket.close()
    return jsonify(response)


app.run(host='0.0.0.0',port=9090,debug=True) 