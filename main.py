class GUIComponent:
    def display(self):
        pass

class Panel(GUIComponent): #Class for panel and displaying with the generation of MS being Called
    def display(self, generation):
        return f"Panel {generation}"

class Button(GUIComponent): #Class for Button and displaying with the generation of MS being Called
    def display(self, generation):
        return f"Button {generation}"

class Textbox(GUIComponent): #Class for Textbox and displaying with the generation of MS being Called
    def display(self, generation):
        return f"Textbox {generation}"

class GUIFactory: #Singleton pattern implemented here
    Instance = None  
    def get_instance():
        if GUIFactory.Instance is None:
            GUIFactory.Instance = GUIFactory()
        return GUIFactory.Instance
    #Constructors
    def create_panel(self):
        pass

    def create_button(self):
        pass

    def create_textbox(self):
        pass


class Word90Factory(GUIFactory): #Factroy classes and their methods for MS 90
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()


class Word00Factory(GUIFactory): #Factroy classes and their methods for MS 00
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()


class Word10Factory(GUIFactory): #Factroy classes and their methods for MS 10
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()


class Word24Factory(GUIFactory): #Factroy classes and their methods for MS 24
    def create_panel(self):
        return Panel()

    def create_button(self):
        return Button()

    def create_textbox(self):
        return Textbox()

class WordTest: #Client side logic
    def __init__(self, config_file):
        self.config_file = config_file

    def run_tests(self):
        generations = []
        factory_counts = {} #Counter for numnber of times factory is being called
        with open(self.config_file, 'r') as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break

                generation = line
                generations.append(generation)
                factory = None

                if generation == "Word90":
                    factory = Word90Factory()
                elif generation == "Word00":
                    factory = Word00Factory()
                elif generation == "Word10":
                    factory = Word10Factory()
                elif generation == "Word24":
                    factory = Word24Factory()
                else:
                    print(f"Factory does not exist for {generation}")
                    continue

                factory_counts[generation] = factory_counts.get(generation, 0) + 1 

                if factory_counts[generation] >= 3:  #Gives warning if a factory is called more than 2 times
                    print(f"Warning: {generation} tested more than twice!")
                else: #Instantiation of methods and printing them using display method
                    panel = factory.create_panel()
                    button = factory.create_button()
                    textbox = factory.create_textbox()
                    print(f"{panel.display(generation)} {button.display(generation)} {textbox.display(generation)}")
               

if __name__ == "__main__":
    test = WordTest("config_file.txt")
    test.run_tests()