function getIP {
    (Get-NetIPAddress).ipv4address | Select-string "192.168*"
    }

$IP = getIP
$USER = $env:USERNAME
$HOSTNAME = $env:COMPUTERNAME
$PVERSION = (get-host).Version 
$DAYOFWEEK = (get-date).DayOfWeek
$MONTH= (get-date).Month
$DAY= (get-date).Day
$YEAR= (get-date).Year


$BODY = "This machine's IP is $IP. User is $USER. Hostname is  $HOSTNAME. Powershell version is $PVERSION. Today's Date is $DAYOFWEEK, $MONTH/$DAY/$YEAR"

Send-MailMessage -To "sekhonss@mail.uc.edu" -From "sukhbirsekhon3939@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 