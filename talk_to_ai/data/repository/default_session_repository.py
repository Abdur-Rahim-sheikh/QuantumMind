import logging
from typing import Optional

from public.models import ChatSession as DBSession
from public.utils import singleton
from talk_to_ai.domain.models import Session
from talk_to_ai.domain.repository import SessionRepository

logger = logging.getLogger(__name__)


@singleton
class DefaultSessionRepository(SessionRepository):
    def create(self, user_id: int, session_name: str) -> Session:
        # check if user id is valid
        session = DBSession.objects.create(user_id=user_id, chat_name=session_name)
        return Session(
            id=session.id,
            user_id=session.user_id,
            name=session.chat_name,
            conversations=session.conversations,
        )

    def get(self, user_id: int, session_id: int) -> Optional[Session]:
        try:
            row = DBSession.objects.get(user_id=user_id, id=session_id)
        except DBSession.DoesNotExist:
            return None

        return Session(
            id=row.id,
            user_id=row.user_id,
            name=row.chat_name,
            conversations=row.conversations,
        )

    def get_all(self, user_id: int) -> list[Session]:
        try:
            rows = DBSession.objects.filter(user_id=user_id)
        except DBSession.DoesNotExist:
            return []

        sessions = []
        for row in rows:
            sessions.append(
                Session(
                    id=row.id,
                    user_id=row.user_id,
                    name=row.chat_name,
                    conversations=row.conversations,
                )
            )
        return sessions

    def update(self, session: Session):
        try:
            DBSession.objects.filter(user_id=session.user_id, id=session.id).update(
                chat_name=session.name, conversations=session.conversations
            )
        except DBSession.DoesNotExist:
            raise RuntimeError(f"Session {session.name} does not exist")

    def delete(self, user_id: int, session_id: int):
        try:
            DBSession.objects.filter(user_id=user_id, id=session_id).delete()
        except DBSession.DoesNotExist:
            raise RuntimeError(f"Session {session_id} does not exist")

    def exists(self, user_id: int, session_id: int) -> bool:
        return DBSession.objects.filter(user_id=user_id, id=session_id).exists()
