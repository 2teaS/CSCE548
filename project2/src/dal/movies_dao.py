from typing import Optional, List, Dict, Any
from mysql.connector import Error
from db import get_conn

class MoviesDAO:
    def create(self, title: str, release_year: int, runtime_minutes: Optional[int], genre: Optional[str]) -> int:
        sql = """
        INSERT INTO movies (title, release_year, runtime_minutes, genre)
        VALUES (%s, %s, %s, %s)
        """
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(sql, (title, release_year, runtime_minutes, genre))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def get_by_id(self, movie_id: int) -> Optional[Dict[str, Any]]:
        sql = "SELECT movie_id, title, release_year, runtime_minutes, genre FROM movies WHERE movie_id=%s"
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute(sql, (movie_id,))
            return cur.fetchone()
        finally:
            conn.close()

    def list_all(self) -> List[Dict[str, Any]]:
        sql = "SELECT movie_id, title, release_year, runtime_minutes, genre FROM movies ORDER BY release_year DESC, title"
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute(sql)
            return cur.fetchall()
        finally:
            conn.close()

    def update(self, movie_id: int, title: str, release_year: int, runtime_minutes: Optional[int], genre: Optional[str]) -> bool:
        sql = """
        UPDATE movies
        SET title=%s, release_year=%s, runtime_minutes=%s, genre=%s
        WHERE movie_id=%s
        """
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(sql, (title, release_year, runtime_minutes, genre, movie_id))
            conn.commit()
            return cur.rowcount == 1
        finally:
            conn.close()

    def delete(self, movie_id: int) -> bool:
        sql = "DELETE FROM movies WHERE movie_id=%s"
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(sql, (movie_id,))
            conn.commit()
            return cur.rowcount == 1
        finally:
            conn.close()

