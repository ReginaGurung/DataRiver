#!/usr/bin/env bash
#
# Example usage assuming event.json exists and contains valid json:
# ./emit.sh IP_OF_EVENTSTORE:2113 test_stream test_event event.json
#

if which uuidgen >/dev/null; then
       UUID=$(uuidgen)
   else
       UUID=$(cat /proc/sys/kernel/random/uuid)
fi
echo "Emitting event with UUID: $UUID"
BASE_URL=$1
STREAM=$2
EVENT=$3
JSON_FILE=$4
curl -d @$JSON_FILE "$BASE_URL/streams/$STREAM" -H "Content-Type:application/json" -H "ES-EventType: $EVENT" -H "ES-EventId: $UUID"
