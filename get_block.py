from pprint import pprint

from proxy import get_rpc_client

rpc_client = get_rpc_client()
block_count = rpc_client.getblockcount()
blockhash = rpc_client.getblockhash(block_count)
block = rpc_client.getblock(blockhash)

print("---------------------------------------------------------------")
print("Block Count:", block_count)
pprint(block)
print("---------------------------------------------------------------\n")

nTx = block['nTx']
if nTx > 10:
    it_txs = 10
    list_tx_heading = "First 10 transactions: "
else:
    it_txs = nTx
    list_tx_heading = f"All the {it_txs} transactions: "
print("---------------------------------------------------------------")
print("BLOCK: ", block_count)
print("-------------")
print("Block Hash...: ", blockhash)
print("Merkle Root..: ", block['merkleroot'])
print("Block Size...: ", block['size'])
print("Block Weight.: ", block['weight'])
print("Nonce........: ", block['nonce'])
print("Difficulty...: ", block['difficulty'])
print("Number of Tx.: ", nTx)
print(list_tx_heading)
print("---------------------")
i = 0
while i < it_txs:
    print(i, ":", block['tx'][i])
    i += 1
print("---------------------------------------------------------------\n")
