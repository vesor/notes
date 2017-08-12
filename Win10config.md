# PowerShell

## Enable-PSRemoting
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-5.1
  PS C:\> Enable-PSRemoting
  PS C:\> Enable-PSRemoting -SkipNetworkProfileCheck -Force

## Access from linux
https://4sysops.com/archives/powershell-remoting-between-windows-and-linux/
### First install powershell in linux. (See google)
### config in win10: 
  winrm set winrm/config/Service/Auth '@{Basic="true"}'
  winrm set winrm/config/Service '@{AllowUnencrypted="true")'
### remote from linux
  $cred = Get-Credential
  Enter-PSSession -ComputerName 10.xx.xx.xx -Credential $cred -Authentication Basic

