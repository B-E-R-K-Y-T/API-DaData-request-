import http

import pytest

MOSCOW_CORDS = (55.878, 37.653)


@pytest.mark.parametrize(
    ["lat", "lon", "radius_meters", "count"],
    [
        (*MOSCOW_CORDS, 1, 1),
        (45.232, -122.41, 1000, 100),
        (-45.232, 122.411, 10, 10),
        (-45.232, -122.41, 10, 10),
        (*MOSCOW_CORDS, 10, 10),
    ],
)
def test_geolocate_address(
    lat: float, lon: float, radius_meters: int, count: int, base_url, client
):
    args = (
        "GET",
        f"{base_url}/geolocate/address",
    )

    assert (
        client(
            *args,
            params={
                "lat": lat,
                "lon": lon,
                "radius_meters": radius_meters,
                "count": count,
            },
        ).status_code == http.HTTPStatus.OK
    )


@pytest.mark.parametrize(
    ["lat", "lon", "radius_meters", "count", "status_code"],
    [
        (0.0, 2342340.0243234, 1, 1, http.HTTPStatus.BAD_REQUEST),
        (111111.0, 0.0, 1, 1, http.HTTPStatus.BAD_REQUEST),
        (0.0, 0.0, -1, 1, http.HTTPStatus.UNPROCESSABLE_ENTITY),
        (0.0, 0.0, 1, -1, http.HTTPStatus.UNPROCESSABLE_ENTITY),
        (0.0, 0.0, 1, 101, http.HTTPStatus.UNPROCESSABLE_ENTITY),
        (0.0, 0.0, 1001, 1, http.HTTPStatus.UNPROCESSABLE_ENTITY),
    ],
)
def test_geolocate_address_fail(
    lat: float,
    lon: float,
    radius_meters: int,
    count: int,
    status_code: int,
    base_url,
    client,
):
    args = (
        "GET",
        f"{base_url}/geolocate/address",
    )

    assert (
        client(
            *args,
            params={
                "lat": lat,
                "lon": lon,
                "radius_meters": radius_meters,
                "count": count,
            },
        ).status_code == status_code
    )


@pytest.mark.parametrize(
    ["lat", "lon", "radius_meters", "count"],
    [
        (*MOSCOW_CORDS, 1, 1),
    ],
)
def test_geolocate_address_view(
    lat: float, lon: float, radius_meters: int, count: int, base_url, client
):
    args = (
        "GET",
        f"{base_url}/geolocate/address_view",
    )

    assert (
        client(
            *args,
            params={
                "lat": lat,
                "lon": lon,
                "radius_meters": radius_meters,
                "count": count,
            },
        ).status_code == http.HTTPStatus.OK
    )


@pytest.mark.parametrize(
    ["lat", "lon", "radius_meters", "count", "status_code"],
    [
        (0.0, 2342340.0243234, 1, 1, http.HTTPStatus.BAD_REQUEST),
        (111111.0, 0.0, 1, 1, http.HTTPStatus.BAD_REQUEST),
        (0.0, 0.0, -1, 1, http.HTTPStatus.UNPROCESSABLE_ENTITY),
        (0.0, 0.0, 1, -1, http.HTTPStatus.UNPROCESSABLE_ENTITY),
        (0.0, 0.0, 1, 101, http.HTTPStatus.UNPROCESSABLE_ENTITY),
        (0.0, 0.0, 1001, 1, http.HTTPStatus.UNPROCESSABLE_ENTITY),
    ],
)
def test_geolocate_address_view_fail(
    lat: float,
    lon: float,
    radius_meters: int,
    count: int,
    status_code: int,
    base_url,
    client,
):
    args = (
        "GET",
        f"{base_url}/geolocate/address_view",
    )

    assert (
        client(
            *args,
            params={
                "lat": lat,
                "lon": lon,
                "radius_meters": radius_meters,
                "count": count,
            },
        ).status_code == status_code
    )
