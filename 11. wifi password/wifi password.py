import subprocess
import re

def get_wifi_passwords_windows():
    try:
        # Run the netsh command to get the list of all profiles
        profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
        
        # Extract the names of all profiles
        profiles = re.findall(r"Profile\s*:\s*(.*)", profiles_data)

        passwords = {}

        for profile in profiles:
            try:
                # Run the netsh command to get the details of each profile
                profile_data = subprocess.check_output(f"netsh wlan show profile name=\"{profile}\" key=clear", shell=True, text=True)
                
                # Extract the password
                match = re.search(r"Key Content\s*:\s*(.*)", profile_data)
                password = match.group(1) if match else "No password found"
                passwords[profile] = password
            except subprocess.CalledProcessError:
                passwords[profile] = "Error retrieving password"

        return passwords
    except subprocess.CalledProcessError as e:
        print("Error running command:", e)
        return None

if __name__ == "__main__":
    passwords = get_wifi_passwords_windows()
    if passwords:
        for ssid, password in passwords.items():
            print(f"SSID: {ssid} - Password: {password}")
