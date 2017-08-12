# PowerShell

## Config windows powershell
The way to allow remote powershell doesn't look secure, but that what MS can provide for now.

### Enable-PSRemoting on windows
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-5.1

    PS C:\> Enable-PSRemoting
    PS C:\> Enable-PSRemoting -SkipNetworkProfileCheck -Force

### allow access using WinRM

    winrm set winrm/config/Service/Auth '@{Basic="true"}'
    winrm set winrm/config/Service '@{AllowUnencrypted="true")'

## Remote from linux
https://4sysops.com/archives/powershell-remoting-between-windows-and-linux/
### install powershell in linux
See powershell install instructions in github

### access from linux powershell
    $cred = Get-Credential
    Enter-PSSession -ComputerName 10.xx.xx.xx -Credential $cred -Authentication Basic


# Nvidia SMI

C:\Program Files\NVIDIA Corporation\NVSMI
