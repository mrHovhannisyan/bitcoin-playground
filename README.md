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

### Bitcoin-core nodes

Build and run docker-compose

```shell script
docker-compose build
```

```shell script
docker-compose up
```

### First things to do

1) Create a new wallet
```shell script
make createwallet
```

2) Get new address 
```shell script
make getnewaddress
```
output: `bcrt1q0kytcpq9hw6g56k9gegc0x53uk50xgv85gwe5v`

3) Copy address from step 2 and put to `address` in step 4

4) Receiving a block reward of 50 bitcoins
```shell script
docker exec --user bitcoin bitcoin-playground-node3-1 bitcoin-cli generatetoaddress 101 <address>
```
5) Check balance
```shell script
make getbalance
```

------------------------------------------------------------------------------------------------
### You can run bitcoin-cli command to get basic information of your blockchain network, for example

```shell script
docker exec --user bitcoin bitcoin-playground-node3-1 bitcoin-cli -regtest getmininginfo
```

_*for more available bitcoin-cli commands [https://developer.bitcoin.org/reference/rpc/index.html](https://developer.bitcoin.org/reference/rpc/index.html)_

------------------------------------------------------------------------------------------------
### Helpful docker commands

Connect to the container using 
`docker exec --user bitcoin -it <container-name> sh` command
```shell
docker exec --user bitcoin -it bitcoin-playground-node3-1 sh
```

To list running containers
```
docker-compose ps 
```






