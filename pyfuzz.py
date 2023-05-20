#!/bin/python
import argparse
import requests
import re

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, help="URL to fuzz for subdomains", required=True)
parser.add_argument('--wordlist', type=str, help="Path to wordlist of sudomain names", required=True)
parser.add_argument('-fc', type=str, help="Filter by HTTP Response code(s)", required=False)
parser.add_argument('-fs', type=str, help="Filter by response size", required=False)
parser.add_argument('--domain', type=str, help="Domain name", required=True)
#parser.add_argument()
args = parser.parse_args()

url_check = re.findall("^(http|https)", args.url)
if len(url_check) == 0:
	print("[*] Error: Please enter in format 'https://domain.com/'")
	exit()



def fuzz(wordlist, url, status_code, size, domain_name):
	print("Starting fuzz:")
	with open(wordlist, "r") as subdomain_list:
		for subdomain in subdomain_list:
			headers = {'Host' : f'{subdomain.rstrip()}.{domain_name}'}
			response = requests.get(url, headers=headers, allow_redirects=False)
			if (str(response.status_code) in status_code or str(len(response.content)) in size) != True:
				print(f'[Status: {response.status_code}, Size: {len(response.content)}]')
				print(f'* * * Subdomain: {subdomain}')

if args.fc is not None:
	filter_codes = args.fc.split(",")
else:
	filter_codes = []

if args.fs is not None:
	filter_size = args.fs.split(",")
else:
	filter_size = []

fuzz(args.wordlist, args.url, filter_codes, filter_size, args.domain)
