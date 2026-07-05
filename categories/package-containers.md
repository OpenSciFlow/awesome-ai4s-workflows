# Package and Container Systems

OpenSciFlow should not become a new package manager. Instead, plugin manifests should declare how existing package and container systems can be used.

| Project | Type | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|
| Bioconda | Bioinformatics package channel | Packaging model reference | High |
| BioContainers | Bioinformatics container ecosystem | Container metadata and reproducibility reference | High |
| Spack | HPC package manager | HPC dependency metadata reference | High |
| Apptainer | HPC container runtime | Preferred HPC container execution target | High |
| Hugging Face Hub | Model and dataset hub | Model distribution analogy/integration target | Low |

## Open questions

- How should manifests represent Conda, Docker, Apptainer, and Spack without becoming too complex?
- How should model weight downloads be validated and licensed?
- What should be mandatory before marking a tool `ready`?

