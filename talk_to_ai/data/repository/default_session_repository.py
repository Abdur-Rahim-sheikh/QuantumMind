import logging

from public.models import ChatSession as DBSession
from public.utils import singleton
from talk_to_ai.domain.models import Session
from talk_to_ai.domain.repository import SessionRepository

logger = logging.getLogger(__name__)


@singleton
class DefaultSessionRepository(SessionRepository):
    def create(self, user_id: int, session_name: str):
        # check if user id is valid
        DBSession.objects.create(user_id=user_id, chat_name=session_name)

    def get(self, user_id: int, session_id: int) -> Session:
        pass

    def get_all(self, user_id: int) -> list[Session]:
        try:
            rows = DBSession.objects.filter(user_id=user_id)
        except DBSession.DoesNotExist:
            return []

        sessions = []
        for row in rows:
            sessions.append(
                Session(
                    chat_id=row.id,
                    user_id=row.user_id,
                    name=row.chat_name,
                    conversations=row.conversations,
                )
            )
        return sessions

    def update(self, user_id: int, session: Session):
        pass

    def delete(self, user_id: int, session_id: int):
        pass
