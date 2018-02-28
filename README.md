## logging tool

本工具通过调用 cos python sdk，可以对 bucket 开启 logging 功能，具体操作步骤如下。

- 设置 SECRET_ID, SECRET_KEY 两个环境变量
- sudo pip install cos-python-sdk-v5-logging
- 执行 python tool.py -s  source_bucket -t target_bucket -p prefix, 对 **source_bucket** 开启 logging
  配置
- 登录 腾讯云 cos 控制台，授予根账号 **100001001014** 对 **target bucket** 的**读取**和**写入**权限
- 后续对 source bucket 的访问会生成日志文件，存放在 target_bucket 中，prefix 为日志文件的路径前缀

**注意，logging设置当前只对北京地域有效, 且只有使用 v5 xml 接口的访问记录会出现在生成的日志文件中.**

target_bucket 中生成的日志文件路径格式:
COS-BUCKET/{prefix}/{logset}/{topic}/{Y}/{m}/{d}/{time}_{random}_{index}.gz

日志文件每行为一条记录, 当前每条记录为19个字段,  字段之间以 '\t' 为分隔符，记录格式为:

| 序号   | 字段名称            | 说明        |
| ---- | --------------- | --------- |
| 01   | eventVersion    | 记录版本      |
| 02   | bucketName      | 存储桶名称     |
| 03   | qcsRegion       | 请求地域      |
| 04   | eventTime       | 事件时间      |
| 05   | eventSource     | 事件来源      |
| 06   | eventName       | 事件名称      |
| 07   | remoteIp        | 来源ip      |
| 08   | userAccessKeyId | 用户访问KeyId |
| 09   | reqQcsSource    | 请求qcs源信息  |
| 10   | reqBytesSent    | 请求字节数     |
| 11   | reqPath         | 请求路径      |
| 12   | reqMethod       | 请求方法      |
| 13   | userAgent       | 用户UA      |
| 14   | resHttpCode     | http 返回码  |
| 15   | resErrorCode    | 错误码       |
| 16   | resErrorMsg     | 错误信息      |
| 17   | resBytesSent    | 返回字节数     |
| 18   | resTotalTime    | 请求总耗时     |
| 19   | resTrueTime     | 内部处理耗时    |

如果字段为 '-', 表示记录值为空.
