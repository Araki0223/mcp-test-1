# シンプルなインメモリ型スレッドコンテキスト保存
# 本番ではRedisやDBに置き換え推奨

_context_store = {}

def get_or_create_context(thread_id: str):
    if thread_id not in _context_store:
        _context_store[thread_id] = []
    return _context_store[thread_id]

def update_context(thread_id: str, new_messages: list):
    context = get_or_create_context(thread_id)
    context.extend(new_messages)
    return context
