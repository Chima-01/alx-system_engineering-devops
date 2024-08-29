# Post Mortem Report

## Incident Summary:
A server failure issue was noticed, resulting from the exhaustion of the server disk space. This led to the server becoming inaccessible to clients.

## Incident Timeline:
- **Start Time:** 22:23 GMT
- **Resolution Time:** 00:27 GMT
- **Duration of Downtime:** 2 hours 4 minutes

## How issue was detected:
Issue was detected by a senior engineer who was trying to access the website, when he noticed the malfunctioning of the website.
The senior engineer escalated the issue to the junior engineers on call.

## Root Cause
The root cause of the server failure was identified as the exhaustion of disk space.

## How issue was fixed
- Using the command ```du -h /path/to/directory | sort -hr ``` large file consuming space was able to be detected.
- Old files were archive somewhere else to free up space
- Outdated and Irrelevant file were deleted
- Datadog was installed to monitor disk space and alert when space is going low.

## Preventive Measures:
To prevent similar incidents in the future, regular disk space monitoring and cleanup procedures will be implemented to ensure optimal server performance and availability.
