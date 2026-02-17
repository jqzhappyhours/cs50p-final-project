import project

def test_normalize_answer():
    assert project.standardize(" YES ") == "yes"
    assert project.standardize("No") == "no"
    assert project.standardize("maybe") == "maybe"


def test_yes_opens_yes_html(monkeypatch):
    opened = {}

    def fake_open(url):
        opened["url"] = url

    # Replace webbrowser.open with fake_open
    monkeypatch.setattr(project.webbrowser, "open", fake_open)

    # Simulate user entering "yes"
    if project.standardize("yes") == "yes":
        project.show_meme()

    assert opened["url"].endswith("yes.html")

def test_no_opens_no_html(monkeypatch):
    opened = {}

    def fake_open(url):
        opened["url"] = url

    # Replace webbrowser.open with fake_open
    monkeypatch.setattr(project.webbrowser, "open", fake_open)

    # Simulate user entering "no"
    if project.standardize("no") == "no":
        project.think_again()

    assert opened["url"].endswith("index.html")