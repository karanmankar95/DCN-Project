from socket import *
import sys
server_port = 53533

# Create a socket (UDP)
server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind to port
server_socket.bind(('', server_port))
DataDict = {}

# Now listen
print('The server is ready to receive message...')
while True:
    # Receive message
    message, client_address = server_socket.recvfrom(2048)
    data = message.decode()

    if 'VALUE' and 'TTL' in data:
        #For Data Dictionary

        Type, Name, Value, TTL = data.split('\n')
        TypeDNS = Type.strip().split('=')[-1]
        TTLValue = TTL.strip().split('=')[-1]
        Hostname = Name.strip().split('=')[-1]
        IP = Value.strip().split('=')[-1]

        DataDict["Type"] = TypeDNS
        DataDict["Hostname"] = Hostname
        DataDict["IP"] = IP
        DataDict["TTL"] = TTLValue
    
        #for File

        file = open('Data.txt','w')
        file.write(data)
        file.close()



        modified_message = '201'
        # Send it back
        server_socket.sendto(modified_message.encode(), client_address)
        
        
        
    
    else:
        Type, Name = data.split('\n')
        Hostname = Name.strip().split('=')[-1]
        TypeDNS = Type.strip().split('=')[-1]
        file = open('Data.txt', 'r')
        FileData = file.read()
        TypeFile, NameFile, ValueFile, TTLFile = FileData.split('\n')
        '''TypeDNSFile = TypeFile.strip().split('=')[-1]
        TTLValueFile = TTLFile.strip().split('=')[-1]
        HostnameFile = NameFile.strip().split('=')[-1]
        IPFile = ValueFile.strip().split('=')[-1]'''
        if 'A' in TypeFile and Hostname in NameFile :
            modified_message = str(FileData)
            server_socket.sendto(modified_message.encode(), client_address)
        

    