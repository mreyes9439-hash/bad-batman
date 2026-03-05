import socket
def scan_port(ip, poort):
try:
  # create a socket object
  s= socket.socket(.AF_INET, socket.SOCK_STREAM)
  s.settimeout(1)  # Wait 1 second for a response
  
  # Attempt to connect to the port
  result = s.connect_ex((ip, port))

if result== 0:
    print(f'Port {port}: OPEN")
    s.close()
    except Exception as e:
    print(f"Error scanning port  {port}:  {e}")

# Configuration
target_ip = "127.0.0.1" # Only scan your own machine (localhost) for practice
ports_to_scan = [21, 22, 80, 443, 3306]

print(f"Scanning target: {target_ip}...")
for port in ports_to_scan:
  scan_port(target_ip, port)
print("Scan complete.")

    
