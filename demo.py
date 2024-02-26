import subprocess

def get_local_interfaces():
    try:
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        if result.returncode == 0:
            output_lines = result.stdout.splitlines()
            interfaces = []
            for line in output_lines:
                if "Ethernet adapter" in line or "Adaptador de Ethernet" in line:  # Windows en español
                    interface_name = line.split(":")[0].strip()
                    interfaces.append(interface_name)
            return interfaces
        else:
            print("Error al ejecutar ipconfig:", result.stderr)
            return None
    except Exception as e:
        print("Error al obtener las interfaces de red:", e)
        return None

def main():
    interfaces = get_local_interfaces()
    if interfaces:
        print("Interfaces de red disponibles:")
        for interface in interfaces:
            print(interface)
    else:
        print("No se pudo obtener la lista de interfaces de red.")

if __name__ == "__main__":
    main()
