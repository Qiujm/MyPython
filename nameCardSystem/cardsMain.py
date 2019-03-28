import interface, functions


def run():
    inter = interface.Interface()
    while True:
        action = inter.get_action()
        if action == "1":
            functions.new_cards()

        elif action == "2":
            functions.show_all_cards()

        elif action == "3":
            functions.query_cards()

        elif action == "0":
            functions.quit_system()


run()
