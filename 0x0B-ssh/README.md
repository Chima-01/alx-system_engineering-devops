# SYSTEM ADMINISTRATOR - Devops

## What is a server:

A server is a computer or software system that provides services, resources, or functionality to other computers, known as clients, over a network. Servers are designed to handle specific tasks, such as serving web pages, processing emails, managing databases, or providing file storage. They often run specialized server software tailored to their intended purpose.
Where servers usually live:

Servers can be physically located in data centers, server rooms, or cloud infrastructure. They can also be virtualized and run on a shared physical server. The location of servers depends on the organization's needs and infrastructure.
What is SSH (Secure Shell):

SSH, or Secure Shell, is a network protocol used for secure communication over a potentially unsecured network, such as the internet. It provides encrypted communication between a client and a server, allowing secure authentication, remote command execution, and secure file transfer. SSH is commonly used for remote administration of servers and secure data transfer.

How to create an SSH RSA key pair:

You can create an SSH RSA key pair using the ssh-keygen command, which is available on most Unix-based systems. Here are the steps:
```
ssh-keygen -t rsa -b 2048
```
This command generates a new RSA key pair with a 2048-bit key length. It will prompt you to choose a location to save the keys and optionally set a passphrase for added security.

How to connect to a remote host using an SSH RSA key pair:

To connect to a remote host using an SSH RSA key pair, you need to have the public key added to the ~/.ssh/authorized_keys file on the remote host. Then, you can use the ssh command to connect:
```
ssh -i /path/to/private-key.pem username@remote-host
```
Replace /path/to/private-key.pem with the path to your private RSA key file, username with the remote username, and remote-host with the hostname or IP address of the remote server.
