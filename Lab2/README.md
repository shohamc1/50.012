# Networks Lab 2

All routes are idempotent as running the same query multiple times does not change the server state. In the case of POST and PUT, sending the same request again will result in a duplicate error thrown, but there is no new data written to the database.

## How 2 run

`docker compose up --build` and then run the `.http` files, preferrably run post first, then get and delete.
If everything runs successfully, there should be a line saying `Uvicorn running on http://127.0.0.1:8000`. 

## What 2 expect

Swagger documentation is available at http://localhost:8000/docs/. Making requests through the documentation page is the easiest way to test the API. Alternatively you can use any other tool and use the documentation as reference.

The GET, PUT and POST sections mimic an online grocery store with products listed with their name, price and user rating.

If product to be deleted does exist: API should return 400.
If product to be added already exists: API should return 400.
If authentication in `/secure/` fails: API should return 401.
In all other cases, the API should return 200 assuming data is correctly formatted.

The challenges completed are:
> Have a route in your application that returns a content type that is not plaintext

The route `/yee/` returns a response of type `image/jpg`.

> Some form of authorization through inspecting the request headers

The route `/secure/` requires a password in the `super-secure` header field of the request.

## How 2 improve performance

Introducing indexing on the database will improve performance for GET requests. When deployed, keeping the database and API server geographically close to each other and the client will help reduce propogation delay. In addition to these, we can introduce a reverse proxy and gunicorn to improve concurrent requests as well as introduce caching.