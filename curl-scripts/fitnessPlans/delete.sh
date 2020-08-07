#!/bin/bash

curl "http://localhost:8000/fitnessPlans/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
