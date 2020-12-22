MAX_SIZE = 10000

YDL_OPTS = {
  'socket_timeout': 5,
  'sleep_interval': 1,
  'max_sleep_interval': 2,
  'retries': 5,
  'ratelimit': 1e6,   # 1E6 for debug on hotspot 
  'min_filesize': 1e5,
  'max_filesize': 1e7, # 1E7 for debug on hotspot
  'simulate': True
}

IP_POOLS = [
  '1.195.11.157:21158',
  '121.20.53.252:15060',
  '125.111.118.224:19365',
  '121.230.211.50:18537',
  '106.226.239.28:20426',
  '106.9.171.20:20621',
  '220.248.157.204:18528',
  '117.81.173.226:17273',
  '171.12.176.88:21839',
  '125.105.49.23:20986'
]

__proxies = {
  'http': IP_POOLS[0],
  "https": IP_POOLS[0]
}
