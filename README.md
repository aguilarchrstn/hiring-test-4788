# SiteHost Recruitment Challenge

## Part One - Calling an API

The `fetch_dns.py` script retrieves domain and DNS record information for a customer using the SiteHost Recruitment API.

### Prerequisites
- Python 3.x

### How to run
To see the result of the API calls, run the following command in your terminal:

```bash
python3 fetch_dns.py
```

The script will output a list of domains and their associated DNS records.

## Part Two - Problem Identification

Based on the DNS records retrieved in Part One, a significant issue was identified with the customer's website configuration:

**Issue:** The A record for `site.recruitment.shq.nz` is pointing to a private IP address: `192.168.1.10`.

**Explanation:** Private IP addresses (like those in the `192.168.x.x` range) are not routable on the public internet. This means that anyone trying to access `site.recruitment.shq.nz` from outside the customer's local network will be unable to reach the website. The A record should instead point to a public IP address where the website is hosted.

### Accessing the Broken Site
To verify the site was accessible despite the DNS issue, I used `curl` to point to the server's public IP address (found via the `api` record) while manually setting the `Host` header:

```bash
curl -H "Host: site.recruitment.shq.nz" http://223.165.64.38
```

### Retrieved Code
The following code was found in the HTML comments of the site's head:
`R2F1ci9FK0pYK2dFcWd4YWVBUkZlaXVDYmNnTWJCeXRNdDhqd3lFVlNOaz0=`
