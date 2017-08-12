# PowerShell

## 1) Enable-PSRemoting on windows
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-5.1

    PS C:\> Enable-PSRemoting
    PS C:\> Enable-PSRemoting -SkipNetworkProfileCheck -Force

## 2) Remote from linux
https://4sysops.com/archives/powershell-remoting-between-windows-and-linux/
### install powershell in linux. (See google)
### config windows powershell: 
    winrm set winrm/config/Service/Auth '@{Basic="true"}'
    winrm set winrm/config/Service '@{AllowUnencrypted="true")'
### access from linux powershell
    $cred = Get-Credential
    Enter-PSSession -ComputerName 10.xx.xx.xx -Credential $cred -Authentication Basic

