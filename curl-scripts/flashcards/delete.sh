#!/bin/bash

curl "http://localhost:8000/flashcards/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
