# minio

## Connect

```python
from minio import Minio
client = Minio("172.18.4.151:9089", 'admin', 'admin#1234',secure=False)
client.list_buckets()
```

## Lifecycle

```python
from minio.lifecycleconfig import LifecycleConfig, Rule, Expiration
from minio.commonconfig import Filter, ENABLED

rule = Rule(
    status=ENABLED,
    rule_filter=Filter(prefix=''),
    rule_id="delete_object_over_90_days",
    expiration=Expiration(days=90)
)
config = LifecycleConfig(rules=[rule])

client.set_bucket_lifecycle('gmobile', config)
print(client.get_bucket_lifecycle('gmobile').rules[0].expiration.days)
```

