import json
import os
import boto3
import platform
import logging

logger = logging.getLogger()
logLevelTable={'DEBUG':logging.DEBUG,'INFO':logging.INFO,'WARNING':logging.WARNING,'ERROR':logging.ERROR,'CRITICAL':logging.CRITICAL}
if 'LOG_LEVEL' in os.environ and os.getenv("LOG_LEVEL") in logLevelTable :
    logLevel = logLevelTable[os.getenv("LOG_LEVEL")]
else:
    logLevel=logging.WARNING # デフォルトは警告以上をログ出力する
logger.setLevel(logLevel)

def lambda_handler(event, context):
    logger.debug(f'start')

    # 動作環境確認
    logger.debug(f'python_version : {platform.python_version()}')
    logger.debug(f'boto3.version : {boto3.__version__}')

    try:
        # ダミーログ出力
        logger.debug(f'これは [DEBUG] レベルのログ出力です')
        logger.info(f'これは [INFO] レベルのログ出力です')
        logger.warn(f'これは [WARNING] レベルのログ出力です')
        logger.error(f'これは [ERROR] レベルのログ出力です')
        logger.critical(f'これは [CRITICAL] レベルのログ出力です')

        logger.debug(f'success')
        
    except Exception as e:
        logger.error(f'error: {e}')

    finally:
        logger.debug(f'finally')
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
