from app.repos.areas_repo import AreasRepo


def get_areas_repo() -> AreasRepo:
    from app.repos.mocks.areas_mock import AreasMock

    return AreasMock()
