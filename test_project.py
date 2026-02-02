import project

def test_normalize_answer():
    assert project.standardize(" YES ") == "yes"
    assert project.standardize("No") == "no"
    assert project.standardize("maybe") == "maybe"


def test_show_gif_opens_browser(monkeypatch):
    opened = {}

    def fake_open(url):
        opened["url"] = url

    monkeypatch.setattr("webbrowser.open", fake_open)
    project.show_gif()

    assert opened["url"] == project.GIF_URL
