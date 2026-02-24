# business.py
"""
Business layer sits between Service and DAL.

Business rules (examples):
- Movie release_year must be reasonable.
- runtime_minutes if provided must be > 0.
- List name cannot be empty.
"""

from typing import Optional, Any, Dict, List
from dal.movies_dao import MoviesDAO
from dal.lists_dao import ListsDAO


class BusinessLayer:
    def __init__(self):
        self.movies = MoviesDAO()
        self.lists = ListsDAO()

    # ----------------------
    # Movies (CRUD)
    # ----------------------
    def create_movie(self, title: str, release_year: int,
                     runtime_minutes: Optional[int], genre: Optional[str]) -> int:
        title = (title or "").strip()
        if not title:
            raise ValueError("Movie title is required.")
        if not (1888 <= release_year <= 2100):
            raise ValueError("release_year must be between 1888 and 2100.")
        if runtime_minutes is not None and runtime_minutes <= 0:
            raise ValueError("runtime_minutes must be > 0 if provided.")
        return self.movies.create(title, release_year, runtime_minutes, genre)

    def get_movie_by_id(self, movie_id: int) -> Optional[Dict[str, Any]]:
        return self.movies.get_by_id(movie_id)

    def list_movies(self) -> List[Dict[str, Any]]:
        return self.movies.list_all()

    def update_movie(self, movie_id: int, title: str, release_year: int,
                     runtime_minutes: Optional[int], genre: Optional[str]) -> bool:
        existing = self.movies.get_by_id(movie_id)
        if not existing:
            raise ValueError("Movie not found.")
        title = (title or "").strip()
        if not title:
            raise ValueError("Movie title is required.")
        if not (1888 <= release_year <= 2100):
            raise ValueError("release_year must be between 1888 and 2100.")
        if runtime_minutes is not None and runtime_minutes <= 0:
            raise ValueError("runtime_minutes must be > 0 if provided.")
        return self.movies.update(movie_id, title, release_year, runtime_minutes, genre)

    def delete_movie(self, movie_id: int) -> bool:
        existing = self.movies.get_by_id(movie_id)
        if not existing:
            raise ValueError("Movie not found.")
        return self.movies.delete(movie_id)

    # ----------------------
    # Lists (CRUD + read items)
    # ----------------------
    def create_list(self, user_id: int, name: str,
                    description: Optional[str], is_public: bool) -> int:
        name = (name or "").strip()
        if not name:
            raise ValueError("List name is required.")
        return self.lists.create(user_id, name, description, is_public)

    def list_lists_by_user(self, user_id: int) -> List[Dict[str, Any]]:
        return self.lists.list_by_user(user_id)

    def update_list(self, list_id: int, name: str,
                    description: Optional[str], is_public: bool) -> bool:
        name = (name or "").strip()
        if not name:
            raise ValueError("List name is required.")
        return self.lists.update(list_id, name, description, is_public)

    def delete_list(self, list_id: int) -> bool:
        return self.lists.delete(list_id)

    def list_items_for_list(self, list_id: int) -> List[Dict[str, Any]]:
        return self.lists.list_items_for_list(list_id)

