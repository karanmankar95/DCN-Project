from flask import Flask, request, jsonify
import requests
from werkzeug.exceptions import HTTPException
from socket import *
app = Flask(__name__)

@app.route('/fibonacci')
def get_params():
    try:
        hostname = request.args['hostname']
        fs_port = request.args['fs_port']
        number = request.args['number']
        as_ip = request.args['as_ip']
        as_port = request.args['as_port']
        print(hostname, fs_port, number, as_ip, as_port)

        # Create socket

        server_name = as_ip
        server_port = int(as_port)

        client_socket = socket(AF_INET, SOCK_DGRAM)
        message = 'TYPE=A \n NAME='+hostname
        client_socket.sendto(message.encode(), (server_name, server_port))

        # Receiver response back

        modified_message, server_address = client_socket.recvfrom(2048)
        if modified_message == 404:
            response = {
                'status_code' : '404',
                'Message' : 'Webpage or Server not found'
            }
            return response
        newMessage = modified_message.decode('utf-8')
        Type, Name, Value, TTL = newMessage.split('\n')
        IP = Value.strip().split('=')[-1]
        print(IP)

        URL = 'http://'+IP+':'+fs_port+'/fibonacci?number='+number

        fibo_json = requests.post(url = URL)
        print(fibo_json)
        data = fibo_json.json()
        if data['status_code'] == 200:
            Fibonacci_Number = data['Fibonacci Number']
        else:
            response = {
                'status_code' : data['status_code'],
                'Message' : data['message']
            }
            return response

        

        # Close the socket
        client_socket.close()

        status_code = 200
        response = {
            'status_code' : status_code,
            'Fibonacci Number' : Fibonacci_Number
        }
        return response
    except HTTPException:
       status_code = 400
       response = {
            'status_code' : status_code,
            'message' : "Bad request"
       }
       return response

app.run(host='0.0.0.0',port=8080,debug=True)