#!/bin/bash

curl "http://localhost:8000/fitnessPlans/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
