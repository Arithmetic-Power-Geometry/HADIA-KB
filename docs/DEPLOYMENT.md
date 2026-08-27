# Deployment

## Streamlit Community Cloud
1. Upload the repository to GitHub.
2. In Streamlit Community Cloud choose **Create app**.
3. Select the repository and branch.
4. Set the entrypoint to `streamlit_app.py`.
5. Deploy.

No secrets or database credentials are required for the public app because it reads the frozen release files packaged in the repository.

## Optional API
Install `requirements-api.txt` and run:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

## Optional PostgreSQL
Use `database/schema.sql` and import the CSV release. PostgreSQL is not required for Streamlit deployment.
