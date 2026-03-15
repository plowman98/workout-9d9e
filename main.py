from src.load import load_log
from src.plot import build_figures


def main() -> None:
    df = load_log()
    for fig in build_figures(df):
        fig.show()


if __name__ == "__main__":
    main()
