#!/bin/bash

curl "http://localhost:8000/flashcards" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
