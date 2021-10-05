var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

/**
 * Total memory in MB
 */
var totalMem = os.totalmem();
var totalMBMem = totalMem / 1024;

/**
* Free memory in MB
*/
var freeMem = os.freemem();
var freeMBMem = freeMem / 1024;


// Convert given OS seconds to days of 24 hours 
function covertSecondsToDays(sec) {
  var days = Math.floor(sec / (3600 * 24));
  return ("Days: " + days + ", ")
}

// Convert given OS seconds to hours of 3600 seconds
function covertSecondsToHours(sec) {
  var hours = Math.floor(sec / 3600);
  return ("Hours: " + hours + ", ")
}

// Convert given OS seconds to minutes 
function covertSecondsToMinutes(sec) {
  // First convert seconds to hours
  var hours = Math.floor(sec / 3600);
  // Figure out the left over seconds
  sec = sec - hours * 3600;
  // Convert left-over seconds to munutes of 60 seconds
  var minutes = Math.floor(sec / 60);
  return ("Minutes: " + minutes + ", ")
}

// Convert given OS seconds to seconds
function covertSecondsToSeconds(sec) {
  // First convert seconds to minutes
  var minutes = Math.floor(sec / 60);
  //Figure out left-over seconds and that's your seconds
  sec = sec - minutes * 60;

  return ("Seconds: " + sec)
}

// Combine all conversions together
function getProcessUptime(sec) {
  return (covertSecondsToDays(sec) + covertSecondsToHours(sec) + covertSecondsToMinutes(sec) + covertSecondsToSeconds(sec))
}

http.createServer(function (req, res) {

  if (req.url === "/") {
    fs.readFile("./public/index.html", "UTF-8", function (err, body) {
      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(body);
    });
  }
  else if (req.url.match("/sysinfo")) {
    myHostName = os.hostname();
    html = `    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${getProcessUptime(os.uptime())}</p>
            <p>Total Memory: ${totalMBMem} MB</p>
            <p>Free Memory: ${freeMBMem} MB </p>
            <p>Number of CPUs: ${(os.cpus()).length}</p>            
          </body>
        </html>`
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(html);
  }
  else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");