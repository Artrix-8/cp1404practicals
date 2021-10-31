import wikipedia

title = input("Page title: ")
while title:
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f"\"{title}\" does not match any pages. Try another query!")
    title = input("Page title: ")
