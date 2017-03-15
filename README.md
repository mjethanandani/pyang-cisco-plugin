# A pyang plugin to validate Cisco native YANG models.

This pyang plugin validates Cisco device specific YANG modules per the naming conventions established within Cisco.



```
$ pyang --cisco Cisco-IOS-XR-ipv4-acl-cfg.yang
/Users/mahesh/nso/xr-models/neds/621/xrv9k62119i/src/yang/Cisco-IOS-XR-ipv4-acl-cfg.yang:14: error: module "Cisco-IOS-XR-types" not found in search path
/Users/mahesh/nso/xr-models/neds/621/xrv9k62119i/src/yang/Cisco-IOS-XR-ipv4-acl-cfg.yang:14: warning: imported module Cisco-IOS-XR-types not used
/Users/mahesh/nso/xr-models/neds/621/xrv9k62119i/src/yang/Cisco-IOS-XR-ipv4-acl-cfg.yang:16: error: module "Cisco-IOS-XR-ipv4-acl-datatypes" not found in search path
/Users/mahesh/nso/xr-models/neds/621/xrv9k62119i/src/yang/Cisco-IOS-XR-ipv4-acl-cfg.yang:18: error: module "Cisco-IOS-XR-ipv4-ace-cfg" not found in search path
/Users/mahesh/nso/xr-models/neds/621/xrv9k62119i/src/yang/Cisco-IOS-XR-ipv4-acl-cfg.yang:48: error: RFC 6087: 4.7: statement "revision" must have a "reference" substatement
/Users/mahesh/nso/xr-models/neds/621/xrv9k62119i/src/yang/Cisco-IOS-XR-ipv4-acl-cfg.yang:79: error: grouping "IPV4-ACE" not found in module Cisco-IOS-XR-ipv4-acl-cfg
```
