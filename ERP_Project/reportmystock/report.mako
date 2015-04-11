<html>
    <head>
    <style type="text/css">${css}</style>
    </head>
<body>
        <h1>report</h1>
        % for session in objects:
		<h2>address: ${ session.address }</h2>
		<h2>keeper: ${ session.keeper_id }</h2>
		<h2>products: ${ session.product_id }</h2>
        % endfor
</body>
</html>
