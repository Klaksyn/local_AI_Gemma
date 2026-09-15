def read_multiline() -> str:
    msg = []
    while True:
        usr = input("> ")

        if (usr == "done" or usr == "exit"
                or usr == "!" or usr == "end"):
            return "\n".join(msg)

        msg.append(usr)