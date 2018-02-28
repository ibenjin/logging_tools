## logging tool

本工具通过调用 cos python sdk，可以对 bucket 开启 logging 功能，具体操作步骤如下。

- 设置 SECRET_ID, SECRET_KEY 两个环境变量
- pip install cos-python-sdk-v5-logging
- python tool.py -s  source_bucket -t target_bucket -p prefix
- 登录 腾讯云 cos 控制台，授予根账号 100001001014 对 target bucket 的读取和写入权限

注意，logging设置只对北京地域有效
