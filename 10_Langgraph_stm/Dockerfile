FROM postgres:16

# Default credentials/database for local LangGraph checkpoint demos.
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres

EXPOSE 5432

# Postgres stores database files here inside the container.
VOLUME ["/var/lib/postgresql/data"]
