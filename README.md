Check if your password is pwned against *pwnedpasswords.com* database. With minimal code, easy to check.
```
$ python3 ispwpwnd.py

Type a clear text password followed by key <enter>, the first 5 hex digits of its sha1 hash will be sent to https://api.pwnedpasswords.com/range/ for lookup (ctrl-c to exit):

password1
password1: found with 2413945 occurences (sha1-hash: E38AD214943DAAD1D64C102FAEC29DE4AFE9DA3D, sent E38AD to https://api.pwnedpasswords.com/range/E38AD)
^D
```

Check a list of passwords (newline separated):
```
$ echo password1 > passwords.txt
$ echo password123 >> passwords.txt
$ cat passwords.txt | python3 ispwpwnd.py

password1: found with 2413945 occurences (sha1-hash: E38AD214943DAAD1D64C102FAEC29DE4AFE9DA3D, sent E38AD to https://api.pwnedpasswords.com/range/E38AD)
password123: found with 121251 occurences (sha1-hash: CBFDAC6008F9CAB4083784CBD1874F76618D2A97, sent CBFDA to https://api.pwnedpasswords.com/range/CBFDA)
```

Run
-
```
git clone git@github.com:damiencorpataux/ispwpwnd.git
cd ispwpwnd
pip3 install requests
python3 ispwpwnd.py
```

Docker
-
```
git clone git@github.com:damiencorpataux/ispwpwnd.git
cd ispwpwnd
docker build -t ispwpwnd .
docker run -it --rm ispwpwnd
```

Taken from https://github.com/mikepound/pwned-search
