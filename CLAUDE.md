# maxo-annotation-ingest

This is a Koza ingest repository for transforming MAxO annotation data into Biolink model format.

## Project Structure

- `download.yaml` - Configuration for downloading MAxO annotation data
- `src/` - Transform code and configuration
  - `transform.py` / `transform.yaml` - Main transform for MAxO annotations
- `tests/` - Unit tests for transforms
- `output/` - Generated nodes and edges (gitignored)
- `data/` - Downloaded source data (gitignored)

## Key Commands

- `just run` - Full pipeline (download -> transform)
- `just download` - Download MAxO annotation data
- `just transform-all` - Run all transforms
- `just test` - Run tests

## Data Source

MAxO (Medical Action Ontology) annotations linking medical actions to diseases and phenotypes.
