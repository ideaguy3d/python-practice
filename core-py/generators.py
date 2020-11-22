# this file practices generators

def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count: return
        counter += 1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen: continue
        yield item
        seen.add(item)

def run_pipeline():
    items = [3,7,7,2,11,11]
    for item in take(3, distinct(items)):
        print(item)



run_pipeline()