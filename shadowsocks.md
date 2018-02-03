
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

# ru ss client in local (socks5):

	sslocal -s 00.00.000.00 -p 1733  -l 1080 -k passwd

run sslocal as service:
https://gist.github.com/ygmpkk/757b89cbe6f911656ddb
	

Then you can convert socks5 to http: 
https://github.com/shadowsocks/shadowsocks/wiki/Convert-Shadowsocks-into-an-HTTP-proxy
	
	apt-get install polipo
	service polipo stop
	polipo socksParentProxy=localhost:1080
	http_proxy=http://localhost:8123 curl www.google.com
	
https://wiki.archlinux.org/index.php/polipo

# use shadowsocks proxy for pip
  	install proxychains
  	add "socks5 127.0.0.1 1080" in /etc/proxychains.conf
  	you can use proxy now: proxychains pip install XXXX

# use mirror for pip
	pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com XXXX
	
See details in https://python.freelycode.com/contribution/detail/4

# use proxy for pip
	pip install --proxy=https://user@mydomain:port somepackage
Note: it is **https://**

# use proxy for apt-get
You can place the following in /etc/apt/apt.conf
	
	Acquire::http::Proxy "http://proxy.server.port:8080";

