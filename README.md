# molai

Molecule AI.


## Installation

- Install Miniconda
  ```shell
  wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
  bash ~/miniconda.sh -b -p ~/miniconda
  export PATH=~/miniconda/bin:$PATH
  ```

- Update conda
  ```shell
  conda update -n base conda
  ```

- Create the conda environment
  ```shell
  conda env create -f environment.yml
  ```

- Activate the conda environment
  ```shell
  conda activate molai
  ```


## Setup

Place your input data files in the `data` directory.


## Command Line Interface

Use command line interface `molai`:
```shell
molai -h
usage: molai [-h] {train,evaluate,predict} ...

positional arguments:
  {train,evaluate,predict}
                        command to be executed
    train               train a model
    evaluate            evaluate a model
    predict             use a model to predict the property 'P1' for a given
                        smile

optional arguments:
  -h, --help            show this help message and exit

```

Train model: `molai train`
```shell
molai train -h
usage: molai train [-h] [--model MODEL]

optional arguments:
  -h, --help     show this help message and exit
  --model MODEL  model ID
```

Evaluate model: `molai evaluate`
```shell
molai evaluate -h
usage: molai evaluate [-h] [--model MODEL]

optional arguments:
  -h, --help     show this help message and exit
  --model MODEL  model ID
```

Make a prediction: `molai predict`
```shell
molai predict -h
usage: molai predict [-h] --smile SMILE [--model MODEL]

optional arguments:
  -h, --help     show this help message and exit
  --smile SMILE  molecule smile
  --model MODEL  model ID
```


## Flask API

###  Run Flask API

In production:
```shell
export FLASK_APP=app.py
flask run --host=0.0.0.0
```
- By default, the production environment is set: `FLASK_ENV=production`

In development:
```shell
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```

### Use Flask API
Use the endpoint `/predict` with the arguments:
- `smile`: smile to be used for prediction
- `model`: model ID

Example:
```
/predict?smile=Cc1cccc(N2CCN(C(=O)C34CC5CC(CC(C5)C3)C4)CC2)c1C&model=1
```


## Docker

Build the Docker container image from the project root directory:
```shell
docker build -t molai .
```

Run the Docker container:
```shell
docker run -dp 5000:5000 -v $PWD/data:/app/data -v $PWD/models:/app/models molai
```

Visit the Flask API at the URL:
http://0.0.0.0:5000/predict?smile=Cc1cccc(N2CCN(C(=O)C34CC5CC(CC(C5)C3)C4)CC2)c1C&model=2


# Models

Two preliminary models have been implemented: model-1 and model-2.

Their respective performance metrics are:
- model-1:
  ```json
  {"loss": 0.8287116885185242, "precision": 0.605042040348053, "recall": 0.7200000286102295, "auc": 0.6242777705192566}
  ```
- model-2:
  ```json
  {"loss": 0.6632762551307678, "precision": 0.6470588445663452, "recall": 0.6600000262260437, "auc": 0.6526111364364624}
  ```
