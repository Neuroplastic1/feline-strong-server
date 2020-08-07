#!/bin/bash

curl "http://localhost:8000/FitnessPlans/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
