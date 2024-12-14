import subprocess
import os
import time
import json

class VirtualAndroidSystem:
    def __init__(self, emulator_path, apk_file=None):
        self.emulator_path = emulator_path
        self.apk_file = apk_file
        self.device_id = None
        self.adb_command = "adb"  # Assuming adb is in the system's PATH
    
    def start_emulator(self):
        print("Starting Android Emulator...")
        # Launch the Android Emulator
        subprocess.Popen([self.emulator_path, "-avd", "Pixel_3a_API_30_x86_64"])
        time.sleep(60)  # Wait for the emulator to start
        
        print("Connecting to the emulator...")
        subprocess.run([self.adb_command, "start-server"])
        time.sleep(5)
        
        # Get the device ID
        device_info = subprocess.check_output([self.adb_command, "devices"])
        device_lines = device_info.decode().splitlines()
        if len(device_lines) < 2:
            print("No device found. Ensure the emulator is running correctly.")
            return False
        self.device_id = device_lines[1].split()[0]
        print(f"Device ID: {self.device_id}")
        return True

    def install_app(self):
        if not self.device_id:
            print("No emulator running.")
            return
        
        print(f"Installing APK: {self.apk_file}")
        result = subprocess.run([self.adb_command, "-s", self.device_id, "install", self.apk_file], capture_output=True)
        
        if result.returncode == 0:
            print(f"APK {self.apk_file} installed successfully.")
        else:
            print(f"Error installing APK: {result.stderr.decode()}")

    def get_system_info(self):
        if not self.device_id:
            print("No emulator running.")
            return
        
        print("Retrieving system information...")
        
        # Get OS version
        os_version = subprocess.check_output([self.adb_command, "-s", self.device_id, "shell", "getprop", "ro.build.version.release"]).decode().strip()
        
        # Get device model
        device_model = subprocess.check_output([self.adb_command, "-s", self.device_id, "shell", "getprop", "ro.product.model"]).decode().strip()
        
        # Get available memory
        available_memory = subprocess.check_output([self.adb_command, "-s", self.device_id, "shell", "cat", "/proc/meminfo"]).decode().splitlines()[0].split(":")[1].strip()
        
        system_info = {
            "OS Version": os_version,
            "Device Model": device_model,
            "Available Memory": available_memory
        }
        
        # Log the information
        print("System Info:", json.dumps(system_info, indent=4))
        return system_info

    def stop_emulator(self):
        print("Stopping Android Emulator...")
        subprocess.run([self.adb_command, "-s", self.device_id, "emu", "kill"])
        subprocess.run([self.adb_command, "kill-server"])

if __name__ == "__main__":
    emulator_path = "/path/to/your/emulator"  # Path to your Android Emulator or QEMU
    apk_file = "sample_app.apk"  # Path to the APK file you want to install

    # Initialize the Virtual Android System
    virtual_android = VirtualAndroidSystem(emulator_path, apk_file)

    # Start the emulator
    if virtual_android.start_emulator():
        # Install the sample APK
        virtual_android.install_app()
        
        # Get and display system information
        virtual_android.get_system_info()
        
        # Stop the emulator after tasks are completed
        virtual_android.stop_emulator()
