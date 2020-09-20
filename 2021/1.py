import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[.]{2,}', '.', new_id)
    while new_id.startswith('.'): new_id = new_id[1:]
    while new_id.endswith('.'): new_id = new_id[:-1]
    if not new_id: new_id = 'a'
    if len(new_id) >= 16: new_id = new_id[:15]
    while new_id.endswith('.'): new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    return new_id