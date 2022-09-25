from pprint import pprint

from proxy import get_rpc_client

rpc_client = get_rpc_client()

# Look Up Wallet

wallet_info = rpc_client.getwalletinfo()
print("---------------------------------------------------------------")
print("Wallet Info:")
print("-----------")
pprint(wallet_info)
print("---------------------------------------------------------------\n")

# List UTXOs
utxos = rpc_client.listunspent()
print("Utxos: ")
print("-----")
pprint(utxos)
print("------------------------------------------\n")

# Select a UTXO - first one selected here
utxo_txid = utxos[0]['txid']

# Get UTXO Hex
utxo_hex = rpc_client.gettransaction(utxo_txid)['hex']

# Get tx Details
utxo_tx_details = rpc_client.decoderawtransaction(utxo_hex)
print("Details of Utxo with txid:", utxo_txid)
print("---------------------------------------------------------------")
print("UTXO Details:")
print("------------")
pprint(utxo_tx_details)
print("---------------------------------------------------------------\n")
