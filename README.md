# getcve
The quick and dirty CVE information retrieval script

Usage:  python3 getcve.py [CVE ID]

**Sample Output:** <br />
~/$ python3 getcve.py CVE-2021-44228

ID:  CVE-2021-44228 <br />
Published:  2021-12-10T10:15:00 <br />
CVSS Score:  9.3 <br />
Impact:  {'availability': 'COMPLETE', 'confidentiality': 'COMPLETE', 'integrity': 'COMPLETE'}

Summary:  Apache Log4j2 2.0-beta9 through 2.15.0 (excluding security releases 2.12.2, 2.12.3, and 2.3.1) JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. An attacker who can control log messages or log message parameters can execute arbitrary code loaded from LDAP servers when message lookup substitution is enabled. From log4j 2.15.0, this behavior has been disabled by default. From version 2.16.0 (along with 2.12.2, 2.12.3, and 2.3.1), this functionality has been completely removed. Note that this vulnerability is specific to log4j-core and does not affect log4net, log4cxx, or other Apache Logging Services projects.
 
