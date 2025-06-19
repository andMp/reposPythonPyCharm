from views.bibl_view import bibl_view
from models.Kniga import Kniga
from models.Koristuvac import Koristuvac
from controllers.controller import Biblioteka_controller

def main():
    view = bibl_view()
    controller = Biblioteka_controller(view)
    controller.run()

# if __name__ == '__main__':
#     main()
