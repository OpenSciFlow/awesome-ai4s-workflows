# Computational Biology and Molecular Simulation Workflows

This category is the first practical focus area for OpenSciFlow.

The first reference demo is a protein molecular dynamics stability analysis workflow that uses an existing trajectory and produces RMSD, RMSF, radius of gyration, plots, logs, artifacts, and a reproducibility report.

| Project | Type | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|
| BioBB | Biomolecular workflow building blocks | Top feedback target for protein/MD workflow templates | High |
| BioSimSpace | Molecular simulation interoperability | Top feedback target for simulation plugin/workflow design | High |
| GROMACS | Molecular dynamics engine | Core protein MD plugin target | Medium |
| CHARMM-GUI | Molecular simulation setup platform | UX and setup workflow reference | Medium |
| OpenMM | Python molecular simulation toolkit | MVP-friendly runtime target | High |
| MDAnalysis | Trajectory analysis library | Core MVP analysis plugin target | High |
| MDTraj | Trajectory analysis library | Fallback/alternative analysis plugin | Medium |
| ColabFold | Protein structure workflow | Structure prediction plugin/template reference | Medium |
| ESM / ESMFold | Protein language model | Future model plugin target | Low |
| OpenFold | AlphaFold2-style implementation | Structure-prediction manifest reference | Medium |
| Uni-Fold | Protein structure prediction platform | Structure-prediction metadata reference | Medium |
| Boltz | Biomolecular interaction model | Model-focused manifest candidate | Medium |
| Chai-1 | Biomolecular structure model | Structure-model metadata comparison target | Medium |
| Protenix | Biomolecular structure prediction model | AlphaFold3-style workflow metadata reference | Medium |
| RoseTTAFold-All-Atom | All-atom biomolecular modeling model | Complex input/output and license metadata reference | Medium |
| RFdiffusion | Protein backbone generation model | Future protein-design workflow reference | Medium |
| ProteinMPNN | Protein sequence design model | Future sequence-design plugin candidate | Medium |
| LigandMPNN | Ligand-aware protein design model | Future constrained design manifest target | Medium |

## Open questions

- Which trajectory-analysis outputs are minimally useful for a first report?
- How should force-field and simulation setup provenance be recorded?
- How should reports prevent overclaiming from RMSD/RMSF/Rg metrics?
