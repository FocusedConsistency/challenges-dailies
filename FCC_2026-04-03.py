def get_browser_history(commands):
    index = -1
    history = []
    for comm in commands:
        if comm == "Back":
            if index != 0:
                index -= 1
        elif comm == "Forward":
            if index != len(history) - 1:
                index += 1
        else:
            index += 1
            if index < len(history):
                history[index] = comm
            else:
                history.append(comm)

    return [history, index]

get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"])
# [["example.com", "example.com/about", "example.com/contact", "freecodecamp.org"], 3]
