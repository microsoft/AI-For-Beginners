FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#    && apt-get -y install libgl1

# Copy requirements.txt to a temp location for package installation
COPY .devcontainer/requirements.txt /tmp/conda-tmp/
# Install packages using conda and pip directly to avoid hanging on environment solving
RUN umask 0002 \
    && /opt/conda/bin/conda install -y -c conda-forge -c pytorch -c defaults \
        python pip ipykernel ipython ipywidgets jupyter matplotlib=3.9 numpy=1.26 \
        requests=2.32 scikit-learn scipy=1.13 opencv setuptools \
        pytorch torchtext torchvision torchdata \
    && /opt/conda/bin/pip install --no-cache-dir -r /tmp/conda-tmp/requirements.txt \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

