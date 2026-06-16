## REST API

`REST (Representational State Transfer) is an approach used to build web services that interact using standard HTTP methods such as GET, POST, PUT and DELETE. APIs built using REST follow predictable rules, making them suitable for data exchange between applications. `

###
At its core, a REST API acts as a bridge between different software applications, allowing them to communicate over the internet using the principles of Representational State Transfer (REST).

### REST API in Python
REST (Representational State Transfer) is an architectural style for designing applications. REST is not a protocol but it is a set of principles that define how web standards, such as HTTP and URLs, should be used for building scalable and loosely coupled systems. RESTful APIs are based on the principles of REST and are commonly used for building web services.

RESTful APIs use standard HTTP methods to perform operations on resources. The most common HTTP methods used in REST are:

### Method Descriptions

# GET: Retrieve a resource
# POST: Create a new resource
# PUT: Update an existing resource or create a new resource if it doesn’t exist
# DELETE: Delete a resource
# PATCH: Partially update a resource
# OPTIONS: Retrieve information about the communication options for a resource
# HEAD: Retrieve the headers of a resource without the body

Certain sets of methods like POST and DELETE might not be available to be used by everyone if you do not have the necessary privileges for it.

In REST, everything is a resource. A resource can be a data entity, such as a user, a product, or any other piece of information. Resources are identified by URIs (Uniform Resource Identifiers). The URI is used to address and interact with the resource. For example:

-- GET /users — Retrieve a list of users
-- GET /users/123 — Retrieve information about the user with ID 123
-- POST /users — Create a new user
-- PUT /users/123 — Update information for the user with ID 123
-- DELETE /users/123 — Delete the user with ID 123

Resources have representations, which can be in various formats such as JSON, XML, or HTML. The client and server communicate by exchanging representations of resources. JSON is a common choice for representing data in RESTful APIs due to its simplicity and widespread adoption.

Below is an image representation of the process of client-server interaction.

![Diagram](../image.webp)


### Explanation:

-- Client: Represents the application or system making the API request.
-- HTTP Request: The client in the image above initiates requests with the server by sending an HTTP request. The request -- includes the HTTP method (GET, POST, PUT, DELETE, etc.) and the URI identifying the resource.
-- Retrieve User (Server): The server receives the request, interprets the HTTP method and URI, and performs the corresponding action. In the example in the image above, retrieves user data.
-- HTTP Response: The server responds with an HTTP response, including a status code indicating the success or failure of the request and the requested user data in the response body.
-- Client: The client receives the HTTP response, processes the data, and executes actions based on the status code and response body.


### Why REST API with Python

-- The combination of Python’s ease of use, rich ecosystem, asynchronous support, and cross-platform compatibility makes it an excellent choice for working with REST APIs. Whether you’re a beginner looking to get started with API integration or an experienced developer building complex applications, Python provides the tools and resources you need to succeed.

-- Python is known for its simplicity and readability, making it an ideal language for developers of all skill levels. The syntax is straightforward and intuitive, allowing developers to quickly grasp concepts and write clean, maintainable code.

-- Python has a vast ecosystem of libraries and frameworks that cover virtually every aspect of software development. When it comes to working with REST APIs, Python offers a variety of well-maintained libraries that provide functionalities for making HTTP requests, handling responses, and managing authentication. This rich ecosystem enables developers to leverage existing tools and libraries, reducing development time and effort.

### Asynchronous Support

Asynchronous programming has become increasingly important for building high-performance, scalable applications. Python’s asyncio library, along with asynchronous library like aiohttp and Tornado, enables developers to write efficient, non-blocking code for handling concurrent requests and I/O operations. This asynchronous support is particularly valuable when working with REST APIs that require efficient handling of multiple concurrent requests.


###  HTTP status code
### Below is a list of the most common status codes returned by REST APIs:

Code	Meaning	                Description
200	    OK	                    The requested action was successful.
201	    Created	                A new resource was created.
202	    Accepted	            The request was received, but no modification has been made yet.
204	    No Content	            The request was successful, but the response has no content.
400	    Bad Request	            The request was malformed.
401	    Unauthorized	        The client is not authorized to perform the requested action.
404	    Not Found	            The requested resource was not found.
415	    Unsupported Media Type	The request data format is not supported by the server.
422	    Unprocessable Entity	The request data was properly formatted but contained invalid or missing data.
500	    Internal Server Error	The server threw an error when processing the request.

## These ten status codes represent only a small subset of the available HTTP status codes. Status codes are numbered based on the category of the result:

Code range	    Category
2xx	        Successful operation
3xx	        Redirection
4xx	        Client error
5xx	        Server error


### REST Architecture
REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.

# REST defines the following architectural constraints:

** Stateless: The server won’t maintain any state between requests from the client.
** Client-server: The client and server must be decoupled from each other, allowing each to develop independently.
** Cacheable: The data retrieved from the server should be cacheable either by the client or by the server.
** Uniform interface: The server will provide a uniform interface for accessing resources without defining their representation.
** Layered system: The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.
** Code on demand (optional): The server may transfer code to the client that it can run, such as JavaScript for a single-page application.


### REST APIs and Web Services
A REST web service is any web service that adheres to REST architecture constraints. These web services expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs.

`https://api.github.com/users/<username>`

This URL allows you to access information about a specific GitHub user. You access data from a REST API by sending an HTTP request to a specific URL and processing the response.

###
    `https://docs.github.com/en/rest/about-the-rest-api/about-the-rest-api`
    