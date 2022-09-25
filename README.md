# Bitcoin-core-three-nodes


------------------------------------------------------------------------------------------------

## Requirements

------------------------------------------------------------------------------------------------

- [Python 3.8](https://www.python.org/downloads/) or higher
- [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)


## Run on local machine

------------------------------------------------------------------------------------------------

### Make sure you’ve got Python & pip installed on your Local machine

Create a virtual environment*

```
virtualenv .venv
```

_*You'll need `virtualenv` to be installed on your system_

```
pip install virtualenv
```

Activate virtualenv

```shell script
source venv/bin/activate
```

Install dependencies

```shell script
pip install -r requirments.txt
```

Copy the `.env.example` file to `.env` and change configuration to appropriate values

```shell script
cp .env.example .env
```

### Start bitcoin-core nodes

```shell script
docker-compose up -d
```

------------------------------------------------------------------------------------------------
### You can run bitcoin-cli command to get basic information of your blockchain network, for example

```shell script
docker exec --user bitcoin bitcoin-three-nodes-node3-1 bitcoin-cli -regtest getmininginfo
```

_*for more available bitcoin-cli commands [https://developer.bitcoin.org/reference/rpc/index.html](https://developer.bitcoin.org/reference/rpc/index.html)_

------------------------------------------------------------------------------------------------
### Helpful docker commands

Connect to the container using 
`docker exec --user bitcoin -it <container-name> sh` command
```shell
docker exec --user bitcoin -it bitcoin-three-nodes-node3-1 sh
```

To list running containers
```
docker-compose ps 
```






