# Scientific Workflow Engines

This category tracks workflow systems and standards that already solve important parts of scientific execution, scalability, portability, and provenance.

OpenSciFlow should not replace these systems. It should describe tools and workflow templates in a way that can later map to mature backends such as Nextflow, Snakemake, CWL, Parsl, AiiDA, FireWorks, or Pegasus.

| Project | Type | Strength | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|---|
| Nextflow | Workflow engine | Mature HPC/cloud workflow execution | Potential backend/interoperability target | High |
| nf-core | Workflow community | Strong governance and review practices | Governance model reference | High |
| Snakemake | Workflow engine | Pythonic, reproducible, HPC-capable | Potential backend/interoperability target | High |
| Galaxy | Web workflow platform | Mature biomedical workflow UX and training | UX/community reference | High |
| Common Workflow Language | Workflow standard | Neutral portable workflow standard | Align with, not replace | High |
| Cromwell / WDL | Workflow language/engine | Established in genomics | Genomics interop reference | Medium |
| Parsl | Python parallel workflow | Strong Python/HPC fit | Potential execution backend | High |
| FireWorks | High-throughput workflow manager | Proven in materials workflows | Metadata/materials reference | Medium |
| Pegasus WMS | Large-scale workflow system | Robust large-scale execution | Long-term HPC reference | Medium |
| AiiDA | Workflow and provenance platform | Strong provenance model | Key provenance reference | High |

## Open questions

- Should OpenSciFlow workflow templates compile into existing engines?
- Which fields overlap with CWL/Snakemake/Nextflow metadata?
- What is the smallest useful interoperability target for v0.2?

