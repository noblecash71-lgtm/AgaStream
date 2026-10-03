from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent / "dist"

class SpaHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = urlsplit(self.path).path
        candidate = ROOT / path.lstrip("/")
        if path != "/" and not candidate.is_file():
            self.path = "/index.html"
        super().do_GET()

    def do_HEAD(self):
        path = urlsplit(self.path).path
        candidate = ROOT / path.lstrip("/")
        if path != "/" and not candidate.is_file():
            self.path = "/index.html"
        super().do_HEAD()

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 3000), SpaHandler).serve_forever()
