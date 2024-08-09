# maxo-annotation-ingest Report

{{ get_nodes_report() }}

{{ get_edges_report() }}

The MAxO Annotation Ingest converts MAxO Annotation data to Biolink Model compliant KGX format. 

Example annotation records: 

|  disease_id   |                   disease_name                    |   citation    |   maxo_id    |               maxo_label               |   hpo_id   | maxo_relation | evidence_code | extension_id |   extension_label   | attribute |          creator          | last_update | created_on |
|---------------|---------------------------------------------------|---------------|--------------|----------------------------------------|------------|---------------|---------------|--------------|---------------------|-----------|---------------------------|-------------|------------|
| MONDO:0014590 | Myasthenic Syndrome, Congenital, 18               | PMID:25381298 | MAXO:0000434 | calcium channel blocking agent therapy | HP:0001324 | TREATS        | TAS           | CHEBI:51599  | 2,4-diaminopyridine |           | ORCID:0000-0002-0736-9199 | 2022-09-27  | 2022-09-27 |
| MONDO:0014584 | Myasthenic Syndrome, Congenital, 3b, Fast-channel | PMID:11435464 | MAXO:0000210 | cholinesteriase inhibitor therapy      | HP:0001324 | TREATS        | TAS           | CHEBI:8665   | Pyridostigmine      |           | ORCID:0000-0002-0736-9199 | 2023-02-26  | 2023-02-26 |
| MONDO:0010421 | Agammaglobulinemia, X-linked                      | PMID:26909497 | MAXO:0001480 | immunoglobulin infusion therapy        | HP:0004432 | TREATS        | PCS           |              |                     |           | ORCID:0000-0001-9969-9517 | 2023-06-10  | 2023-03-15 |
| MONDO:0010196 | Werner Syndrome                            | PMID:20301687 | MAXO:0001139 | calcium supplementation | HP:0000939 | PREVENTS      | TAS           |              |                 |                       | ORCID:0000-0002-4142-7153 | 2023-02-11  | 2022-02-28 |
| MONDO:0010156 | Spastic Paraplegia 20, Autosomal Recessive | PMID:20301556 | MAXO:0000011 | physical therapy        | HP:0007340 | PREVENTS      | TAS           |              |                 |                       | ORCID:0000-0002-4142-7153 | 2022-02-28  | 2022-02-28 |
| MONDO:0008667 | Von Hippel-lindau Syndrome                 | PMID:20301636 | MAXO:0000058 | pharmacotherapy         | HP:0009713 | PREVENTS      | TAS           |              |                 | comment: "CHEBI:9513" | ORCID:0000-0002-4142-7153 | 2023-06-14  | 2022-08-01 |
| MONDO:0100079 | Epileptic Encephalopathy, Early Infantile, 6 (dravet Syndrome) | PMID:9596203 | MAXO:0000208 | sodium channel inhibitor therapy | HP:0032794 | CONTRAINDICATED | TAS           | CHEBI:6367   | lamotrigine     | comment: "Seizures can worsen on withdrawing lamotrigine." | ORCID:0000-0002-1735-8178 | 2023-07-12  | 2023-07-12 |

Mapping between MAxO relation and biolink predicate: 

| maxo_relation | biolink_predicate                                                                                         |
|---------------|-----------------------------------------------------------------------------------------------------------|
| TREATS        | [biolink:ameliorates_condition](https://biolink.github.io/biolink-model/ameliorates_condition/)           |
| PREVENTS      | [biolink:prevantative_for_condition](https://biolink.github.io/biolink-model/preventative_for_condition/) |
| CONTRAINDICATED | [biolink:contraindicated_in](https://biolink.github.io/biolink-model/contraindicated_in/)                 |
