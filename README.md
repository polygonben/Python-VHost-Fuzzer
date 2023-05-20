# Python-VHost-Fuzzer
Simple python script to fuzz for subdomains on a website.

## Installation

`git clone https://github.com/polygonben/Python-VHost-Fuzzer/` 
`cd Python-VHost-Fuzzer`
`chmod +x pyfuzz.py` 

## Usage

`./pyfuzz.py --url http://domain.com --domain domain.com --wordlist subdomains.txt`

This will send GET requests with the HTTP header `Host: example.domain.com` set. After running this you will see the response code & size of the HTTP responses. 
It is helpful to then use `--fc` (filter HTTP response code) and `--fs` (filter response size) to find a valid VHost.

For example:

`./pyfuzz.py --url http://domain.com --domain domain.com --wordlist subdomains.txt --fc 301,500,400 --fs 2345`

The above will only show you the HTTP responses that do not have HTTP codes 301 or 500 or 400 AND will not display any responses of size 2345 bytes.
