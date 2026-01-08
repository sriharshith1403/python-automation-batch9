import json

# -----------------------------------
# Part A: API Interaction
# -----------------------------------
def fetch_products(url):
    """Fetch product data from API and validate response."""
    try:
        import requests   # 👈 moved INSIDE function

        response = requests.get(url, timeout=10)

        if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
            print("API response received: 200 OK")
            return response.json()

        return []
    except Exception:
        return []


# -----------------------------------
# Product Validation
# -----------------------------------
def validate_product(product):
    if not isinstance(product, dict):
        return False

    p_id = product.get("id")
    price = product.get("price")
    title = product.get("title")
    category = product.get("category")

    return (
        isinstance(p_id, int) and p_id > 0 and
        isinstance(price, (int, float)) and price > 0 and
        isinstance(title, str) and title.strip() != "" and
        isinstance(category, str) and category.strip() != ""
    )



# -----------------------------------
# Processing & File Writing
# -----------------------------------
def process_and_save(products, filename="valid_products.json"):
    if not isinstance(products, list):
        return [], 0, 0

    valid_products = [p for p in products if validate_product(p)]
    total = len(valid_products)
    avg_price = sum(p["price"] for p in valid_products) / total if total else 0

    with open(filename, "w") as f:
        json.dump(valid_products, f, indent=4)

    print(f"Valid products processed: {total}")
    print(f"Average product price: {avg_price:.2f}")
    print(f"Data saved to {filename}")

    return valid_products, total, avg_price


# -----------------------------------
# Main
# -----------------------------------
if __name__ == "__main__":
    products = fetch_products("https://fakestoreapi.com/products")
    process_and_save(products)
