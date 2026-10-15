# Access Requests API

A beginner-friendly Flask API for managing application access requests. This project builds on a small Python exercise with lists, dictionaries, functions, and request status changes.

## Current features

- `GET /requests` — returns all access requests as JSON.
- `POST /requests` — accepts a JSON object containing `user` and `application`, validates the values, and creates a request with the `pending` status.
- `PATCH /requests/<user_name>` — changes a matching pending request to `approved` or `rejected`.
- Invalid request data returns an error response with an appropriate HTTP status code.

Example request body for `POST /requests`:

```json
{
  "user": "Vasile",
  "application": "Zoom"
}
```

Example request body for `PATCH /requests/Jon`:

```json
{
  "status": "approved"
}
```

## Run locally

1. Install Flask:

   ```bash
   python -m pip install flask
   ```

2. Start the application:

   ```bash
   python main.py
   ```

3. Open `http://127.0.0.1:5000/requests` for the list endpoint.

Use a REST client such as Postman to send `POST` and `PATCH` requests. For JSON request bodies, select **Body → raw → JSON**.

## Current limitations

- Requests are stored in a Python list in memory. They are lost when the server stops or restarts.
- The current model identifies a request by user name, so it does not yet handle multiple requests from the same user reliably.
- There is no database, authentication, or authorization yet.

## Next steps

- Add automated tests for the API and its validation rules.
- Improve request identification and duplicate handling.
- Persist requests in PostgreSQL.
- Add authentication and authorization.

This is a learning project and is not intended for production use.
