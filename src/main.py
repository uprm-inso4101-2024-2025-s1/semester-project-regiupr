import paramiko

RUMAD_host = "136.145.30.28" #"rumad.upr.edu" ip address: 136.145.30.28 136.145.30.28
port = 22
regiupr_username = "estudiante" # SI NO PONES "estudiante", se supone que en el terminal te aparezca "Authentication failed."
regiupr_password = ""
break_point = 255

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(RUMAD_host, port, username=regiupr_username, password=regiupr_password)

    while break_point > 1:
        try:
            break_point-=1
            cmd_args = input("enter command: ")
            if cmd_args == "exit":
                break
            stdin, stdout, stderr = client.exec_command(cmd_args) # cmd_imput, cmd_output, cmd_line_err
            output = stdout.read()
            print(output)
        except KeyboardInterrupt:
            break
    client.close()

except Exception as error:
    print(str(error))

#probad esto con puTTY pero en vez de poner en url de rumad, poned "localhost" en el puerto "999".