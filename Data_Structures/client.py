import socket
import sys

HOST, PORT = "192.168.0.7", 8901

print("to use:\n"
      ">linkedlist insert [data]\n"
      ">linkedlist insert [data] before [data]\n"
      ">linkedlist remove [data]\n"
      ">linkedlist show_list\n"
      "\n"
      ">stack push [data]\n"
      ">stack pop\n"
      ">stack show_data\n"
      )


def sent(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))
        received = str(sock.recv(1024), "utf-8")
    #print(f'Sent:     {data}')
    print(f'Received: {received}')


while True:
    x = input('enter request for send to server (or "exit" for exit):')
    if x == 'exit':
        break
    else:
        sent(x)
