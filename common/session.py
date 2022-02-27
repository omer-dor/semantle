from datetime import datetime

from pymongo import MongoClient
from redis.client import Redis


from common import config


def get_mongo():
    db = MongoClient(config.mongo).Semantle
    if datetime.strptime(config.twitter_date, '%Y-%m-%d') <= datetime.utcnow():
        return db.tword2vec
    else:
        return db.word2vec


def get_redis():
    return Redis.from_url(config.redis, decode_responses=True)
