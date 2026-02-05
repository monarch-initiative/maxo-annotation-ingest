# maxo-annotation-ingest

Koza ingest for MAxO (Medical Action Ontology) annotations, transforming treatment-disease-phenotype relationships into Biolink model format.

## Data Source

[MAxO Annotations](https://github.com/monarch-initiative/maxo-annotations) provides curated annotations linking medical actions (treatments, interventions) to diseases and phenotypes.

Data is downloaded from: `https://raw.githubusercontent.com/monarch-initiative/maxo-annotations/master/annotations/maxo-annotations.tsv`

## Output

This ingest produces:
- **Treatment-disease associations** - Links medical actions to diseases they treat, prevent, or are contraindicated for
- **Treatment-phenotype associations** - Links medical actions to phenotypes they address

## Usage

```bash
# Install dependencies
just install

# Run full pipeline
just run

# Or run steps individually
just download      # Download MAxO annotations
just transform-all # Run Koza transform
just test          # Run tests
```

## Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- [just](https://github.com/casey/just) command runner

## License

BSD-3-Clause
