import panel as pn

pn.extension(sizing_mode="stretch_width")

TEXT = "Panel"

length = pn.widgets.IntSlider(value=len(TEXT), end=len(TEXT), name="length")


def text(value):
    return  TEXT[:value]

pn.Column(length, pn.bind(text, length)).servable() 

