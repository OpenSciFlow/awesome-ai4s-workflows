# HPC and Local Execution

OpenSciFlow is local-first: workflows should run on the user's workstation, lab server, or HPC environment whenever possible.

This category tracks tools and systems relevant to local/HPC execution, scheduling, web access, and deployment.

| Project | Type | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|
| Slurm | HPC workload manager | Core scheduler adapter target | Medium |
| Open OnDemand | HPC web portal | Deployment and HPC UX reference | Medium |
| Parsl | Python/HPC execution | Potential execution backend | High |
| FireWorks | High-throughput workflow manager | HPC workflow metadata reference | Medium |
| Pegasus WMS | Large-scale scientific workflow | Long-term HPC reference | Medium |
| Apptainer | HPC container runtime | Preferred HPC container target | High |
| Spack | HPC package manager | Dependency metadata and installation reference | High |

## Open questions

- What should a plugin manifest declare for Slurm support?
- Should OpenSciFlow v0.1 submit jobs, or only generate dry-run scripts?
- How should site-specific HPC policies be represented without overfitting?

