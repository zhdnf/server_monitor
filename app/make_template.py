#!/usr/bin/python3

import sys,os

path = None
for i in sys.argv:
    if i == "-p" and len(sys.argv) == 3:
        path = sys.argv[sys.argv.index(i)+1]
        
if path == None:
    print("path needed")


template = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>[title]</title>
	<link rel="stylesheet" href="/static/css/bootstrap.min.css">
	<link rel="stylesheet" href="/static/css/open-iconic-bootstrap.min.css">
</head>
<body>
    % include("head")
    % include("left")
    <div class="col-sm-9 col-md-10">
    </div>
	<script type="text/javascript" src="/static/js/jquery.slim.min.js"></script>
	<script type="text/javascript" src="/static/js/popper.min.js"></script>
	<script type="text/javascript" src="/static/js/bootstrap.min.js"></script>
</body>	
</html>
'''

with open(path, "w") as f:
    f.write(template)
