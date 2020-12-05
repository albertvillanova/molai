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
  conda create -y --name molai python=3.6
  ```

- Activate the conda environment
  ```shell
  conda activate molai
  ```

- Install dependencies
  ```shell
  conda install -c conda-forge rdkit
  ```
