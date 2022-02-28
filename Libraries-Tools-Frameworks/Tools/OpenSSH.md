# OpenSSH Server

Setting up an OpenSSH server requires a few steps:

1. Allow SSH through the firewall: `ufw allow ssh`.
1. Modify **/etc/ssh/sshd_config**.
1. Update the port, disable password authentication, (and enable the **authorized_keys** file?).
1. Public keys are pasted in this file on each line.
1. Connect to the server with `ssh $USER@$SERVER`.
1. To find the server's IP use `ifconfig` and use the **inet** IP.
1. Update the firewall to allow ssh through the new port with `ufw allow $PORT` or `iptables -A INPUT -p tcp --dport $PORT -j ACCEPT`.
