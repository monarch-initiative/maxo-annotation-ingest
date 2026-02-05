import uuid  # For generating UUIDs for associations

import koza
from biolink_model.datamodel.pydanticmodel_v2 import (
    AgentTypeEnum,
    ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation,
    KnowledgeLevelEnum,
)

predicate_mapping = {
    "TREATS": "biolink:ameliorates_condition",
    "PREVENTS": "biolink:preventative_for_condition",
    "CONTRAINDICATED": "biolink:contraindicated_in",
    "UNKNOWN": "biolink:related_to",
    "INVESTIGATES": "biolink:related_to",  # TODO: this is too general, but biolink:diagnoses doesn't feel right
    "LACK OF OBSERVED RESPONSE": "biolink:related_to",  # TODO: this is also too general,
    # but negation + biolink:ameliorates_condition feels too strong
}


@koza.transform_record()
def transform_record(koza_transform, row):
    # Code to transform each row of data
    # For more information, see https://koza.monarchinitiative.org/Ingests/transform

    try:
        predicate = predicate_mapping.get(row["maxo_relation"].upper())

    except KeyError:
        raise ValueError(f"Not sure how to map maxo_relation {row['maxo_relation']} to a biolink predicate")

    association = ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(
        id=str(uuid.uuid4()),
        subject=row["maxo_id"],
        subject_specialization_qualifier=row.get("extension_id") if row.get("extension_id") else None,
        predicate=predicate,
        original_predicate=row["maxo_relation"],
        object=row["hpo_id"],
        disease_context_qualifier=row.get("disease_id"),
        primary_knowledge_source="infores:maxo",
        aggregator_knowledge_source=["infores:monarchinitiative"],
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_agent,
        publications=[row["citation"]],
    )

    return [association]
