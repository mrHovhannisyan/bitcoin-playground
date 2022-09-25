.DEFAULT_GOAL:= help

.PHONY: createwallet
createwallet: ## Create new wallet
	docker exec --user bitcoin bitcoin-playground-node3-1 bitcoin-cli -regtest createwallet "node3_wallet"

.PHONY: getnewaddress
getnewaddress: ## Get new address
	docker exec --user bitcoin bitcoin-playground-node3-1 bitcoin-cli getnewaddress

.PHONY: getbalance
getbalance: ## Get balance
	docker exec --user bitcoin bitcoin-playground-node3-1 bitcoin-cli getbalance

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
