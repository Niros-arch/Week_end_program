# Linux Networking 
## Get your IP

- Use this command to see your IP address. `ifconfig` on its own will list all interfaces, or you can specify one.
```
ifconfig 
```
- or you can specify the interfaces  like *eth0, lo, tun0, wlan0 *
```
ifconfig [interface]
```

##  Curl

Curl POST Request:
```
curl -X POST [options] [URL]
```
- **`[options]`**: These are optional flags that customize the request. Common ones include:
    
    - `-d 'data'` or `--data 'data'`: Sends data in the request body (e.g., form data or JSON).
        
    - `-H 'Header: Value'` or `--header 'Header: Value'`: Adds custom HTTP headers (e.g., `Content-Type: application/json`).
        
    - `-F 'field=@file'` or `--form 'field=@file'`: Uploads files as multipart/form-data (ideal for file uploads).
        
    - `--json '{...}'`: Sends JSON data with the correct `Content-Type: application/json` header (available in curl 7.82.0+).
        
    - `-u 'username:password'`: Includes basic authentication credentials.
        
    - `-k` or `--insecure`: Skips SSL certificate verification (use with caution). 
        
- **`[URL]`**: The target endpoint where the POST request is sent.
## SSH

 - **SSH in Kali Linux** is a secure method for remote access, enabling encrypted communication between a client and server over an insecure network.
 ### Generating a Keypair
  - Generate a public and private key with the following command. By default it will save to the `~/.ssh` directory.
  ```
  $ ssh-keygen
  ```
  ![[Pasted image 20260320135222.png]]
## Testing a Connection

- How to test if you can force a box to communicate back to you?
### NetCat

 - A `netcat` listener is useful for many reasons, including catching shells. But it can also be good for testing a one-off connection, such as a HTTP request.

- This is the basic syntax for a netcat listener:
```
$ nc -lp [PORT]
```
- This will catch incoming connections, and also harvest user agents from the requestor.
- To start on a priveleged port, such as 80 or 443, you must run with root priveleges:
```
$ sudo nc -lnvp 80
```
- For extra info, use the `-v` flag to put it in verbose mode. Use the `-n` flag to not perform DNS lookups on the incoming connections. This is the standard netcat command I use:
```
$ nc -lnvp [PORT]
```
- Netcat can listen for anything sent over TCP or UDP (practically any web traffic besides `ping` requests).
- Netcat closes after one connection by default. To have your netcat listener stay open after a connection, use the `-k` flag.
### Python web-server

- A Python webserver is better than Netcat if you want to make multiple requests, as it stays open after a connection by default. However, a Python webserver does not harvest as much information by default, such as User Agent strings
- On host machine, start a webserver:
```
$ python3 -m http.server [PORT]
```
- (_Note:_ This listens on port 8000 by default.)

Then make a connection to your box, using any method available to you:

- Curl: `$ curl http://[IP]:[PORT]`
- Wget: `$ wget http://[IP]:[PORT]`
- Netcat: `$ nc [IP]:[PORT]`
- Curl.exe (Windows 10): `curl.exe --url http://[IP]:[PORT]`
- Powershell: `powershell -command "Invoke-WebRequest -Uri http://[IP]:[PORT]"`
### ping 

- The **ping** command in Kali Linux is used to test network connectivity by sending ICMP echo requests to a target host and waiting for a reply.
- On the target machine, ping your box once using either:
- `ping -c 1 [IP]` (Linux)
- `ping -n 1 [IP]` (Windows)
- Pinging only once is necessary if you have non-interactive remote code execution (i.e. you can issue a command, but not press `Ctrl + C` to abort it). Otherwise, the box will continue pinging forever.
## PHP Webservers

Similarly to the Python Webserver, this starts a server locally and quickly, and gives you output logs. However, it is more useful for serving PHP files than it is for transferring files between boxes.
If you want to test a PHP script locally, you can run a PHP webserver in the serving directory like so:
```
$ php -S localhost:[PORT]
```
- Like with Python, you will need root privileges to run on a priveleged port (<1000)
## Tunneling

Use tunneling to access a remote port via a local port.
For example, a webserver is running locally on a remote box (it is not exposed publicly to the internet). If this server was running on port 9999, it would be accessed on the remote box via `http://localhost:9999`.
If we have a way of tunneling to this box, we can set up a relay from our computer to the remote computer. For example, we could tell our port 8000 to point to the remote server's port 9999. If the remote server's IP was `192.0.0.2`, the tunnel would look like this:
- We make a request to `http://localhost:8000` on our local machine
- This request is forwarded, via a tunnel, to `http://192.0.0.2:9999`
This setup allows us, for example, to access a website in the browser that we may only have been able to interact with previously over command line.
### With SSH
If we have SSH access to this machine, we can use SSH tunneling to accomplish this goal:
```
$ ssh -L 8000:localhost:9999 [USER@]192.0.0.2 [-i /path/to/private/key]
```
This assumes the same addresses as above. It will ask us to log in, or use an optional provided private key. Once the SSH connection completes, an SSH terminal will open, and the tunnel will be setup.
You can then 'navigate' to the remote host's 'local' webserver by visiting your own localhost:

```
$ curl localhost:8000
```