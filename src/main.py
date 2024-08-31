import paramiko
import os

host = "127.0.0.1" #"10.34.3.62" #127.0.0.0
port = 22
username = "name"
password = "string"
break_point = 5

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    while break_point > 1:
        try:
            break_point-=1
            cmd = input("$> ")
            if cmd == "exit":
                break
            stdin, stdout, stderr = client.exec_command(cmd) # cmd_imput, cmd_output, cmd_line_err
        except KeyboardInterrupt:
            break
    client.close()
except Exception as err:
    print(str(err))

#probad esto con puTTY pero en vez de poner en url de rumad, poned "localhost" en el puerto "999".