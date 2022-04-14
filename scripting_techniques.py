from colr import color
import fire


class Log:

    def warning(self, string):
        print(color(string, fore='green', style='bright'))

    def error(self, string):
        print(color(string, fore='green', style='bright'))


if __name__ == '__main__':
    fire.Fire(Log)