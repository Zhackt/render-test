"""Tes deploy Render — backend gratis tanpa kartu (Bangzhackt).

Server kecil pakai Python standar saja (tanpa library luar).
Jalan di PORT dari environment Render (default 10000).
"""
import http.server
import os


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            "<h1>Halo dari Render!</h1>"
            "<p>Tes deploy Bangzhackt — backend gratis tanpa kartu.</p>"
            "<p>Kalau halaman ini kebuka, berarti GitHub ke Render jalan.</p>"
        )
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    http.server.HTTPServer(("0.0.0.0", port), Handler).serve_forever()
