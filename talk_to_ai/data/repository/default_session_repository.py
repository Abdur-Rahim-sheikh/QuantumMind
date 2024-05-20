from public.models import ChatSession as DBSession
from talk_to_ai.domain.models import Session
from talk_to_ai.domain.repository import SessionRepository


class DefaultSessionRepository(SessionRepository):
    def create(self, user_id: int, session_name: str):
        # check if user id is valid
        DBSession.objects.create(user_id=user_id, chat_name=session_name)
        DBSession.objects.save()

    def get(self, session_id: int) -> Session:
        pass

    def get_all(self) -> list[Session]:
        pass

    def update(self, session: Session):
        pass

    def delete(self, session_id):
        pass
