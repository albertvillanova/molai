FROM continuumio/miniconda3

WORKDIR /app

# Create the conda environment
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the conda environment
SHELL ["conda", "run", "-n", "molai", "/bin/bash", "-c"]

# Install molai
COPY setup.py .
COPY molai molai
RUN pip install .

# Run Flask API at start
COPY app.py .
ENV FLASK_APP=app.py
EXPOSE 5000
#ENTRYPOINT ["conda", "run", "-n", "molai", "flask", "run", "--host", "0.0.0.0"]
ENTRYPOINT exec flask run --host 0.0.0.0
