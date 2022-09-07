
### Differentiate between GET and POST.
Both GET and POST method is used to transfer data from client to server in HTTP protocol but
Main difference between POST and GET method is that GET carries request parameter appended
in URL string while POST carries request parameter in message body which makes it more secure
way of transferring data from client to server.

|                                       |                                  | 
| ------------------------------------- | -------------------------------- | 
| GET                                   | POST                             | 
| Not secure due to exposed in URL bar  | Secure: data is sent in body.    | 
| Idempotent: No side effect            | Non-idempotent                   | 
| Limited amount of data only in header | Large amount of data in the body | 
| More efficient => More common         | Less efficient => Less common    | 

PUT implies putting a resource - completely replacing whatever is available at the given URL with a different thing. By definition, a PUT is idempotent. Do it as many times as you like, and the result is the same. x=5 is idempotent. You can PUT a resource whether it previously exists, or not (eg, to Create, or to Update)!

POST updates a resource, adds a subsidiary resource, or causes a change. A POST is not idempotent, in the way that x++ is not idempotent.

The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
The HEAD method asks for a response identical to a GET request, but without the response body.
The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
The PUT method replaces all current representations of the target resource with the request payload.
The DELETE method deletes the specified resource.
The PATCH method applies partial modifications to a resource.


cURL, which stands for client URL, is a command line tool to send API requests.