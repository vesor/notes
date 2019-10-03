# For SSH
1) create a socks5 proxy using a ssh server:

	ssh -N -D 1080 weizhe@172.16.20.20

2) select one of the two methods:

a) launch chrome using socks5 proxy: 

	chrome --proxy-server="socks5://127.0.0.1:1080"

then install SwitchyOmega from google store

or b) go to github: https://github.com/FelisCatus/SwitchyOmega/releases   
download crx files and install.

3) then set SwitchyOmega proxy to 127.0.0.1:1080   

# For VMWare
To access the socks5 proxy on guest from host, set vmware network to Bridge (Not NAT).   
Find guest machine's ip address by run ipconfig in guest.   
Disable Windows Defenter Firewall on guest. (Ping guest ip from host to check.)   
Change ssh command to allow public access:
	
	ssh -N -D *:1080 weizhe@172.16.20.20

You may need to change /etc/sshd/sshd_config on the ssh server you use, set "GatewayPorts yes" in the config file.   

Now you can set proxy in host to guest_ip:1080 to access the socks proxy.   

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

	sslocal -s 00.00.000.00 -p 1733  -l 3128 -k passwd -m aes-256-cfb

run sslocal as service:
https://gist.github.com/ygmpkk/757b89cbe6f911656ddb

create a file /etc/systemd/system/sslocal.service:

	[Unit]
	Description=Daemon to start Shadowsocks Client
	Wants=network-online.target
	After=network.target

	[Service]
	Type=simple
	ExecStart=/usr/local/bin/sslocal -s 00.00.000.00 -p 1733  -l 3128 -k passwd -m aes-256-cfb   

	[Install]
	WantedBy=multi-user.target

Then enable service:

	systemctl enable sslocal
	

Then you can convert socks5 to http: 
https://github.com/shadowsocks/shadowsocks/wiki/Convert-Shadowsocks-into-an-HTTP-proxy
	
	apt-get install polipo
	service polipo stop

More configurations:
https://wiki.archlinux.org/index.php/polipo

Modify /etc/polipo/config:
	
	socksParentProxy = localhost:3128
	socksProxyType = socks5
	proxyAddress = "::0"        # both IPv4 and IPv6
	# or IPv4 only
	# proxyAddress = "0.0.0.0"
	proxyPort = 1080

# use shadowsocks proxy for git clone
  	git config --global http.proxy 'socks5://127.0.0.1:3128'
	git config --global https.proxy 'socks5://127.0.0.1:3128'
	
The config is in ~/.gitconfig

# use mirror for pip
	pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com XXXX
	
See details in https://python.freelycode.com/contribution/detail/4

# use proxy for pip
	pip install --proxy=https://user@mydomain:port somepackage
Note: it is **https://**

# use proxy for apt-get
You can place the following in /etc/apt/apt.conf
	
	Acquire::http::Proxy "http://localhost:1080/";

