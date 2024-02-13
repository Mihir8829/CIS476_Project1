class GUIComponent:
    def display(self):
        pass

class Panel(GUIComponent):
    def display(self, generation):
        return f"Panel {generation}"

class Button(GUIComponent):
    def display(self, generation):
        return f"Button {generation}"

class Textbox(GUIComponent):
    def display(self, generation):
        return f"Textbox {generation}"

class GUIFactory:
    def create_panel(self):
        pass

    def create_button(self):
        pass

    def create_textbox(self):
        pass


class Word90Factory(GUIFactory):
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()


class Word00Factory(GUIFactory):
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()


class Word10Factory(GUIFactory):
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()


class Word24Factory(GUIFactory):
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()

class WordTest:
    def __init__(self, config_file):
        self.config_file = config_file

    def run_tests(self):
        generations = []
        factory_counts = {}
        with open(self.config_file, 'r') as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                generation = line
                generations.append(generation)
                if generation == "Word90":
                    factory = Word90Factory()
                elif generation == "Word00":
                    factory = Word00Factory()
                elif generation == "Word10":
                    factory = Word10Factory()
                elif generation == "Word24":
                    factory = Word24Factory()
                else:
                    print(f"No factory defined for {generation}")
                    continue

                factory_counts[generation] = factory_counts.get(generation, 0) + 1

                if factory_counts[generation] >= 3:
                    print(f"Warning: {generation} tested more than twice!")
                else:
                    panel = factory.create_panel()
                    button = factory.create_button()
                    textbox = factory.create_textbox()
                    print(f"{panel.display(generation)} {button.display(generation)} {textbox.display(generation)}")
               

if __name__ == "__main__":
    test = WordTest("config_file.txt")
    test.run_tests()