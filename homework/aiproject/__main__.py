"""
Run
Initial a application, fall into the mainloop
"""
from views import Application


def main():
    app = Application(width=5, height=4)
    app.mainloop()

if __name__ == '__main__':
    main()
