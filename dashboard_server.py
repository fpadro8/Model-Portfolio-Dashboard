from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import os
import sys

HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 8001))

class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith('/api/chart/'):
            self.handle_chart_api(parsed)
        else:
            super().do_GET()

    def handle_chart_api(self, parsed):
        ticker = parsed.path.replace('/api/chart/', '', 1).strip()
        if not ticker or '/' in ticker or '?' in ticker:
            self.send_error(400, 'Invalid ticker')
            return

        query = parsed.query
        remote_url = f'https://query1.finance.yahoo.com/v8/finance/chart/{quote(ticker)}'
        if query:
            remote_url += f'?{query}'

        try:
            req = Request(remote_url, headers={
                'User-Agent': 'Mozilla/5.0 (compatible; dashboard-proxy/1.0)',
                'Accept': 'application/json',
            })
            with urlopen(req, timeout=15) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_header('Content-Type', resp.headers.get('Content-Type', 'application/json'))
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Pragma', 'no-cache')
                self.send_header('Expires', '0')
                self.end_headers()
                self.wfile.write(data)
        except HTTPError as exc:
            self.send_error(exc.code, exc.reason)
        except URLError as exc:
            self.send_error(502, f'Bad gateway: {exc.reason}')
        except Exception as exc:
            self.send_error(500, f'Internal server error: {exc}')

if __name__ == '__main__':
    server_address = (HOST, PORT)
    print(f'Serving dashboard on http://{HOST}:{PORT}/')
    print('Proxying /api/chart/<ticker> to Yahoo Finance.')
    try:
        with HTTPServer(server_address, DashboardHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down.')
        sys.exit(0)
