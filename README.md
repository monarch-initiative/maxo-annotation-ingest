# MAxO Annotations

[MAxO](https://github.com/monarch-initiative/MAxO) (Medical Action Ontology) provides a structured vocabulary of medical actions including treatments, interventions, and diagnostic procedures. [MAxO Annotations](https://github.com/monarch-initiative/maxo-annotations) are curated annotations linking these medical actions to diseases and phenotypes.

Data is downloaded from: `https://raw.githubusercontent.com/monarch-initiative/maxo-annotations/master/annotations/maxo-annotations.tsv`

## Treatment Associations

Each annotation row links a medical action (MAxO term) to a phenotype (HPO term), with an optional disease context and optional extension term that further specifies the action. The `maxo_relation` field determines the predicate:

| maxo_relation | Predicate |
|---|---|
| TREATS | `biolink:ameliorates_condition` |
| PREVENTS | `biolink:preventative_for_condition` |
| CONTRAINDICATED | `biolink:contraindicated_in` |
| INVESTIGATES | `biolink:related_to` |
| LACK OF OBSERVED RESPONSE | `biolink:related_to` |
| UNKNOWN | `biolink:related_to` |

**Biolink Captured:**

- `biolink:ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation`
    - id (UUID)
    - subject (MAxO term ID)
    - subject_specialization_qualifier (extension ID, when present)
    - predicate (mapped from maxo_relation, see above)
    - original_predicate (raw maxo_relation value)
    - object (HPO term ID)
    - disease_context_qualifier (disease ID, when present)
    - publications (citation)
    - primary_knowledge_source (`infores:maxo`)
    - aggregator_knowledge_source (`["infores:monarchinitiative"]`)
    - knowledge_level (`knowledge_assertion`)
    - agent_type (`manual_agent`)

## Citation

Carmody LC, Gargano MA, Toro S, Vasilevsky NA, Adam MP, Blau H, Chan LE, Gomez-Andres D, Horvath R, Kraus ML, Ladewig MS, Lewis-Smith D, Lochmuller H, Matentzoglu NA, Munoz-Torres MC, Schuetz C, Seitz B, Similuk MN, Sparks TN, Strauss T, Swietlik EM, Thompson R, Zhang XA, Mungall CJ, Haendel MA, Robinson PN. The Medical Action Ontology: A tool for annotating and analyzing treatments and clinical management of human disease. Med. 2023;4(12):913-927.e3. doi: 10.1016/j.medj.2023.10.003. PMID: 37963467

## License

BSD-3-Clause
