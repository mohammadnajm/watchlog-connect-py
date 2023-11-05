# watchlog

A Node.js client for [watchlog](https://watchlog.us/) server .



## Usage

```python

from watchlog import watchlogConnect
import asyncio

# Send Metric: Increments a stat by a value (default is 1)
await ws_client.increment("Your_metric")
await ws_client.increment("Your_metric" , 75)

# Send Metric: Decrements a stat by a value (default is 1)
await ws_client.decrement("Your_metric")
await ws_client.decrement("Your_metric" , 25)

# Send Metric: Percentage a stat by a value (value is required. min is 0 and max is 100)
await ws_client.percentage("Your_metric" , 12.23)

# Send Metric: To measure a specific metric (value is required)
await ws_client.gauge("Your_metric" , 12.23)

# Send Metric: To send byte of a metric (value is required)
await ws_client.systembyte("Your_metric" , 1024000000) //for example : 1024000000 is 1 GB

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())


```
