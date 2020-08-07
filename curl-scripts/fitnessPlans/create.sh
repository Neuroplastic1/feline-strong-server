#!/bin/bash

curl "http://localhost:8000/FitnessPlans/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "fitnessPlan": {
      "date": "'"${DATE}"'",
      "plan": "'"${PLAN}"'",
      "nutrition": "'"${NUTRITION}"'"
    }
  }'

echo
