#!/bin/bash
# THIs script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
DEATH=$(echo $DATA | jq '.[0].death')

TODAY=$(date)
echo "On $TODAY, there were $POSITIVE positive, $NEGATIVE negative, $PENDING pending, and $DEATH death COVID cases"
