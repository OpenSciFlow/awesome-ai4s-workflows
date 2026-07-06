# Awesome AI for Science Workflows

Curated landscape of AI for Science agents, workflow engines, local/HPC execution tools, model hubs, and reproducible scientific workflows.

## Why this exists

AI for Science tools are growing quickly, but researchers still struggle with environments, dependencies, HPC deployment, workflow orchestration, citation, and reproducibility.

OpenSciFlow does **not** aim to replace existing tools. This list maps the ecosystem so we can interoperate with established projects and identify practical metadata/workflow gaps.

## Status

Early curated draft. Project descriptions may be incomplete. Maintainers of listed projects are welcome to correct entries.

## Categories

- [AI for Science agents](categories/agents.md)
- [Scientific workflow engines](categories/workflow-engines.md)
- [Computational biology and molecular simulation workflows](categories/bio-molecular-workflows.md)
- [HPC and local execution tools](categories/hpc-local-execution.md)
- [Package and container systems](categories/package-containers.md)
- [Model hubs and model zoos](categories/model-hubs.md)
- [Scientific models](categories/scientific-models.md)
- [Reproducibility and provenance tools](categories/reproducibility.md)
- [Chemistry and materials workflow tools](categories/chemistry-materials.md)
- [中文摘要](zh/README.md)

## Data

The machine-readable seed list is in:

```text
data/projects.yaml
```

The current seed list includes 83+ related projects across agents, workflow systems, molecular simulation, HPC, packaging, reproducibility, model hubs, scientific models, chemistry, and materials science.

Detailed assessment metadata is in:

```text
data/project-assessments.yaml
```

Assessment fields include:

- `type`
- `strengths`
- `weaknesses`
- `relation_to_opensciflow`
- `contact_priority`

## Inclusion criteria

Projects should have at least one of:

- public repository or website;
- documented scientific workflow relevance;
- local/HPC execution relevance;
- package/container/reproducibility relevance;
- model/tool metadata relevance.

## Accuracy policy

Listed projects are related projects only. OpenSciFlow does not claim partnership unless explicitly approved by project maintainers.

If your project is listed inaccurately, please open an issue with:

- project name;
- corrected description;
- preferred citation or documentation link;
- whether you want the entry revised or removed.

## High-priority feedback targets

- BioBB / BioSimSpace maintainers
- MDAnalysis / MDTraj contributors
- OpenMM / GROMACS workflow authors
- Nextflow / Snakemake / Galaxy / nf-core community members
- AiiDA / Parsl / FireWorks workflow experts
- BioImage Model Zoo maintainers
- DiffDock / Boltz / ProteinMPNN / MACE / Protenix / GNINA / Uni-Mol / Chemprop / NequIP / Allegro / CHGNet / MatterGen / REINVENT4 / MatterSim / Nucleotide Transformer / ChemCrow / Biomni-style model or agent authors

## Contact priority definition

- `high`: ask for correction or focused feedback in the first outreach wave.
- `medium`: track for second-wave feedback or domain expansion.
- `low`: cite as context or analogy; do not ask for early collaboration.

## Start here

- Project metadata: `data/projects.yaml`
- Detailed assessments: `data/project-assessments.yaml`
- Category pages: `categories/`
- Chinese summary: `zh/README.md`
- First issue list: `ISSUES.md`
- First milestone: `MILESTONES.md`
