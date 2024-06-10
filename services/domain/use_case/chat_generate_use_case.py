class ChatGenerateUseCase:
    def __init__(self, chat_repository):
        self.chat_repository = chat_repository

    def __call__(self, input_text: str):
        return self.chat_repository.generate(input_text=input_text)
