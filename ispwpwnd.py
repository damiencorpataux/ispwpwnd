import hashlib
import requests
import sys

baseurl = 'https://api.pwnedpasswords.com/range/'
n = 5

if sys.stdin.isatty():
    print(
        f'\nType a clear text password followed by key <enter>, '
        f'the first {n} hex digits of its sha1 hash will be sent to {baseurl} for lookup:\n')

for password in (line for line in sys.stdin if line.strip('\n')):
    password = password.strip('\n')
    hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = hash[:n], hash[n:]
    url = baseurl + head
    response = requests.get(url)
    if not response.ok:
        raise RuntimeError('Error fetching "{}": {}'.format(url, res.status_code))
    count = {tail_found: count for tail_found, count
        in (line.split(':') for line in response.text.splitlines())
        if tail_found == tail}.get(tail, 0)

    print (f'{password}: found with {count} occurences (sha1-hash: {hash}, sent {head} to {url})')
