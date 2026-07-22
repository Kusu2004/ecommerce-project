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

    actions = {
        "browser": "Show personalized product recommendations",
        "comparer": "Show a product comparison guide or feature breakdown",
        "discount_seeker": "Show a limited-time coupon or discount offer",
        "cart_abandoner": "Show a cart recovery reminder with free shipping incentive",
        "loyal_customer": "Show loyalty rewards and exclusive member benefits"
    }

    nudges = {
        "browser": "Explore products recommended for you",
        "comparer": "Compare key features to make a confident decision",
        "discount_seeker": "Unlock a special offer before it expires",
        "cart_abandoner": "Your cart is waiting — complete your purchase and get free shipping",
        "loyal_customer": "You are a valued customer — enjoy your exclusive rewards"
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

    # Highest score
    state = max(scores, key=scores.get)

    return {
        "state": state,
        "score": scores[state],
        "confidence": f"{scores[state]}%",
        "evidence": evidence[state],
        "recommended_action": actions[state],
        "nudge": nudges[state],
        "all_scores": scores
    }