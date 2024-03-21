from typing import Optional

from pydantic import BaseModel


class BaseListNavigation(BaseModel):
    offset: Optional[int] = None
    limit: Optional[int] = None

    def apply_to_query(self, query):
        if self.offset is not None:
            query = query.offset(self.offset)
        if self.limit is not None:
            query = query.limit(self.limit)
        return query