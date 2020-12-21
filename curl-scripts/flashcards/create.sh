#!/bin/bash

curl "http://localhost:8000/flashcards" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "flashcard": {
      "title": "'"${TITLE}"'",
      "question": "'"${QUESTION}"'",
      "answer": "'"${ANSWER}"'"
    }
  }'

echo
