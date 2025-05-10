from datetime import datetime

from app.utils import round_minutes


def test_base_interval_no_change():
    _ = datetime(year=2025, month=1, day=1, hour=1, minute=15)
    assert round_minutes.round_minutes(_) == _


def test_base_interval_round_up():
    _ = datetime(year=2025, month=1, day=1, hour=1, minute=1)
    assert round_minutes.round_minutes(_) == datetime(
        year=2025, month=1, day=1, hour=1, minute=15
    )


def test_base_interval_round_up_next_hour():
    _ = datetime(year=2025, month=1, day=1, hour=1, minute=46)
    assert round_minutes.round_minutes(_) == datetime(year=2025, month=1, day=1, hour=2)


def test_base_interval_round_up_next_day():
    _ = datetime(year=2025, month=1, day=1, hour=23, minute=46)
    assert round_minutes.round_minutes(_) == datetime(year=2025, month=1, day=2, hour=0)


def test_base_interval_round_up_month():
    _ = datetime(year=2025, month=12, day=30, hour=23, minute=55)
    assert round_minutes.round_minutes(_) == datetime(
        year=2025, month=12, day=31, hour=0
    )


def test_base_interval_round_up_year():
    _ = datetime(year=2025, month=12, day=31, hour=23, minute=55)
    assert round_minutes.round_minutes(_) == datetime(year=2026, month=1, day=1, hour=0)


def test_custom_interval_no_change():
    _ = datetime(year=2025, month=1, day=1, hour=15, minute=30)
    assert round_minutes.round_minutes(_, 30) == _


def test_custom_interval_round_up():
    _ = datetime(year=2025, month=1, day=1, hour=13, minute=1)
    assert round_minutes.round_minutes(_, 30) == datetime(
        year=2025, month=1, day=1, hour=13, minute=30
    )


def test_custom_interval_round_up_next_hour():
    _ = datetime(year=2025, month=1, day=1, hour=1, minute=31)
    assert round_minutes.round_minutes(_, 30) == datetime(
        year=2025, month=1, day=1, hour=2
    )
