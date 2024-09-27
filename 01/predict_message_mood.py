class SomeModel:
    def predict(self, message: str) -> float:
        pass


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    
    model = SomeModel()

    prediction = model.predict(message)

    if prediction < bad_thresholds:
        return "неуд"
    elif prediction > good_thresholds:
        return "отл"
    else:
        return "норм"