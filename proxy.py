import os

from bitcoinlib.services.bitcoind import BitcoindClient
from bitcoinrpc.authproxy import AuthServiceProxy
from dotenv import load_dotenv

load_dotenv()

RPC_USER = os.environ.get("RPC_USER")
RPC_PASS = os.environ.get("RPC_PASS")
RPC_HOST = os.environ.get("RPC_HOST")
RPC_PORT = os.environ.get("RPC_PORT")
DEFAULT_WALLET = os.environ.get("DEFAULT_WALLET")

SERVICE_URL = f"http://{RPC_USER}:{RPC_PASS}@{RPC_HOST}:{RPC_PORT}"


def get_rpc_client(url=SERVICE_URL):
    rpc_client = AuthServiceProxy(url, timeout=120)

    return rpc_client


def get_bitcoind_client(base_url=SERVICE_URL, wallet_name=DEFAULT_WALLET):
    if wallet_name:
        base_url += f"/wallet/{wallet_name}"
    bdc = BitcoindClient(base_url=base_url)

    return bdc
