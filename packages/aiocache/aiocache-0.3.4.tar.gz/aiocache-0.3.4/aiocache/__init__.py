from aiocache.cache import SimpleMemoryCache, RedisCache, MemcachedCache
from aiocache.decorators import cached, multi_cached
from aiocache import settings


__all__ = (
    'settings',
    'cached',
    'multi_cached',
    'RedisCache',
    'SimpleMemoryCache',
    'MemcachedCache',
)
