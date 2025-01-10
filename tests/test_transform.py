"""
An example test file for the transform script.

It uses pytest fixtures to define the input data and the mock koza transform.
The test_example function then tests the output of the transform script.

See the Koza documentation for more information on testing transforms:
https://koza.monarchinitiative.org/Usage/testing/
"""

import pytest
from koza.utils.testing_utils import mock_koza

# Define the ingest name and transform script path
INGEST_NAME = "maxo_annotation"
TRANSFORM_SCRIPT = "./src/maxo_annotation_ingest/transform.py"


@pytest.fixture
def row_with_extension_entities(mock_koza):
    row = {
        "disease_id": "MONDO:0014590",
        "disease_name": "Myasthenic Syndrome, Congenital, 18",
        "citation": "PMID:25381298",
        "maxo_id": "MAXO:0000434",
        "maxo_label": "calcium channel blocking agent therapy",
        "hpo_id": "HP:0001324",
        "maxo_relation": "TREATS",
        "evidence_code": "TAS",
        "extension_id": "CHEBI:51599",
        "extension_label": "2,4-diaminopyridine",
        "creator": "ORCID:0000-0002-0736-9199",
        "last_update": "2022-09-27",
        "created_on": "2022-09-27",
    }
    return mock_koza(
        INGEST_NAME,
        [row],
        TRANSFORM_SCRIPT,
    )


def test_row_with_extension(row_with_extension_entities):
    entities = row_with_extension_entities
    assert len(entities) == 1
    association = entities[0]
    assert association.subject == "MAXO:0000434"
    assert association.subject_specialization_qualifier == "CHEBI:51599"
    assert association.predicate == "biolink:ameliorates_condition"
    assert association.object == "HP:0001324"
    assert association.disease_context_qualifier == "MONDO:0014590"
    assert association.category == ["biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"]


# Define an example row to test (as a dictionary)
@pytest.fixture
def no_hpo_row():
    return {
        "disease_id": "MONDO:0009797",
        "disease_name": "Orotic Aciduria",
        "citation": "PMID:9042911",
        "maxo_id": "MAXO:0010022",
        "maxo_label": "uridine supplementation",
        "hpo_id": "MONDO:0009797",
        "maxo_relation": "TREATS",
        "evidence_code": "TAS",
        "extension_id": "",
        "extension_label": "",
        "attribute": "",
        "creator": "ORCID:0000-0002-0736-9199",
        "last_update": "2022-09-06",
        "created_on": "2022-09-06",
    }


# Define the mock koza transform
@pytest.fixture
def no_hpo_entities(mock_koza, no_hpo_row):
    # Returns [entity_a, entity_b, association] for a single row
    return mock_koza(
        INGEST_NAME,
        no_hpo_row,
        TRANSFORM_SCRIPT,
    )


def test_no_hpo(no_hpo_entities):
    entities = no_hpo_entities
    assert len(entities) == 1
    association = entities[0]
    assert association.subject == "MAXO:0010022"
    assert association.predicate == "biolink:ameliorates_condition"
    assert association.object == "MONDO:0009797"
    assert association.publications == ["PMID:9042911"]
    # this can't be captured yet
    # assert association.creator == "ORCID:0000-0002-0736-9199"
    assert association.category == ["biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"]
