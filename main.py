import subprocess
import tempfile
import webbrowser
from src.load import load_log
from src.plot import build_figures


def _open_browser(path: str) -> None:
    try:
        with open("/proc/version") as f:
            is_wsl = "microsoft" in f.read().lower()
    except OSError:
        is_wsl = False

    if is_wsl:
        win_path = subprocess.check_output(["wslpath", "-w", path]).decode().strip()
        subprocess.run(["explorer.exe", win_path])
    else:
        webbrowser.open(f"file://{path}")


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

    _open_browser(path)


if __name__ == "__main__":
    main()
