[![codecov](https://codecov.io/gl/hyperion-gray/googlespider/branch/master/graph/badge.svg)](https://codecov.io/gl/hyperion-gray/googlespider)
[![PyPI version](https://badge.fury.io/py/googlespider.svg)](https://badge.fury.io/py/googlespider)
[![Python version](https://img.shields.io/badge/python-3.4%2C3.5%2C3.6-blue.svg)](https://img.shields.io/badge/python-3.4%2C3.5%2C3.6-blue.svg)
Googlespider
------------

Search Google from the command line.

The Google UI is lovely to look at, but less useful if you want to do something with the results. Googlepider downloads the results from Google in friendly formats, such as csv, tsv and json.

Googlespider allows you to make (polite) batch requests - point it at a file containing a list of queries and go for a beer. This is good for some quick data-wrangling and beer-drinking, not scaleable web crawling.


Requires Python 3.4+.

Installation
------------
Using a Python3.4+ virtualenv:

```bash
$ pip install googlespider
```

Notes
-----

Automated scraping of Google is against their TOS, this script is for educational puposes only.

Only 'web' results are included. Universal results, e.g. images, news, etc., *are stripped out*.  If you want results that include these, this is not the tool you are looking for.

Requests are throttled in order to be kind to Google (30 seconds). This can be adjusted with the `-d` parameter but it is not recommended. Using Googlespider concurrently from the same IP, or even querying Google while using it, may trigger captchas and break it - it does not handle such errors.

Googlespider supports "localisation", meaning you can adjust the Google domain, request parameters, and request headers in order to obtain location-specific results. However, the only way to ensure that results accurately reflect what a user would see in a particular country is to make the request from that country. Googlespider supports this by way of the `--proxy` option.


Usage
-----

Googlespider provides a shell command. To use (with caution), simply do:

```bash
$ googlespider "hyperion gray"
```

And get the below:

```bash
hyperion gray	1	http://www.hyperiongray.com/
hyperion gray	2	https://www.punkspider.org/
hyperion gray	3	http://www.forbes.com/sites/thomasbrewster/2015/05/06/punkspider-google-for-all-web-vulnerabilities/
hyperion gray	4	https://twitter.com/hyperiongray?lang=en-gb
hyperion gray	5	http://hyperiongray.tumblr.com/
hyperion gray	6	https://www.linkedin.com/in/amanda-towler-2988167
hyperion gray	7	https://www.linkedin.com/company/hyperion-gray
hyperion gray	8	https://www.linkedin.com/in/alejandrojcaceres
hyperion gray	9	http://upstart.bizjournals.com/companies/innovation/2015/04/13/hyperion-gray-building-an-army-of-robot-interns-to.html
hyperion gray	10	http://www.theregister.co.uk/2013/02/21/punkspider/
```

You can supply multiple queries:

```bash
$ googlespider "hyperion gray" "punkspider"
```

Or point it at a file containing a list of queries (one per line):

```bash
$ googlespider @queries.txt
```

There are various options, available via `$ googlespider --help`:

```bash
usage: googlespider [-h] [-v] [-c COUNTRY] [-p PROXY] [-l LANGUAGE] [-L]
                    [-n NUM_RESULTS] [-d DELAY] [-i] [-r RESULTS_PER_PAGE]
                    [-s START_INDEX] [-f {json,tsv,csv}] [--min-date MIN_DATE]
                    [--max-date MAX_DATE]
                    [queries [queries ...]]

Command line Google search.

positional arguments:
  queries               google search queries (use @filename to read from
                        file) (default: [])

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbose logging (repeat for more verbose) (default: 2)
  -c COUNTRY, --country COUNTRY
                        google search country as ISO-3166 country code (e.g.
                        uk, us, ca) (default: us)
  -p PROXY, --proxy PROXY
                        proxy string (protocol://username:password@ip:port)
                        (default: None)
  -l LANGUAGE, --language LANGUAGE
                        ACCEPT-LANGUAGE request header (e.g. en-us, en-gb, en)
                        (More examples: https://msdn.microsoft.com/en-
                        gb/library/ee825488(v=cs.20).aspx) (default: en-US)
  -L, --localise        localise language to country (overrides -l) (default:
                        False)
  -n NUM_RESULTS, --num-results NUM_RESULTS
                        number of results to fetch (1 - 1000) (default: 10)
  -d DELAY, --delay DELAY
                        seconds to wait between requests (default: 30)
  -i, --ignore-https    supress HTTPS warnings (default: False)
  -r RESULTS_PER_PAGE, --results-per-page RESULTS_PER_PAGE
                        number of results per page (1 - 100) (default: 100)
  -s START_INDEX, --start-index START_INDEX
                        start index (1 - 999) (default: 0)
  -f {json,tsv,csv}, --format {json,tsv,csv}
                        output format (default: tsv)
  --min-date MIN_DATE   minimum date, US format, dd/mm/yyyy (default: None)
  --max-date MAX_DATE   max date, US format, dd/mm/yyyy (default: None)
```

HTTPS Warnings
--------------

Googlespider uses the requests module which in turn depends on urllib3. These will trigger various warnings when requesting secure URLs, e.g. https://www.google.com.

`InsecurePlatformWarning` and  `SNIMissingWarning` can sometimes be resolved by installing the requests package with the security dependencies:

```
$ pip install requests[security]
```

If you have not properly configured SSL certificate support you will see `InsecureRequestWarning`. You can temporarily ignore these by setting an environment variable:

```
export PYTHONWARNINGS="ignore:Unverified HTTPS request"
```

Googlespider supports laziness and insecurity by allowing you to just use the `-i` flag to supress these warnings.


Configuration
-------------
Googlespider uses config.ini files for configuration. These are used to define headers and set country-specific Google domains.

You can override settings by placing your own ini file in the following locations (in order of precedence):

* `./config.ini`
* `~/.googlespider.ini`
* `/etc/googlespider/config.ini`
