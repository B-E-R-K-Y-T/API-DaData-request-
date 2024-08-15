from typing import Optional


def get_full_address(data: dict[str, Optional[str]]) -> str:
    target_keys = {
        "postal_code",
        "country",
        "federal_district",
        "region_with_type",
        "city_area",
        "street_with_type",
        "house_type_full",
        "house",
    }

    address_parts = (
        item for key, item in data.items()
        if item is not None and key in target_keys
    )

    full_address = " ".join(address_parts)

    return full_address
