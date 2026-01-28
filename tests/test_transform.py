"""
Test file for the MAxO annotation transform script.

Uses Koza 2.x testing patterns with KozaRunner and PassthroughWriter.

See the Koza documentation for more information on testing transforms:
https://koza.monarchinitiative.org/Usage/testing/
"""

import pytest
from koza.io.writer.passthrough_writer import PassthroughWriter
from koza.runner import KozaRunner, KozaTransformHooks

from transform import transform_record


# Define the ingest name and transform script path
INGEST_NAME = "maxo_annotation"


@pytest.fixture
def row_with_extension_entities():
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
    writer = PassthroughWriter()
    runner = KozaRunner(
        data=iter([row]),
        writer=writer,
        hooks=KozaTransformHooks(transform_record=[transform_record]),
    )
    runner.run()
    return writer.data


def test_row_with_extension(row_with_extension_entities):
    entities = row_with_extension_entities
    assert len(entities) == 1
    association = entities[0]
    assert association.subject == "MAXO:0000434"
    assert association.subject_specialization_qualifier == "CHEBI:51599"
    assert association.predicate == "biolink:ameliorates_condition"
    assert association.original_predicate == "TREATS"
    assert association.object == "HP:0001324"
    assert association.disease_context_qualifier == "MONDO:0014590"
    assert association.category == ["biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation"]
    assert association.primary_knowledge_source == "infores:maxo"
    assert association.aggregator_knowledge_source == ["infores:monarchinitiative"]


@pytest.fixture
def no_hpo_entities():
    row = {
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
    writer = PassthroughWriter()
    runner = KozaRunner(
        data=iter([row]),
        writer=writer,
        hooks=KozaTransformHooks(transform_record=[transform_record]),
    )
    runner.run()
    return writer.data


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
    assert association.primary_knowledge_source == "infores:maxo"
    assert association.aggregator_knowledge_source == ["infores:monarchinitiative"]
