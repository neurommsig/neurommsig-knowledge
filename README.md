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
  <a href="#citation">Citation<a>  •
  <a href="#license">License</a>  •
  <a href="#acknowledgements">Acknowledgements</a>
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

## Citation

If you find NeuroMMSig useful in your work, consider citing:

- Domingo-Fernández, D., *et al* (2017). [Multimodal mechanistic signatures for neurodegenerative
  diseases (NeuroMMSig): A web server for mechanism enrichment](https://doi.org/10.1093/bioinformatics/btx399).  Bioinformatics, 33(22), 3679–3681.

- Hoyt, C. T., *et al* (2019). [Re-curation and Rational Enrichment of Knowledge Graphs in
  Biological Expression Language](https://doi.org/10.1101/536409>). *bioRxiv*, 536409.

## License

- BEL scripts in this repository are licensed under the CC BY 4.0 license.
- Python source code in this repository is licensed under the MIT license.

## Acknowledgements

This work was supported by the European Union/European Federation of Pharmaceutical Industries and 
Associations (EFPIA) Innovative Medicines Initiative Joint Undertaking under AETIONOMY [grant number 115568], 
resources of which are composed of financial contribution from the European Union’s Seventh Framework 
Programme (FP7/2007-2013) and EFPIA companies in kind contribution.
