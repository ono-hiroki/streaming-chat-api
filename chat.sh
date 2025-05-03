#!/usr/bin/env bash

URL="http://127.0.0.1:8000/v1/chat/stream"
PAYLOAD='{"messages":[{"role":"system","content":"You are a helpful assistant."},{"role":"user","content":"やっほ"}]}'

curl -sN \
  -H "Content-Type: application/json" \
  -d "${PAYLOAD}" \
  "${URL}" |
while IFS= read -r line; do
  if [[ $line == data:* ]]; then
    printf '%s' "${line#data: }"
  elif [[ $line == event:\ done ]]; then
    break
  fi
done

printf '\n'