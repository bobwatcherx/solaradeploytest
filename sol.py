# sol.py
import solara


@solara.component
def Page():
    with solara.Column():
        solara.Title("nice app")
    with solara.Columns([1, 2]):
        solara.Button("nice", color="primary")
        solara.Button("nice222", color="red")