from pptx.util import Inches


def add_slide(prs, title, points):

    layout = prs.slide_layouts[1]

    slide = prs.slides.add_slide(layout)

    slide.shapes.title.text = title

    tf = slide.placeholders[1].text_frame

    tf.clear()

    for p in points:

        paragraph = tf.add_paragraph()
        paragraph.text = p
        paragraph.level = 0

    return slide
