# File Storage API

This is a simple API for storing files. It is designed to be used with the [File Storage Client](https://github.com/struckchure/file-storage-client).

It can also be used as a standalone API on RESTFul communications over HTTP/HTTPS. By default it runs on port `1276`

# Running image

To run the container, using `docker`. Pull from any registry, DockerHub or GitHub, both registries are linked to this repository and work exactly the same.

- DockerHub

```sh
$ docker pull struckchure/file_storage
$ docker run -p 1276:1276 -it struckchure/file_storage
```

- GitHub

```sh
$ docker pull ghcr.io/struckchure/file_storage
$ docker run -p 1276:1276 -it ghcr.io/struckchure/file_storage
```

# Running from source

To run the API from source, you need to have `python3` and `pip3` installed. Then you can install the dependencies and run the API.

```sh
$ git clone git@github.com:struckchure/file_storage_api.git
$ cd file_storage_api
$ pip3 install -r requirements.txt
$ python3 manage.py runserver 1276
```

# Using the API

- `POST api/v1/files/` - Upload a file

Upload file using the key `file` in the request body.\
Example (using `curl`):

```sh
$ curl -F "file=@/path/to/file" -X POST http://localhost:1276/api/v1/files/
```

- `GET api/v1/files/` - Get a list of all files

List all files in the database (not sure if you want to do this, but it's there).\
Example (using `curl`):

```sh
$ curl http://localhost:1276/api/v1/files/
```

- `GET api/v1/files/<file_id>` - Get a file by ID

Get a file by ID.\
Example (using `curl`):

```sh
$ curl http://localhost:1276/api/v1/files/c678409202e12677e2c4/
```

- `PUT api/v1/files/<file_id>` - Update a file by ID

Update a file by ID.\
Example (using `curl`):

```sh
$ curl -F "file=@/path/to/file" -X PUT http://localhost:1276/api/v1/files/c678409202e12677e2c4/
```

- `DELETE api/v1/files/<file_id>` - Delete a file by ID

Delete a file by ID.\
Example (using `curl`):

```sh
$ curl -X DELETE http://localhost:1276/api/v1/files/c678409202e12677e2c4/
```
