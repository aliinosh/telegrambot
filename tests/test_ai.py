from ai.slide_planner import create_slide_plan


def test_slide_plan():

    slides = create_slide_plan("AI", 5)

    assert len(slides) > 0
