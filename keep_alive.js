var http = require('http');

http.createServer(function (req, res) {
    res.write("╔═════════════════════════════════════╗");
    res.write("║   BreakingDown Bot Is Now Online!   ║");
    res.write("╚═════════════════════════════════════╝");
    res.end();
}).listen(8080);
