MAX_SIZE = 10000

YDL_OPTS = {
  'socket_timeout': 5,
  'sleep_interval': 1,
  'max_sleep_interval': 2,
  'retries': 5,
  'ratelimit': 1e5,   # 100k for debug on hotspot
  'min_filesize': 1e5,
  'max_filesize': 4e9
}