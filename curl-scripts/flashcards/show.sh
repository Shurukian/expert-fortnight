#!/bin/bash

curl "http://localhost:8000/flashcards/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
