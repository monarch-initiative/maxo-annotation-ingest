import uuid  # For generating UUIDs for associations

from biolink_model.datamodel.pydanticmodel_v2 import (
    AgentTypeEnum,
    ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation,
    KnowledgeLevelEnum,
)
from koza.cli_utils import get_koza_app

koza_app = get_koza_app("maxo_annotation")

predicate_mapping = {
    "TREATS": "biolink:ameliorates_condition",
    "PREVENTS": "biolink:preventative_for_condition",
    "CONTRAINDICATED": "biolink:contraindicated_in",
}


while (row := koza_app.get_row()) is not None:
    # Code to transform each row of data
    # For more information, see https://koza.monarchinitiative.org/Ingests/transform

    try:
        predicate = predicate_mapping.get(row["maxo_relation"])
    except KeyError:
        raise ValueError(f"Not sure how to map maxo_relation {row['maxo_relation']} to a biolink predicate")

    disease_context_qualifier = row.get("disease_id") if row.get("disease_id") != row.get("hpo_id") else None

    association = ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation(
        id=str(uuid.uuid4()),
        subject=row["maxo_id"],
        subject_specialization_qualifier=row.get("extension_id"),
        predicate=predicate,
        object=row["hpo_id"],
        disease_context_qualifier=row.get("disease_id"),
        primary_knowledge_source="infores:maxo",
        aggregator_knowledge_source="infores:monarchinitiative",
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_agent,
        publications=[row["citation"]],
    )

    koza_app.write(association)
