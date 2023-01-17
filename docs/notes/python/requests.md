+ `proxy error`

```python
session = requests.session()
session.trust_env = False
```

+ `certificate verify failed: unable to get local issuer certificate`

```python
#    :param verify: (optional) Either a boolean, in which case it controls whether we verify
#                    the server's TLS certificate, or a string, in which case it must be a path
#                    to a CA bundle to use. Defaults to ``True``.
with requests.Session() as client:
		response = client.request("GET", 
                              url, 
                              headers=headers, 
                              data=payload, 
                              verify=False # 
                             )
```

