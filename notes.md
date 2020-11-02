### pylint

```
docker run -ti -v ~/splunk/etc/apps/ta-routeros:/app --rm  schose/pylint pylint /app/bin/routerosint.py
```

### run eventgen

```
docker run -ti --rm -v ~/splunk/etc/apps/ta-routeros:/app weberjas/eventgen7:latest /bin/bash

splunk_eventgen -v generate ./cicd/eventgen.conf
```

# run appinspect

```
docker run -ti -v  ~/splunk/etc/apps/ta-routeros:/app --rm  weberjas/appinspect:latest /bin/bash
splunk-appinspect inspect /app --excluded-tags=check_for_expansive_permissions --output-file appinspect_result.json --mode precert
```