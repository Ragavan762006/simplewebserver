from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<title>Top revenue generating companies</title>
<body>
      <table border="1" cellspacing=1" cellpadding="20">
<caption> <h2>Top revenue generating companies</h2></caption>
<tr>
     <th>S.No</th>
     <th>Company</th>
     <th>revenue</th>
  </tr>
<tr>
     <th>1</th>
     <td>Microsoft</td>
     <td>65 billion</td>
 </tr>
   <tr>
<th>2</th>
<td>Oracle</td>
<td>60 billion</td>

</tr>
<tr>
<th>3</th>
<td>IBM</td>
<td>10.5 billion</td>
</tr>
<tr>
<th>4</th>
<td>SAP</td>
<td>6.5 billion</td>
</tr>
<tr>
<th>5</th>
<td>symantec</td>
<td>5.3 billion</td>

</tr>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()