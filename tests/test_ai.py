from ai.slide_planner import create_slide_plan


def test_slide_generation():

    topic = "Artificial Intelligence"

    slides = create_slide_plan(topic, 5)

    assert slides is not None
    assert len(slides) > 0
