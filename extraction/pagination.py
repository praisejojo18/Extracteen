from extraction.api_client import get_data


def get_all_products(url, page_size=30, headers=None):
    all_products = []
    skip = 0

    while True:
        params = {
            "limit": page_size,
            "skip": skip
        }

        result = get_data(
            url,
            params=params,
            headers=headers
        )

        if not result["success"]:
            return result

        page_data = result["data"]

        products = page_data.get("products", [])

        all_products.extend(products)

        total_products = page_data.get("total", 0)

        skip += page_size

        print(
            f"Fetched {len(all_products)} "
            f"of {total_products} products"
        )

        if skip >= total_products or not products:
            break

    return {
        "success": True,
        "status_code": 200,
        "data": all_products,
        "total_records": len(all_products)
    }