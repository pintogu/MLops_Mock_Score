# MLops Mock Score Service

This repository contains a very simple FastAPI application that exposes a mock scoring endpoint.


---

## What this does

* Runs a FastAPI application
* Exposes one endpoint: `/score`
* Always returns `1`

---

## How to run it

From the repository root:

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

After running it, the service will be available at:

```
http://127.0.0.1:8000/score
```

