# 1) Remote access using PowerShell

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


# 2) Make Powershell more powerful
## allow to run script 
    Set-ExecutionPolicy RemoteSigned
## create profile (something like .bashrc)
    New-Item $profile -Type File -Force
It creates a file called Microsoft.PowerShell_profile.ps1 in a folder called WindowsPowerShell under your Documents folder.

## install vim for windows
Then use vim in powershell.
    set-alias vim "C:/Program Files/Vim/Vim74/./vim.exe"
    
# Powershell commands
    $PSVersionTable
    $Profile

# Misc
Nvidia SMI locate in 
    C:\Program Files\NVIDIA Corporation\NVSMI
