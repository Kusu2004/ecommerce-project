def classify_shopper(features):

    scores = {
        "browser": 0,
        "comparer": 0,
        "discount_seeker": 0,
        "cart_abandoner": 0,
        "loyal_customer": 0
    }
    evidence = {
        "browser": [],
        "comparer": [],
        "discount_seeker": [],
        "cart_abandoner": [],
        "loyal_customer": []
    }

    # Browser
    if features["product_views"] >= 3:
        scores["browser"] += 30
        evidence["browser"].append(
            f"Viewed {features['product_views']} products"
        )

    # Comparer
    if features["comparisons"] >= 2:
        scores["comparer"] += 50
        evidence["comparer"].append(
            f"Compared {features['comparisons']} products"
        )

    if features["product_views"] >= 5:
        scores["comparer"] += 20
        evidence["comparer"].append(
            f"Viewed {features['product_views']} products"
        )

    # Discount Seeker
    if features["coupon_searches"] >= 2:
        scores["discount_seeker"] += 50
        evidence["discount_seeker"].append(
            f"Searched for coupons {features['coupon_searches']} times"
        )

    if features["discount_page_views"] >= 2:
        scores["discount_seeker"] += 30
        evidence["discount_seeker"].append(
            f"Visited discount pages {features['discount_page_views']} times"
        )

    # Cart Abandoner
    if features["cart_additions"] >= 1 and features["purchases"] == 0:
        scores["cart_abandoner"] += 80
        evidence["cart_abandoner"].append(
            "Added product to cart but did not purchase"
        )

    # Loyal Customer
    if features["purchases"] >= 3:
        scores["loyal_customer"] += 80
        evidence["loyal_customer"].append(
            f"Completed {features['purchases']} purchases"
        )

    # Find highest score
    state = max(scores, key=scores.get)

    return {
        "state": state,
        "score": scores[state],
        "evidence": evidence[state],
        "all_scores": scores
    }

def extract_features(events):
    features = {
        "product_views": 0,
        "searches": 0,
        "comparisons": 0,
        "cart_additions": 0,
        "purchases": 0,
        "coupon_searches": 0,
        "discount_page_views": 0,
        "repeat_visits": 0
    }

    for event in events:

        if event.event_type == "product_view":
            features["product_views"] += 1

        elif event.event_type == "search":
            features["searches"] += 1

        elif event.event_type == "compare":
            features["comparisons"] += 1

        elif event.event_type in ["add_to_cart", "cart_add"]:
            features["cart_additions"] += 1

        elif event.event_type == "purchase":
            features["purchases"] += 1

        elif event.event_type == "coupon_search":
            features["coupon_searches"] += 1

        elif event.event_type == "discount_page_view":
            features["discount_page_views"] += 1

        elif event.event_type == "repeat_visit":
            features["repeat_visits"] += 1

    return features