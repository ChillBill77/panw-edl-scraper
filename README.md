
# Palo Alto Networks EDL Scraper

Palo Alto EDL Hosting Service is a list of Software-as-a-Service (SaaS) application endpoints maintained by Palo Alto Networks. Each Feed URL below contains an external dynamic list (EDL) that is checked daily for any new endpoints added to the publicly available Feed URLs published by the SaaS application provider. 
[To scrape and easily create the PANW External Dynamic Lists (EDL)](https://docs.paloaltonetworks.com/resources/edl-hosting-service "Palo Alto Networks")

So far so good... however there are just a couple of them.

## Challenge
How to add them efficiently to the Palo Alto Firewalls for both the IPv4 lists as well as the URL lists
- [Python] scraper.py was born

## Installation

Not really, it is just Python3
You could spin up a container with python in it.

### Windows
```sh
docker run -it --rm -v "%cd%:/workdir" -w /workdir python:latest /bin/sh (on Windows)
python3 scraper.py
```

### Linux/MAC
```sh
docker run -it --rm -v "${PWD}:/workdir" -w /workdir python:latest /bin/sh
python3 scraper.py
```

## Results

| Output        | Field Description           |
|:------------- |:-------------|
| Group     | GRP_m365_china_any_all_ipv4 | 
| URL       | https://saasedl.paloaltonetworks.com/feeds/m365/china/any/all/ipv4 |
| Description | List of all 21Vianet (China) IPv4 endpoints for all service areas |
|set_command | ```set external-list "GRP_m365_china_any_all_ipv4" type ip description "List of all 21Vianet (China) IPv4 endpoints for all service areas" urlhttps://saasedl.paloaltonetworks.com/feeds/m365/china/any/all/ipv4 recurring daily at 5``` |

The schedule for updating the EDL is random, but you could change that ;-) 

###### created with https://markdit.com/
