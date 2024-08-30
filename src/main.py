import telnetlib

HOST = "127.0.0.0" #"10.34.3.62" #127.0.0.0
tn = telnetlib.Telnet(HOST, "23")

tn.write("xd\n")
print(tn.read_all())

#probad esto con puTTY pero en vez de poner en url de rumad, poned "localhost" en el puerto "999".