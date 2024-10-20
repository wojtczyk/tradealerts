from cdp import *

Cdp.configure_from_json("../../.cdk_env.json")

print("CDP SDK has been successfully configured from JSON file.")

# Create a wallet with one address by default.
wallet = Wallet.create()

# A wallet has a default address.
address = wallet.default_address

# Fund the wallet with a faucet transaction.
faucet_tx = wallet1.faucet()

print(f"Faucet transaction successfully completed: {faucet_tx}")

# Create a new wallet wallet3 to transfer funds to.
another_wallet = Wallet.create()

print(f"Wallet successfully created: {another_wallet}")

transfer = wallet.transfer(0.00001, "eth", another_wallet).wait()

print(f"Transfer successfully completed: {transfer}")

# Create a wallet on `base-mainnet` to trade assets with.
wallet = Wallet.create(network_id="base-mainnet")

print("Wallet successfully created: {wallet}")

# Fund wallet's default address with ETH from an external source.

# Trade 0.00001 ETH to USDC
trade = wallet.trade(0.00001, "eth", "usdc").wait()

if trade.status is Transaction.Status.COMPLETE:
  print(f"Trade successfully completed: {trade}")
else:
  print(f"Trade failed on-chain: {trade}")

# Trade the wallet's full balance of USDC to WETH
trade2 = wallet.trade(wallet.balance("usdc"), "usdc", "weth").wait()

if trade2.status is Transaction.Status.COMPLETE:
  print(f"Second trade successfully completed: {trade2}")
else:
  print(f"Second trade failed on-chain: {trade}")