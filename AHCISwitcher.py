import subprocess, pyfiglet
from getpass import getpass
import time

print(pyfiglet.figlet_format("AHCISwitcher"))
print("This software was created by sonyakun to simplify the change to AHCI mode.")
subprocess.run("bcdedit /set {current} safeboot maximum", shell=True)
yn = input("Did this work? If not, enter n, if it worked, enter y to proceed.")
if yn == "n":
    subprocess.run("bcdedit /set safebootminimal", shell=True)
with open("./safeahci.bat", "w") as f:
    f.write('bcdedit /deletevalue {current} safeboot\nSET /P ANSWER="Did this work? If not, enter n, if it worked, enter y to proceed."\nif /i {%ANSWER%}=={y} (goto :yes)\nif /i {%ANSWER%}=={yes} (goto :yes)\necho Terminates the process.\nEXIT\n\n\n:yes\nbcdedit /deletevalue safeboot')
    print(f"The bat script has been saved to {__file__}. Reboot and change the UEFI or BIOS settings, then restart Windows in Safe Mode.")
    getpass("Once the enter key is pressed, the system will restart.")
    for i in range(10):
        print(f"Remaining time to reboot:{10-i}")
        time.sleep(1)
    subprocess.run("shutdown /r /f /t 0", shell=True)