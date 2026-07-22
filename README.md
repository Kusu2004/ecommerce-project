# Ecommerce Personalization Rules Engine

An intelligent ecommerce personalization engine that analyzes shopper behavior and classifies users into different behavioral segments.

The system converts shopper events into behavioral features and applies a rule-based decision engine to generate personalized recommendations and nudges.

---

## Project Overview

Ecommerce users behave differently.

Some users browse products, some compare products, some search for discounts, some abandon their carts, and some become loyal customers.

This project analyzes shopper behavior and identifies the most likely shopper segment.

The system generates:

- Shopper classification
- Confidence score
- Behavioral evidence
- Recommended personalization action
- Personalized customer nudge

---

## Shopper Segments

### 1. Browser

Users who view multiple products but do not take further action.

Recommended action:

Show personalized product recommendations.

### 2. Comparer

Users who compare multiple products before making a decision.

Recommended action:

Show product comparison guides or feature breakdowns.

### 3. Discount Seeker

Users who frequently search for coupons or visit discount pages.

Recommended action:

Show limited-time coupons or discount offers.

### 4. Cart Abandoner

Users who add products to their cart but do not complete a purchase.

Recommended action:

Show cart recovery reminders with free shipping incentives.

### 5. Loyal Customer

Users who complete multiple purchases.

Recommended action:

Show loyalty rewards and exclusive member benefits.

---

## System Architecture

Shopper Events
        ↓
Feature Extraction
        ↓
Behavioral Features
        ↓
Rules Engine
        ↓
Shopper Classification
        ↓
Personalized Action
        ↓
Personalized Nudge

---

## Technology Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### Frontend

- HTML
- CSS
- JavaScript

### API Testing

- Swagger UI

---

## Backend Features

The backend provides a REST API endpoint:

POST /classify

The API accepts shopper events and returns:

- User ID
- Extracted behavioral features
- Shopper state
- Confidence score
- Evidence
- Recommended action
- Personalized nudge
- All shopper scores

---

## Example Request

```json
{
  "user_id": "user_001",
  "events": [
    {
      "event_type": "product_view",
      "timestamp": "2026-07-21T16:00:00"
    },
    {
      "event_type": "cart_add",
      "timestamp": "2026-07-21T16:03:00"
    }
  ]
}