from public.models import ChatSession as DBSession
from public.utils import singleton
from talk_to_ai.domain.models import Session
from talk_to_ai.domain.repository import SessionRepository


@singleton
class DefaultSessionRepository(SessionRepository):
    def create(self, user_id: int, session_name: str):
        # check if user id is valid
        DBSession.objects.create(user_id=user_id, chat_name=session_name)
        DBSession.objects.save()

    def get(self, user_id: int, session_id: int) -> Session:
        pass

    def get_all(self, user_id: int) -> list[Session]:
        rows = DBSession.objects.get(user_id=user_id)

        info = []
        for row in rows:
            conversation = [
                [conv.role, conv.message] for conv in row.conversation_set.all()
            ]
            info.append(
                Session(
                    chat_id=row.id,
                    user_id=row.user_id,
                    chat_name=row.chat_name,
                    conversations=conversation,
                )
            )
        return info

    def update(self, user_id: int, session: Session):
        pass

    def delete(self, user_id: int, session_id: int):
        pass
