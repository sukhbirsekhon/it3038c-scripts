function getIP {
    (Get-NetIPAddress).ipv4address | Select-string "192.168*"
    }

$IP = getIP

Write-Host("This machine's IP is $IP")
Write-Host("This machine's IP is {0}" -f $IP)