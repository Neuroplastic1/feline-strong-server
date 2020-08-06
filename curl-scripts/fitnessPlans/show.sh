#!/bin/bash

curl "http://localhost:8000/FitnessPlans/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
