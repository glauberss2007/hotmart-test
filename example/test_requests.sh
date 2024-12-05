#!/bin/bash

# Test document processing endpoint
echo "Testing document processing endpoint..."
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hotmart is a global technology and education company, a leader in the digital products market, headquartered in Amsterdam, Netherlands, with offices in Brazil, Spain, Colombia, Mexico, the United States, the United Kingdom, and Mexico."
  }'

echo -e "\n\nWaiting for 5 seconds before testing query endpoint..."
sleep 5

# Test query processing endpoint
echo "Testing query processing endpoint..."
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Where is the hotmart headquarter?"
  }'

echo -e "\n\nTesting another query..."
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Does hotmar has any office?"
  }'

echo -e "\n\nDone testing!"