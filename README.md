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
usage: molai predict [-h] --smile SMILE

optional arguments:
  -h, --help     show this help message and exit
  --smile SMILE  molecule smile
```


## Run Flask application

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
