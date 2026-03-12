def create_slide_plan(topic, slides):

    plan = []

    for i in range(slides):

        plan.append({
            "title": f"{topic} Slide {i+1}",
            "points": []
        })

    return plan
