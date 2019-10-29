							README
							
-> For the setup to be made, Client has to be run on your local machine and Servers on VCL Ubuntu machines.
   Reservations for the VCL machines can be done in vcl.ncsu.edu

-> Run the Client on your local machine. List of Server Ip addresses need to be given along with file to be sent, port number of the server and MSS which is the maximum segment size.

	python3 Client.py <ip_add1> <ip_add2> port# fname MSS
	
	Eg:
	python3 Client.py 152.46.18.151 152.46.78.13 7735 abcd.txt 200
	
-> Run the Servers on the VCL machines. The initial step is to allow UDP to run on Ubuntu machines, for this run the following commands:

	sudo iptables -F
	
	For the Server to run , use the below command. Here port# is the port on which server listens to, fname is the file where you want data to be transferred and prob is the loss probability.
	
	python3 Server.py port# fname prob
	
	Eg:
	python3 Server.py 7735 recieved_file 0.05
	