# Scientific Models

This category tracks individual AI for Science models that may need OpenSciFlow plugin manifests, workflow templates, model-weight metadata, citation propagation, hardware requirements, and limitation notes.

These entries are related projects only. OpenSciFlow does not claim partnership with listed model authors or maintainers.

## Biomolecular structure and protein models

| Project | Type | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|
| Google DeepMind AlphaFold | Biomolecular structure prediction platform | Landmark reference for structure-prediction workflows | Low |
| OpenFold | Open AlphaFold2-style implementation | Structure-prediction manifest reference | Medium |
| OmegaFold | Protein structure prediction model | Historical/alternative structure-model metadata reference | Low |
| Uni-Fold | Protein structure prediction platform | Structure-prediction metadata reference | Medium |
| ColabFold | Protein structure workflow | Structure prediction workflow/plugin reference | Medium |
| ESM / ESMFold | Protein language model and structure model | Protein model metadata reference; repository is archived but historically important | Low |
| Boltz | Biomolecular interaction structure model | Strong model-focused manifest candidate | Medium |
| Chai-1 | Biomolecular structure prediction model | Useful comparison target for model-weight and citation metadata | Medium |
| Protenix | Biomolecular structure prediction model | AlphaFold3-style workflow metadata reference | Medium |
| RoseTTAFold-All-Atom | All-atom biomolecular modeling model | Complex input/output and license metadata reference | Medium |
| RFdiffusion | Protein backbone generation/design model | Future protein-design workflow and safety-boundary reference | Medium |
| ProteinMPNN | Protein sequence design model | Compact future sequence-design plugin candidate | Medium |
| LigandMPNN | Ligand-aware protein sequence design model | Future constrained design manifest target | Medium |

## Genomic and biological sequence models

| Project | Type | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|
| GENA-LM | Genomic masked language model | Sequence-model metadata reference | Medium |
| HyenaDNA | Long-range genomic foundation model | Genomics model manifest reference | Medium |
| Nucleotide Transformer | Genomics and transcriptomics foundation model | Model card and sequence workflow metadata reference | Medium |

## Docking, chemistry, and materials models

| Project | Type | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|
| DiffDock | AI molecular docking model | Example AI model plugin and feedback target | High |
| GNINA | Deep-learning molecular docking framework | Docking manifest comparison target | Medium |
| EquiBind | Geometric deep-learning docking model | Docking-model metadata reference | Low |
| TorchDrug | Drug-discovery machine-learning platform | Model/toolkit metadata reference | Low |
| GT4SD | Generative Toolkit for Scientific Discovery | Generative model registry/workflow metadata reference | Medium |
| REINVENT4 | AI molecular design and optimization tool | Workflow-scoped generative chemistry manifest candidate | Medium |
| AiZynthFinder | Retrosynthetic planning tool | Chemistry planning workflow/report-boundary reference | Medium |
| GuacaMol | Generative chemistry benchmark | Evaluation metadata reference | Low |
| MolBART | Molecular language model | Archived historical molecular-language-model reference | Low |
| Recursion GFlowNet | GFlowNet library for graph and molecular data | Generative molecular workflow reference | Medium |
| Uni-Mol | 3D molecular pretraining and downstream modeling framework | Molecular representation, docking/property, and model-weight metadata reference | Medium |
| Chemprop | Message-passing neural network package for molecular property prediction | Molecular property workflow and citation metadata reference | Medium |
| MACE | Machine-learning interatomic potential | Future materials model manifest target | Medium |
| NequIP | E(3)-equivariant interatomic potential framework | Atomistic model training/inference and HPC metadata reference | Medium |
| Allegro | Scalable equivariant interatomic potential model within the NequIP ecosystem | Large-scale atomistic simulation and LAMMPS/ASE integration metadata reference | Medium |
| MatterSim | Deep learning atomistic model | Future atomistic model manifest candidate | Medium |
| AI2BMD | AI-powered ab initio biomolecular dynamics simulation | Future biomolecular dynamics workflow reference | Medium |
| JMP | Atomic property prediction model | Archived historical atomistic model reference | Low |
| Google DeepMind materials_discovery | Materials discovery model/code reference | Future materials workflow metadata reference | Low |
| MatCalc | Materials property calculation library | Downstream materials workflow target | Medium |
| CHGNet | Charge-informed graph neural network potential | Atomistic model manifest candidate | Medium |
| M3GNet | Materials graph network | Archived/historical materials model metadata reference | Low |
| MatterGen | Generative inorganic materials model | Future generative-materials workflow reference | Medium |
| FAIR-Chem | Chemistry/materials machine-learning library | Broad model ecosystem reference | Medium |
| MatGL | Materials graph learning library | Future AI materials plugin example | Low |

## Model metadata fields to track

- model family and exact model version;
- source repository and release;
- model-weight URL, license, checksum, and retrieval policy;
- required input formats;
- expected output artifacts;
- required hardware and accelerator assumptions;
- environment options: Conda, Docker, Apptainer, system install;
- dry-run and smoke-test commands;
- citation requirements;
- data and training-domain limitations;
- unsafe or unsupported use cases.

## Open questions

- Should structure-prediction models, sequence-design models, and docking models share one manifest profile or use separate profiles?
- How strict should OpenSciFlow be about model-weight checksums before a model is marked `ready`?
- What should a report say when a model output is hypothesis-generating rather than experimentally validated?
