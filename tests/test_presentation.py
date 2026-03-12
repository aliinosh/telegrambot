from presentation.ppt_generator import generate_presentation


def test_ppt():

    slides = [

        {
            "title": "Test",
            "points": ["A", "B", "C"]
        }

    ]

    path = generate_presentation(slides)

    assert path is not None
