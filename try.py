from string import hexdigits
from bitcoinrpc.authproxy import AuthServiceProxy

u = '__cookie__'
p = '0fa5a0ff724514aca2968a45370d7ce02b561c1efd12f822618f49d332bca884'

# rpc_user and rpc_password are set in the bitcoin.conf file
# rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(u, p))
#best_block_hash = rpc_connection.getbestblockhash()
#print(rpc_connection.getblock(best_block_hash))

# batch support : print timestamps of blocks 0 to 99 in 2 RPC round-trips:
commands = [ [ "getblockhash", height] for height in range(757200, 757244) ]
block_hashes = rpc_connection.batch_(commands)
blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
block_times = [ block["time"] for block in blocks ]

print(block_times)
