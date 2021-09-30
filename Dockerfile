FROM python:3.9

ARG NB_USER
ARG NB_UID

ENV USER "${NB_USER:-binder}"
ENV HOME "/home/${USER}"
ENV PATH "${HOME}/.local/bin:${PATH}"

# Install Apt packages.
#
# Flags:
#     -m: Ignore missing packages and handle result.
#     -q: Produce log suitable output by omitting progress indicators.
#     -y: Assume "yes" as answer to all prompts and run non-interactively.
RUN apt-get update -m && apt-get install -qy \
    build-essential \
    libsndfile1 \
    llvm-9 \
    llvm-9-dev \
    texlive

# Create non-priviledged user.
#
# Flags:
#     -l: Do not add user to lastlog database.
#     -m: Create user home directory if it does not exist.
#     -s /usr/bin/fish: Set user login shell to Fish.
#     -u 1000: Give new user UID value 1000.
# RUN useradd -lm -s /bin/bash -u 1000 "${USER}"

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid "${NB_UID:-1000}" \
    "${USER}"

USER "${USER}"
WORKDIR "${HOME}"

# Set Bash as default shell.
SHELL ["/bin/bash", "-c"]

RUN mkdir build

COPY ./README.md build/
COPY ./pyproject.toml build/
COPY ./src build/

RUN pip install --use-feature=in-tree-build ./build/

COPY --chown="${USER}" ./notebooks ./notebooks

WORKDIR "${HOME}/notebooks"

RUN for notebook in *.md; do \
    jupytext --execute --to ipynb "${notebook}"; \
    jupyter trust "${notebook/.md/.ipynb}"; \
    rm "${notebook}"; \
  done
