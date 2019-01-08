<h1 align="center">
  <br>
  NeuroMMSig Knowledge
  <a href="https://zenodo.org/badge/latestdoi/164427425"><img src="https://zenodo.org/badge/164427425.svg" alt="DOI"></a>
  <br>
</h1>

<p align="center">
This repository contains knowledge curated in Biological Expression Language (BEL)
for NeuroMMSig during the <a href="https://aetionomy.eu">AETIONOMY</a> project.
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

## Installation

``neurommsig_knowledge`` can be installed from [PyPI](https://pypi.org/project/neurommsig-knowledge/) with the following command:

```bash
$ pip install neurommsig_knowledge
```

The latest version can be installed from [GitHub](https://github.com/neurommsig/neurommsig-knowledge) with:

```bash
$ pip install git+https://github.com/neurommsig/neurommsig-knowledge.git
```

## Usage

The graph can be loaded with:

```python
from neurommsig_knowledge import repository
from pybel import union

# Get all graphs
graphs = repository.get_graphs()

# Combine them all using pybel.union
graph = union(graphs.values())
```

## License

- BEL scripts in this repository are licensed under the CC BY 4.0 license.
- Python source code in this repository is licensed under the MIT license.
