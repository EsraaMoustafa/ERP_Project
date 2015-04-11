<html>
    <head>
    <style type="text/css">${css}</style>
    </head>
<body>
        <h1>report</h1>
        % for session in objects:
		<h2>Name: ${ session.name }</h2>
		<h2>Code: ${ session.code }</h2>
        % endfor
</body>
</html>
