import socket

server_name = socket.gethostname()

main_file = "domains.txt"

domain_owner_file = server_name + '-domains.txt'
string_to_add = "https://"

with open(main_file, 'r' ) as f:
    file_lines = [''.join([string_to_add, x.strip(), '\n']) for x in f.readlines()]

with open(domain_owner_file, 'w') as f:
    f.writelines(file_lines) 