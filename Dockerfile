FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# uv installation
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

COPY . .

RUN uv sync --frozen

CMD ["uv", "run", "arxgen"]

# Building docker image:
# (sudo) docker build -t arxgen:latest .

# Running docker image (-it : -i for interactive and -t to simulate a real terminal with colors):
# (sudo) docker run -it --network="host" --env-file .env arxgen:latest