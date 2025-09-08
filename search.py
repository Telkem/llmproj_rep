import meilisearch
client = meilisearch.Client('http://127.0.0.1:7700', '6VU7Rgs5M6vaGLvgKCyBWrh5pVW0WB9IrO93a2ObvjE')

def stock_search(query):
    return client.index('nasdaq').search(query)