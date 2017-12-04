
# install shadowsocks server
	sudo apt-get install python-setuptools
	sudo easy_install pip
	
	sudo pip install shadowsocks
	sudo ssserver -p 1733 -k password -m aes-256-cfb --user nobody -d start

# run when system launch:
	sudo vi /etc/rc.local
	insert before the line "exit 0"
	sudo /usr/local/bin/ssserver -p 1733 -k password -m aes-256-cfb --user nobody -d start
	sudo chmod +x /etc/rc.local

# use shadowsocks proxy for pip
  install proxychains
  add "socks5 127.0.0.1 1080" in /etc/proxychains.conf
  you can use proxy now: proxychains pip install XXX
