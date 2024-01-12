# index-refresh

This repo contains python script to refresh index patterns in opensearch. The opensearch url, username and passport can be passed as environment variables.

```
opensearch_username = os.environ.get("username")
opensearch_password = os.environ.get("password")
opensearch_url = os.environ.get("url")
```

You can run the docker image using the below command:

```
docker run -e "username=admin" -e "password=admin" -e "url=https://localhost:9200" imageimpressario/index-refresh
```
