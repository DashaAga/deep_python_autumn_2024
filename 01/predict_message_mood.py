class SomeModel:

    def predict(self, message: str) -> float:
        return message[0]

    def some_function(self, smt: int) -> int:
        return smt


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:

    model = SomeModel()

    prediction = model.predict(message)

    if prediction < bad_thresholds:
        return "неуд"

    if prediction > good_thresholds:
        return "отл"

    return "норм"
