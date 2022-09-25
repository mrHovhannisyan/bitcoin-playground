from pprint import pprint

from proxy import get_rpc_client

rpc_client = get_rpc_client()

print("Creating a Transaction")

# 0. Create New Addresses
new_address = rpc_client.getnewaddress()
new_change_address = rpc_client.getrawchangeaddress()

# 1. Select UTXO
utxos = rpc_client.listunspent()
selected_utxo = utxos[0]  # we select the first utxo here
utxo_address = selected_utxo['address']
utxo_txid = selected_utxo['txid']
utxo_vout = selected_utxo['vout']
utxo_amt = float(selected_utxo['amount'])
# here we are sending bitcoins to an address generated by us in our own wallet.
recipient_address = new_address
recipient_amt = utxo_amt / 2  # sending half coins to recipient
miner_fee = 0.00000300  # choose appropriate fee based on your tx size
change_address = new_change_address
change_amt = float('%.8f' % ((utxo_amt - recipient_amt) - miner_fee))
print("---------------------------------------------------------------")
print("Transaction Details:")
print("-------------------")
print("UTXO Address.......: ", utxo_address)
print("UTXO Txid..........: ", utxo_txid)
print("Vector ID of Output: ", utxo_vout)
print("UTXO Amount........: ", utxo_amt)
print("Tx Amount..........: ", recipient_amt)
print("Recipient Address..: ", recipient_address)
print("Change Address.....: ", change_address)
print("Miner Fee..........: ", miner_fee)
print("Change Amount......: ", change_amt)
print("---------------------------------------------------------------\n")

# 2. Create Raw Transaction
txids_vouts = [{"txid": utxo_txid, "vout": utxo_vout}]
addresses_amts = {f"{recipient_address}": recipient_amt, f"{change_address}": change_amt}
unsigned_tx_hex = rpc_client.createrawtransaction(txids_vouts, addresses_amts)
print("---------------------------------------------------------------")
print("Unsigned Transaction Hex: ", unsigned_tx_hex)
print("---------------------------------------------------------------\n")

# 3. Sign Raw Transaction
address_priv_key = [rpc_client.dumpprivkey(utxo_address)]  # list of priv keys of each utxo
signed_tx = rpc_client.signrawtransactionwithkey(unsigned_tx_hex, address_priv_key)
print("---------------------------------------------------------------")
print("Signed Transaction: ")
print("----------------------")
pprint(signed_tx)
print("---------------------------------------------------------------\n")

# 4. Broadcast Transaction
send_tx = rpc_client.sendrawtransaction(signed_tx['hex'])
print("---------------------------------------------------------------")
print("TXID of sent transaction: ", send_tx)
