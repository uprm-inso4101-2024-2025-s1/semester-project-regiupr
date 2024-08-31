from paramiko import SSHClient, AutoAddPolicy

RUMAD_host = "136.145.30.28" # "rumad.upr.edu" ip address: 136.145.30.28 
port = 22
regiupr_username = "estudiante" # SI quitas "estudiante" por otra cosa, se supone que en el terminal te aparezca "Authentication failed."
regiupr_password = ""
break_point = 255

try:
    # Creates the host client
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(RUMAD_host, port, username=regiupr_username, password=regiupr_password)

    # Updates the inputs and outputs
    while break_point > 1:
        try:
            break_point-=1
            cmd_args = input("enter command: ")
            if cmd_args == "exit":
                break
            stdin, stdout, stderr = client.exec_command(cmd_args) # cmd_input, cmd_output, cmd_line_err
            output = stdout.read().decode()
            print(output)
            
        except KeyboardInterrupt:
            break
    client.close()

except Exception as error:
    print(str(error))