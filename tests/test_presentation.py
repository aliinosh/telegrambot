from presentation.ppt_generator import generate_presentation


def test_ppt_generation():

    slides = [

        {
            "title": "Test Slide",
            "points": [
                "Point 1",
                "Point 2",
                "Point 3"
            ]
        }

    ]

    path = generate_presentation(slides)

    assert path is not None
