### Identify Resources
Build a REST API is to identify the resources the API will manage. It’s common to describe these resources as plural nouns, like customers, events, or transactions. As you identify different resources in your web service, you’ll build out a list of nouns that describe the different data users can manage in the API.

## Define Your Endpoints

HTTP method	 API endpoint	                Description
GET	        /transactions	                Get a list of transactions.
GET	        /transactions/<transaction_id>	Get a single transaction.
POST	    /transactions	                Create a new transaction.
PUT	        /transactions/<transaction_id>	Update a transaction.
PATCH	    /transactions/<transaction_id>	Partially update a transaction.
DELETE	    /transactions/<transaction_id>	Delete a transaction.

# six endpoints cover all the operations that you’ll need to create, read, update, and delete transactions in the web service. Each resource in your web service would have a similar list of endpoints based on what actions a user can perform with the API.

HTTP method	        API endpoint	                         Description
GET	            /events/<event_id>/guests	            Get a list of guests.
GET	            /events/<event_id>/guests/<guest_id>	Get a single guest.
POST	        /events/<event_id>/guests	            Create a new guest.
PUT	            /events/<event_id>/guests/<guest_id>	Update a guest.
PATCH	        /events/<event_id>/guests/<guest_id>	Partially update a guest.
DELETE	        /events/<event_id>/guests/<guest_id>	Delete a guest.



#### Design Success Responses
All responses from your REST API should have a similar format and include the proper HTTP status code.

In this section, you’ll look at some example HTTP responses for a hypothetical API that manages an inventory of cars. These examples will give you a sense of how you should format your API responses. To make things clear, you’ll look at raw HTTP requests and responses instead of using an HTTP library like requests.

