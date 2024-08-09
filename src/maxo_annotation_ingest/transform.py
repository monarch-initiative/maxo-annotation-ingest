import uuid  # For generating UUIDs for associations

from biolink_model.datamodel.pydanticmodel_v2 import *  # Replace * with any necessary data classes from the Biolink Model
from koza.cli_utils import get_koza_app

koza_app = get_koza_app("maxo_annotation")

predicate_mapping = {
    "TREATS:": "biolink:ameliorates_condition",
    "PREVENTS:": "biolink:preventative_for_condition",
    "CONTRAINDICATED":  "biolink:contraindicated_in",
}


while (row := koza_app.get_row()) is not None:
    # Code to transform each row of data
    # For more information, see https://koza.monarchinitiative.org/Ingests/transform

    print(row)

    # association = Association(
    #     id=str(uuid.uuid1()),
    #     subject=row["example_column_1"],
    #     predicate=row["example_column_3"],
    #     object=row["example_column_2"],
    #     subject_category="SUBJ",
    #     object_category="OBJ",
    #     category=["biolink:Association"],
    #     knowledge_level="not_provided",
    #     agent_type="not_provided",
    # )
    # koza_app.write(association)
