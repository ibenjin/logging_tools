# -*- coding=UTF-8 -*-

import sys
import time
import os
import getopt

from qcloud_cos import CosS3Client
from qcloud_cos import CosConfig

SECRET_ID = os.environ["SECRET_ID"]
SECRET_KEY = os.environ["SECRET_KEY"]


def test_put_get_bucket_logging(src_bucket, target_bucket, target_prefix):
    logging_config = {
        'LoggingEnabled': {
            'TargetBucket': target_bucket,
            'TargetPrefix': target_prefix,
        }
    }
    beijing_conf = CosConfig(
        Region="ap-beijing",
        Secret_id=SECRET_ID,
        Secret_key=SECRET_KEY
    )
    logging_client = CosS3Client(beijing_conf)
    response = logging_client.put_bucket_logging(
        Bucket=src_bucket,
        BucketLoggingStatus=logging_config
    )
    print response
    time.sleep(3)
    response = logging_client.get_bucket_logging(
        Bucket=src_bucket
    )
    print response
    assert response['LoggingEnabled']['TargetBucket'] == target_bucket
    assert response['LoggingEnabled']['TargetPrefix'] == target_prefix


def usage():
    print(
        """
        Usage: python tool.py [option]
        -h or --help：show this help
        -s or --source：source bucket name, e.g. chenxiloggingtest-1253870963
        -t or --target：target bucket name, e.g. loggingtarget-1253870963
        -p or --prefix：log file path prefix, e.g. prefixloggingtest
        """
    )
    sys.exit()


if __name__ == "__main__":
    src_bucket = ""
    target_bucket = ""
    target_prefix = ""
    try:
        options, args = getopt.getopt(sys.argv[1:], "hs:t:p:", ["help", "source=", "target=", "prefix="])
    except getopt.GetoptError:
        sys.exit()
    for name, value in options:
        if name in ("-h", "--help"):
            usage()
        if name in ("-s", "--source"):
            src_bucket = value
            print 'source bucket is ---', value
        if name in ("-t", "--target"):
            target_bucket = value
            print 'target bucket is ---', value
        if name in ("-p", "--prefix"):
            target_prefix = value
            print 'prefix is ---', value
    # check args
    if src_bucket == "" or target_bucket == "" or target_prefix == "":
        print "all args can not be empty, use -h to show help"
        usage()
    if len(src_bucket.split("-")) < 2 or len(target_bucket.split("-")) < 2:
        print "source bucket or target bucket name invalid, " \
              "use long bucket name including appid, e.g. chenxiloggingtest-1253870963"
        sys.exit()
    print "args: ", options

    # check env
    if SECRET_ID == "" or SECRET_KEY == "":
        print "please set env SECRET_ID and SECRET_KEY, use your Tencent Cloud (SecretId, SecretKey)"
        sys.exit()

    # set and get source bucket logging config
    test_put_get_bucket_logging(src_bucket, target_bucket, target_prefix)
