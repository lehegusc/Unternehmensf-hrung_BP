"""
BP Analyse Docs Server
Serves the bp-analyse/ folder as a documentation website.
Paths are derived from the script's own location so it works on any machine.
"""

import http.server
import json
import os
import socketserver
import urllib.parse

# Derive paths from this script's location
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = _SCRIPT_DIR
CONTENT_DIR = os.path.dirname(_SCRIPT_DIR)   # parent of _docs-site = bp-analyse/
PORT = 8000

IGNORE = {".DS_Store", "_docs-site", ".git", "__pycache__", "start-docs.command", "start-docs.bat", ".gitignore", "README.md"}


def build_tree(root_dir):
    """Recursively scan directory, return nested tree of folders and .md files."""
    tree = []
    try:
        entries = sorted(os.listdir(root_dir))
    except PermissionError:
        return tree
    dirs = []
    files = []
    for entry in entries:
        if entry.startswith(".") or entry.startswith("_") or entry in IGNORE:
            continue
        full_path = os.path.join(root_dir, entry)
        rel_path = os.path.relpath(full_path, CONTENT_DIR).replace(os.sep, "/")
        if os.path.isdir(full_path):
            children = build_tree(full_path)
            dirs.append({"name": entry, "path": rel_path, "type": "folder", "children": children})
        elif entry.lower().endswith(".md"):
            files.append({"name": entry, "path": rel_path, "type": "file"})
    return dirs + files


def read_md_file(rel_path):
    """Read a markdown file by its path relative to CONTENT_DIR."""
    # Convert URL forward slashes to OS path separators (for Windows)
    rel_path = rel_path.replace("/", os.sep)
    safe_path = os.path.normpath(os.path.join(CONTENT_DIR, rel_path))
    if not safe_path.startswith(os.path.normpath(CONTENT_DIR)):
        return None
    if not os.path.isfile(safe_path):
        return None
    with open(safe_path, "r", encoding="utf-8") as f:
        return f.read()


class DocsHandler(http.server.BaseHTTPRequestHandler):
    """Handles requests for the docs site."""

    def log_message(self, fmt, *args):
        print(f"  {args[0]}")

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/" or path == "/index.html":
            self._serve_file(os.path.join(SITE_DIR, "index.html"), "text/html")

        elif path == "/api/tree":
            self._serve_json(build_tree(CONTENT_DIR))

        elif path.startswith("/api/content/"):
            rel_path = urllib.parse.unquote(path[len("/api/content/"):])
            content = read_md_file(rel_path)
            if content is not None:
                self._serve_text(content)
            else:
                self._serve_error(404, "File not found")

        else:
            self._serve_error(404, "Not found")

    def _serve_file(self, filepath, content_type):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = f.read().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            self._serve_error(404, "File not found")

    def _serve_json(self, obj):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _serve_text(self, text):
        data = text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _serve_error(self, code, message):
        data = json.dumps({"error": message}).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def run():
    print()
    print("  BP Analyse Docs")
    print(f"  Running at:  http://localhost:{PORT}")
    print("  Stop with:   Ctrl+C")
    print()
    print(f"  Content dir: {CONTENT_DIR}")
    print()

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), DocsHandler) as srv:
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped.")


if __name__ == "__main__":
    run()
      except KeyboardInterrupt:
            print("\n  Server stopped.")


if __name__ == "__main__":
    run()
