import pandas as pd


def clean_sales_data(data):
    """Clean the sales data before calculations are performed."""
    cleaned_data = data.drop_duplicates().copy()
    cleaned_data["customer"] = cleaned_data["customer"].fillna("Unknown")
    cleaned_data["city"] = cleaned_data["city"].fillna("Unknown")
    cleaned_data["order_date"] = pd.to_datetime(
        cleaned_data["order_date"], errors="coerce", format="mixed"
    )
    cleaned_data = cleaned_data.dropna(subset=["order_date", "price"])
    cleaned_data = cleaned_data[
        (cleaned_data["quantity"] > 0) & (cleaned_data["price"] > 0)
    ]
    return cleaned_data


def add_sales_amount(data):
    """Add sales_amount by multiplying quantity and price."""
    data = data.copy()
    data["sales_amount"] = data["quantity"] * data["price"]
    return data
