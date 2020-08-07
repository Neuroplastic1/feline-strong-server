#!/bin/bash

curl "http://localhost:8000/fitnessPlans/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
