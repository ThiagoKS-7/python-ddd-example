from typing import List, Any

from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.Response import Response


class BackofficeUsersResponse(Response):

    def __init__(self, users: List[User], **metadata: Any):
        self.__users = users
        self.__meta = metadata

    def to_primitives(self) -> Any:
        json_users = [user.to_primitives() for user in self.__users]
        response = {
            'data': json_users,
        }
        if self.__meta:
            response['meta'] = self.__meta
        return response
