import psutil
import time

# === Configuration ===
SCAN_INTERVAL = 5  # Delay between scans in seconds

# === State Storage ===
known_pids = set()
known_connections = set()

# === Process Monitoring ===
def check_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['pid'] not in known_pids:
            known_pids.add(proc.info['pid'])
            print(f"[🧠] New process detected: {proc.info['name']} (PID: {proc.info['pid']})")

# === Network Monitoring ===
def check_network():
    conns = psutil.net_connections(kind='inet')
    for conn in conns:
        if conn.status == "ESTABLISHED" and conn.raddr:
            remote = (conn.raddr.ip, conn.raddr.port)
            if remote not in known_connections:
                known_connections.add(remote)
                print(f"[🌐] New network connection: {remote[0]}:{remote[1]}")

# === Main Loop ===
def main():
    print("🔒 SecuMon started. Monitoring processes and network...\n")
    while True:
        check_processes()
        check_network()
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main()
