from typing import Optional, List, Dict, Any
from db import get_conn

class ListsDAO:
    def create(self, user_id: int, name: str, description: Optional[str], is_public: bool) -> int:
        sql = """
        INSERT INTO lists (user_id, name, description, is_public)
        VALUES (%s, %s, %s, %s)
        """
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(sql, (user_id, name, description, is_public))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def list_by_user(self, user_id: int) -> List[Dict[str, Any]]:
        sql = """
        SELECT list_id, user_id, name, description, is_public, created_at
        FROM lists
        WHERE user_id=%s
        ORDER BY created_at DESC
        """
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute(sql, (user_id,))
            return cur.fetchall()
        finally:
            conn.close()

    def update(self, list_id: int, name: str, description: Optional[str], is_public: bool) -> bool:
        sql = """
        UPDATE lists
        SET name=%s, description=%s, is_public=%s
        WHERE list_id=%s
        """
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(sql, (name, description, is_public, list_id))
            conn.commit()
            return cur.rowcount == 1
        finally:
            conn.close()

    def delete(self, list_id: int) -> bool:
        sql = "DELETE FROM lists WHERE list_id=%s"
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute(sql, (list_id,))
            conn.commit()
            return cur.rowcount == 1
        finally:
            conn.close()

    def list_items_for_list(self, list_id: int) -> List[Dict[str, Any]]:
        # This is great for your console "retrieve records" demo
        sql = """
        SELECT li.list_item_id, m.title, m.release_year, li.status, li.watched_on, li.notes
        FROM list_items li
        JOIN movies m ON m.movie_id = li.movie_id
        WHERE li.list_id = %s
        ORDER BY li.added_at DESC
        """
        conn = get_conn()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute(sql, (list_id,))
            return cur.fetchall()
        finally:
            conn.close()

