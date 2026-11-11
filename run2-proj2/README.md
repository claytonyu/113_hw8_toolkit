# Idea Garden — sample Project 2

## AI-generated starter notes

This is a minimal starting point for a creative web app: collect ideas and notes in an “idea garden.” The frontend is a static preview with sample content; its controls are disabled because it is not connected to the backend. The backend is a separate, working JSON API backed by SQLite. Python 3 is the only dependency. No secrets are used.

Run the backend from this folder:

```sh
python3 backend/server.py
```

It listens on `127.0.0.1:8000` and creates `backend/ideas.db`. You can set `PORT` or `IDEA_DB` to change the port or database path. Try it in another terminal:

```sh
curl -X POST http://127.0.0.1:8000/ideas -H 'Content-Type: application/json' -d '{"title":"A tiny library","note":"Share books nearby"}'
curl http://127.0.0.1:8000/ideas
curl -X DELETE http://127.0.0.1:8000/ideas/1
```

Open `frontend/index.html` in a browser to see the preview. To continue, connect the form and list to the API, handle loading and errors, and decide how to serve them together. The server currently binds to localhost and has no authentication; it is intended for local development, not public deployment.

This is a starter, not a completed assignment. Project 2 also requires your own README, an honest prompt log, personal code contributions, deployment, a portfolio link, and other course deliverables. Review the course specification and document your actual process. Codex generated this starter.
