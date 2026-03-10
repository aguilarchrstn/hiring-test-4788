Hi Alice,

Thank you for reaching out.

After investigating your DNS configuration, I have identified the issue. The A record for `site.recruitment.shq.nz` is currently set to a private IP address (`192.168.1.10`), which is only accessible within a local network and cannot be reached over the public internet.

To resolve this, you will need to update the DNS record for `site.recruitment.shq.nz` to point to the correct public IP address of your web server.

As proof that I was able to access the site by bypasssing the DNS issue, here is the code retrieved from the HTML source: `R2F1ci9FK0pYK2dFcWd4YWVBUkZlaXVDYmNnTWJCeXRNdDhqd3lFVlNOaz0=`

Best regards,
Jules
