#!/bin/bash
data=$(curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&fo$
echo "$data" | jq -r '.[].receiptTime' | head -n 6