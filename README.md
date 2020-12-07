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
usage: molai train [-h]

optional arguments:
  -h, --help  show this help message and exit
```

Evaluate model: `molai evaluate`
```shell
molai evaluate -h
usage: molai evaluate [-h]

optional arguments:
  -h, --help  show this help message and exit
```

Make a prediction: `molai predict`
```shell
molai predict -h
usage: molai predict [-h] --smile SMILE

optional arguments:
  -h, --help     show this help message and exit
  --smile SMILE  molecule smile
```
