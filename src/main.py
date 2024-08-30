import telnetlib

HOST = "localhost"
tn = telnetlib.Telnet(HOST, "999")

tn.write("xd\n")
print(tn.read_all())

#probad esto con puTTY pero en vez de poner en url de rumad, poned "localhost" en el puerto "999".