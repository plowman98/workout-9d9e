import tempfile
import webbrowser
from src.load import load_log
from src.plot import build_figures


def main() -> None:
    df = load_log()
    figs = build_figures(df)

    divs = "\n".join(
        fig.to_html(full_html=False, include_plotlyjs=(i == 0))
        for i, fig in enumerate(figs)
    )
    html = f"<html><body>{divs}</body></html>"

    with tempfile.NamedTemporaryFile(
        suffix=".html", delete=False, mode="w", encoding="utf-8"
    ) as f:
        f.write(html)
        path = f.name

    webbrowser.open(f"file://{path}")


if __name__ == "__main__":
    main()
