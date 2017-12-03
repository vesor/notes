# ubuntu locale issue
follow the prompt,
then logout and login again!

# attach data disk
add data disk in vm's settings -> disk page on website
then mount it in linux https://chrismckee.co.uk/creating-mounting-new-drives-in-ubuntu-azure/

# install shadowsocks server
	sudo apt-get install python-setuptools
	sudo easy_install pip
	
	sudo pip install shadowsocks
	sudo ssserver -p 1733 -k password -m aes-256-cfb --user nobody -d start

run when system launch:
	sudo vi /etc/rc.local
	insert before the line "exit 0"
	sh /usr/bin/python /usr/local/bin/ssserver -p 1733 -k password -m aes-256-cfb --user nobody -d start
	sudo chmod +x /etc/rc.local
