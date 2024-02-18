API Documentation
Base URL

https://kaizntreeapp-831ad391a3c2.herokuapp.com/admin/login/?next=/admin/  
Authentication

A super user is created use  username - root password - root  This will help in administrator logging in moving forward more users and items can be created for testing the application

Endpoints

List Items

URL: /admin/dashboard/items/
Method: GET
Auth Required: Yes
Parameters:
stock_status: Filter items by stock status (e.g., in_stock, out_of_stock).
created_at_gte: Filter items created after a specific date (YYYY-MM-DD format).
Sample Call:

Create Item

URL: /admin/dashboard/items/
Method: POST
Auth Required: Yes
Data Params:

Update Item

URL: /admin/dashboard/items/<id>/
Method: PUT
Auth Required: Yes
Data Params: Same as Create Item
Sample Call:

Delete Item

URL: /admin/dashboard/items/<id>/
Method: DELETE
Auth Required: Yes
Sample Call:





Note 
I have used heroku to host my application and AWS RDS PostgreSQL to showcase multi platform adaptation.

Handling Responses
The API uses standard HTTP response codes to indicate the success or failure of requests:

200 OK: The request was successful.
201 Created: A resource was successfully created.
400 Bad Request: The request was malformed.
401 Unauthorized: Authentication credentials were missing or incorrect.
403 Forbidden: The authenticated user is not allowed to access the specified resource.
404 Not Found: The requested resource does not exist.
500 Internal Server Error: An error occurred on the server side.


If using Django Rest Framework's browsable API, the above endpoints can be easily tested via your browser. This guide provides a basic overview of the application.

2 / 2



