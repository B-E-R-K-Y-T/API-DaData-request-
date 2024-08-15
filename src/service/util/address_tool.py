from typing import Optional


def get_full_address(data: dict[str, Optional[str]]) -> str:
    """
    Формирует полный адрес на основе предоставленных данных.
    Учитываются только заданные ключи.

    :param data: Словарь с частями адреса, где ключи - это названия частей адреса, а значения - строки адреса.
    :return: Полный адрес, состоящий из непустых значений.
    """
    # Определяем ключи, которые используются для формирования полного адреса
    target_keys = (
        "postal_code",
        "country",
        "federal_district",
        "region_with_type",
        "city_area",
        "street_with_type",
        "house_type_full",
        "house",
    )

    # Извлекаем части адреса на основе заданных ключей
    address_parts = (
        item for key, item in data.items()
        if item is not None and key in target_keys
    )

    full_address = " ".join(address_parts)

    return full_address


__all__ = (
    get_full_address.__name__,
)
