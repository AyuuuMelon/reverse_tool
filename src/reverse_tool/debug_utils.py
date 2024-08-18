import time
import functools
import logging

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.debug(f"{func.__name__} took {end_time - start_time:.5f} seconds to execute")
        return result
    return wrapper

logging.basicConfig(level=logging.DEBUG,  # 设置日志级别
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 设置日期格式
                    handlers=[
                        # logging.FileHandler('app.log'),  # 将日志输出到文件
                        logging.StreamHandler()  # 将日志输出到控制台
                    ])
logger = logging.getLogger(__name__)
