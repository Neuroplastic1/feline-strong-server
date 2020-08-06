#!/bin/bash

curl "http://localhost:8000/FitnessPlans/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
