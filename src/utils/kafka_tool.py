# -*- coding: utf-8 -*-

from src.modules.log import Logger
# from src.utils.tools import *
from src.config import *

MODULE_NAME = __name__.upper()
logging = Logger(console_name='.main')


def kafka_murmur2(data: bytes):
    """
    Kafka 官方 Java 版 Murmur2 的 Python 實作
    """
    length = len(data)
    seed = 0x9747b28c
    # 'm' and 'r' are mixing constants generated offline.
    # They're not so unique, so they don't have to be random.
    m = 0x5bd1e995
    r = 24

    # Initialize the hash to a 'random' value
    h = seed ^ length
    length_4 = length // 4

    for i in range(length_4):
        i_4 = i * 4
        k = struct.unpack('<I', data[i_4:i_4 + 4])[0]
        k = (k * m) & 0xffffffff
        k ^= (k >> r) & 0xffffffff
        k = (k * m) & 0xffffffff
        h = (h * m) & 0xffffffff
        h ^= k

    # Handle the last few bytes of the input array
    extra_bytes = length % 4
    if extra_bytes == 3:
        h ^= (data[(length & ~3) + 2] << 16) & 0xffffffff
    if extra_bytes >= 2:
        h ^= (data[(length & ~3) + 1] << 8) & 0xffffffff
    if extra_bytes >= 1:
        h ^= (data[length & ~3]) & 0xffffffff
        h = (h * m) & 0xffffffff

    h ^= (h >> 13) & 0xffffffff
    h = (h * m) & 0xffffffff
    h ^= (h >> 15) & 0xffffffff
    return h


def get_partition_id(consumer, topic_name: str, topic_key: str) -> int:
    # 取得分區總數
    cluster_metadata = consumer.list_topics(topic=topic_name)
    partitions = cluster_metadata.topics[topic_name].partitions
    num_partitions = len(partitions)

    # 計算 Partition ID
    # target_partition = (mmh3.hash(topic_key.encode('utf-8'), seed=0x12345678) & 0x7fffffff) % num_partitions
    target_partition = (kafka_murmur2(topic_key.encode('utf-8')) & 0x7fffffff) % num_partitions

    logging.info(f"[{topic_key}] 對應 Partition 分區 ID 為: [{target_partition}]")
    return target_partition


def producer_on_message(err, msg):
    if err is not None:
        logging.warning(f"訊息推送失敗: {err}")
    else:
        # logging.info(f"訊息成功推送到 {msg.topic()} [{msg.partition()}]")
        pass


def start_service(main_name, threads, service_function: callable, **kwargs):
    service_thread = threading.Thread(
        target=service_function,
        daemon=True,  # 當主執行緒結束時，子執行緒會被強制終止
        kwargs=kwargs,
    )
    service_thread.start()
    threads.append(service_thread)
    logging.warning(f'[{main_name}] {kwargs.get('title', '服務')}已啟動...')


def stop_all_services(main_name, stop_event, threads: list):
    logging.error(f'[{main_name}] 正在向所有執行緒發出停止訊號...', exc_info=False)
    stop_event.set()  # 發出停止訊號

    # 等待所有執行緒結束
    for thread in threads:
        if thread.is_alive():
            logging.info(f'[{main_name}] 等待 {thread.name} 執行緒結束...')
            thread.join()

    logging.warning('\n\n' + logging.title_log(f'[{main_name}] 所有執行緒服務已確實關閉'))