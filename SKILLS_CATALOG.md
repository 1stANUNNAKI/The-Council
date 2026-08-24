# 🧩 كتالوج المهارات الكامل — Skills Catalog (77)

> مولَّد آلياً من ترويسات SKILL.md الفعلية. الأوصاف بالإنجليزية (لغة التشغيل العالمية) والعناوين ثلاثية الدلالة.

> Auto-generated from real SKILL.md frontmatter. Deployed to 4 targets per skill.

## 🛡️ المسار الأمني — Security Pipeline (4)

| Skill | What it does |
|-------|--------------|
| `security-clean-code-auditor` | Audits code safety, prevents XSS/SQLi vulnerabilities, and enforces Clean Code standards. |
| `nuclei-security-auditor` | Security configuration auditing and vulnerability assessment using Nuclei templates. Verifies security headers, Cloudflare edge settings, CORS, and deployment safety. |
| `owasp-zap-api-shield` | Dynamic API security analysis and role-based isolation testing using OWASP ZAP in isolated sandbox environments. |
| `trufflehog-secret-scanner` | Automated secret scanning and credential leakage prevention using TruffleHog. Scans git repositories, commits, environment files, and build artifacts to prevent API key and credential leaks. |

## 🏛️ أدوار المجلس — Council Playbooks (16)

| Skill | What it does |
|-------|--------------|
| `maestro-hadi-orchestration` | Strategic coordination, agent orchestra routing, interactive user alignment, sidecars error monitoring, and macro task execution management. |
| `agent-weaver-builder` | Recruits and generates specialized custom agents dynamically adhering to the ReferenceStructure. |
| `intent-observer-audit360` | Performs 360-degree requirement auditing, implicit intention detection, and gap analysis. |
| `chronicle-logger-timestamp` | Automates real timestamp logging, work documentation, and update report generation. |
| `inner-learner-feedback` | Extracts lessons learned, user feedback, and internal corrective knowledge items. |
| `data-modeler-schema` | Designs robust database schemas, ERDs, and relationship models adhering to normal forms. |
| `stream-partitioner-bigdata` | Partitions large data streams, chunking payloads and managing memory efficiency. |
| `visual-diagrammer-mermaid` | Generates clean Mermaid charts, system architecture diagrams, and sequence flow visualizations. |
| `integrative-architect-docs` | Engineers standard system architecture, tech stack selection, and 14 integration documents. |
| `risk-assessor-feasibility` | Evaluates technical risks, feasibility studies, performance bottlenecks, and security trade-offs. |
| `backend-api-shield-services` | Builds secure backend services, REST/GraphQL APIs, authentication, and endpoint defense. |
| `cicd-automation-deploy` | Automates continuous integration pipelines, build scripts, deployment and environment setup. |
| `isolated-sandbox-environment` | Manages isolated execution contexts, safe script evaluation, and container sandbox testing. |
| `qa-automated-tester-unit` | Executes automated test suites, regression assertions, and quality assurance workflows. |
| `tool-innovator-skill-fetcher` | Searches, fetches, downloads, installs, and configures new skills and GitHub packages automatically. |
| `lightweight-dep-manager` | Manages package dependencies, audit trees, pruning unnecessary bloat for minimal overhead. |

## 🔬 قواعد البيانات العلمية — Science Databases (36)

| Skill | What it does |
|-------|--------------|
| `alphafold-database-fetch-and-analyze` | Retrieve and analyze AlphaFold predicted structures for a protein. Use when the user provides a specific UniProt Accession ID and wants structural confidence metrics (pLDDT), domain boundary analysis, or disorder assessment. Do not use if the user only has a protein name, gene name, or amino acid sequence — ask for a UniProt ID first. |
| `alphagenome-single-variant-analysis` | Analyzes genetic variant effects on gene expression (RNA-seq), chromatin accessibility (DNASE), histone marks (ChIP), and transcription factors using the AlphaGenome API. Use when the user asks about non-coding variant effects, pathogenicity, clinical significance, disease associations, functional effects, gene expression changes, splicing disruption, or regulatory effects in promoters and enhancers. Also use for resolving biological terms to tissue/cell-type ontologies (UBERON/CL) or analyzing variants in chr:pos:ref>alt format. |
| `chembl-database` | Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved drugs, and chemical structures. Use when the user asks about compounds, targets, IC50/Ki values, drug mechanisms, or structure searches. |
| `clinical-trials-database` | Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by condition, drug, location, status, or phase; retrieve trial details by NCT ID; check eligibility/inclusion criteria; count trials across conditions or time periods; identify a sponsor's trial portfolio; find recruiting trials for patient matching. |
| `clinvar-database` | Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Benign, VUS), clinical evidence rationales, or finding "hard positive" benchmark controls for human genomic variants. |
| `dbsnp-database` | Use when you want to look up, map, and search for short genetic variants (SNPs, indels) in NCBI's dbSNP database. Resolves between rsIDs, genomic coordinates in VCF format, and HGVS strings. For an rsID, returns variant type, gene associations, clinical significance, allele frequencies, and genomic coordinates (GRCh38). |
| `embl-ebi-ols` | Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, definitions, and hierarchies across 250+ ontologies (e.g., GO, DOID, HP). Use when the user asks to search for terms, retrieve details, navigate hierarchies (parents, children, ancestors), look up properties and individuals, get autocomplete suggestions, or access ontology metadata and statistics. |
| `encode-ccres-database` | Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API, or make custom queries to the ENCODE Portal REST API for experiments and files (ChIP-seq peaks, etc.). Use when you want to query regulatory annotations or raw experimental data across human cell types. |
| `ensembl-database` | Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or protein sequences, retrieve gene structures (exons), and get variant consequence and effect predictions (VEP). Use this skill as a primary ID translator, genomic sequence database and variant effect prediction tool. |
| `foldseek-structural-search` | Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API. Use ONLY when the user provides a physical 3D coordinate file (.cif, .mmcif, or .pdb) and wants to find structurally similar proteins. Do NOT use if the user only provides a protein sequence, gene name, or UniProt ID. |
| `gnomad-database` | Query the Genome Aggregation Database (gnomAD). Use when determining the rarity or allele frequency of specific genetic variants, retrieving gene constraint metrics (pLI, LOEUF) to assess loss-of-function intolerance, finding variants in a genomic region or gene, or querying structural variants. Don't use for analyzing individual patient genomes, tracking somatic mutations in cancer (use COSMIC), or requesting raw sequencing reads (use ENA). |
| `gtex-database` | Use when you want to retrieve quantitative RNA expression data and variant eQTL information from the GTEx (Genotype-Tissue Expression) Project across 54 non-diseased tissue sites. |
| `human-protein-atlas-database` | Use when you want to retrieve semi-quantitative protein expression and spatial localisation data from the Human Protein Atlas (HPA). |
| `interpro-database` | Identify domains, families, and sites in proteins; find all proteins in a family or sharing a domain; explore species distribution for a domain; annotate genomes with protein families and GO terms. InterPro combines 14 databases (e.g., Pfam, CDD) into one searchable resource. InterPro-N significantly expands annotation and sequence coverage with deep learning. Includes domain architecture (IDA) search. |
| `jaspar-database` | Query the JASPAR database for Transcription Factor (TF) binding profiles. Use when retrieving Position Frequency Matrices (PFMs) or Position Weight Matrices (PWMs) for specific TFs, resolving gene symbols to JASPAR Matrix IDs, or getting TF metadata. Supports multiple output formats (MEME, TRANSFAC, PFM, JASPAR, YAML). |
| `literature-search-arxiv` | Search for scientific papers, preprints, and publications on arXiv. Extract metadata, abstracts, and download full-text PDFs or HTML versions of papers. Use when the user asks to find research papers, literature, or specific arXiv IDs. |
| `literature-search-biorxiv` | Browse, filter, and download life sciences, biology, and medical preprints from bioRxiv and medRxiv. Supports fetching paper metadata by DOI, and browsing by date range with category and keyword filters. Keyword filtering is local, so date ranges MUST be narrow (1-4 weeks) with a category to prevent timeouts. |
| `literature-search-europepmc` | Search Europe PMC for scientific literature and download open-access full texts and PDFs. Retrieve full-text XML/plain text by PMCID, get citation lists and bibliography. |
| `literature-search-openalex` | Query the OpenAlex scholarly database for research papers, authors, institutions, topics, sources, publishers, funders, geo-locations, and keywords. Use when searching academic papers, resolving DOIs, downloading open-access PDFs, finding an author's publications, aggregating bibliometric data (citation counts, h-index, impact factor), exploring the research taxonomies, or performing DOI lookups. |
| `ncbi-sequence-fetch` | Retrieve protein and nucleotide sequences from NCBI databases using E-utilities. Supports direct accession lookup, CDS translation, gene+organism search, locus lookup, PubMed-linked sequences, patent protein extraction, and organism+length fallback search. Use when you need to fetch biological sequences by accession, gene name, locus tag, PubMed ID, or patent number. |
| `openfda-database` | Query, search, and download data from the openFDA API for drugs, devices, foods, tobacco, cosmetics, animal and veterinary products, substances, and transparency data. Use for FDA adverse events, recalls, labeling, approvals, shortages, 510(k) clearances, NDC lookups, and any FDA safety or regulatory data query across all 28 API endpoints. |
| `opentargets-database` | Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs, for therapeutic target identification. |
| `pdb-database` | Use when you want to search for or download experimentally-determined 3D structures for biomolecules (proteins, nucleic acids, bound ligands). Supports searching by sequence similarity, structure similarity, chemical and other attributes. Also use to get metadata about biomolecular structure experiments. |
| `pdf-scan-layer-cleaner` | مهارات تنظيف مستندات كتب الـ PDF الممسوحة ضوئياً من الطبقات المضللة، الخفيات الرمادية، الصور المزدوجة، ومسارات القص مع الحفاظ على النص الناصع وإمكانية البحث والنسخ دون ظهور مستطيلات سوداء. |
| `protein-sequence-msa` | Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need to align multiple sequences to assess similarity, domain conservation, or key residue conservation. Supports up to 4000 sequences and a maximum file size of 4 MB. Do not use to search for homologous proteins in a database (use MMseqs2, BLAST), align non-protein sequences (DNA, RNA), perform structural alignment (use Foldseek, PyMOL), or if you only have a single sequence. |
| `protein-sequence-similarity-search` | Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback). Trigger this whenever the user provides a protein sequence or FASTA file and asks to find homologues, sequence matches, or wants to infer protein function based on sequence similarity, but not when the user wants to infer protein function based on structural similarity. |
| `pubchem-database` | Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics. Use when a user asks about a specific chemical, drug, or molecule. |
| `pubmed-database` | Search PubMed for scientific literature, including published clinical trials. Fetch abstracts and full text. Link published research to biological databases (gene, protein, nucleotide, PubChem) to discover associations between papers and specific compounds or genes. Verify medical spelling, match raw citations, and cache result sets for bulk processing. Interfaces NCBI E-utilities and PMC BioC APIs. |
| `pymol` | Visualize, analyze, and render protein and molecular structures using PyMOL. Use when the user wants to create images of protein structures, perform structural alignments or superposition, measure distances or contacts, highlight binding sites or active site residues, color by B-factor/pLDDT, or analyze protein-ligand interactions. Do not use for docking, molecular dynamics, or sequence-only analysis. |
| `quickgo-database` | Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this when you need to map genes to biological processes, molecular functions, or cellular components, find genes associated with a specific pathway/GO term, or explore the Gene Ontology hierarchy. Do not use for querying drug targets (use OpenTargets) or mechanistic signaling pathway diagrams (use KEGG). |
| `reactome-database` | Query the Reactome database (Analysis and Content Services). Use when the user asks about pathway analysis, gene list enrichment, retrieving results by token, finding unmapped or not-found identifiers, mapping identifiers, reaction participants (inputs, outputs), pathway hierarchy (including top-level pathways), diagram export, cross-reference mapping, or searching the knowledgebase. |
| `string-database` | Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology. Use when the user asks about interactions between specific proteins, interaction evidence, confidence scores, protein interaction partners, or pathway enrichments. |
| `ucsc-conservation-and-tfbs` | Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding Sites (TFBS) from the UCSC Genome Browser. Use when analyzing whether genomic variants or regions are evolutionarily conserved, functionally important, or bounded by TF regulators across major projects (ENCODE, JASPAR, ReMap). |
| `unibind-database` | Queries the UniBind database for experimentally validated transcription factor (TF) binding sites. Use when retrieving direct TF-DNA interaction datasets, downloading binding site coordinates (BED/FASTA) for local analysis, or listing available datasets by species, cell line, or TF name. Don't use to query specific intervals, locations, genes, motif models or expression data. |
| `uniprot-database` | Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and UniRef. Use when searching for proteins, mapping identifiers, or retrieving functional annotations and publications. Don't use for sequence alignment, protein folding, or sequence similarity search (use specialized skills for those tasks). |
| `uv` | Checks whether the uv Python package manager is installed and installs it if missing. Ensures uv is on PATH. Use when another skill requires uv as a prerequisite. |

## 🎨 الإنتاج الإبداعي — Creative Production (14)

| Skill | What it does |
|-------|--------------|
| `cinematic-animator-gsap` | Creates fluid 60FPS UI animations, scroll triggers, GSAP timelines, and micro-interactions. |
| `design-system-master-hsl` | Maintains design tokens, dark modes, Shadcn/HSL color palettes, and glassmorphism styling. |
| `responsive-layout-engine` | Enforces 100% multi-device responsiveness, CSS Grid/Flexbox stability, and mobile optimizations. |
| `vector-print-publisher-pdf` | Renders vector PDFs, high-DPI print templates, and document layouts ready for export. |
| `frontend-clean-coder-js` | Generates modular, accessible, Clean Code frontend components and UI logic. |
| `neuro-marketing-copywriter` | Applies Grand Slam offer frameworks, high-converting copywriting, and neuro-marketing funnels. |
| `advanced-image-slicing-skill` | Custom specialized skill for advanced_image_slicing_skill. |
| `animation-scroll-effects` | Animation and scroll effects skill using GSAP, Lenis, and Framer Motion. |
| `explode-animation-skill` | Custom specialized skill for explode_animation_skill. |
| `marketing-funnel-skill` | Custom specialized skill for marketing_funnel_skill. |
| `premium-visual-polish-skill` | Custom specialized skill for premium_visual_polish_skill. |
| `psychological-copywriting-skill` | Custom specialized skill for psychological_copywriting_skill. |
| `remotion-video-engine` | وثيقة مهارة مخصصة لإنشاء وإنتاج الموشن جرافيكس والفيديوهات البرمجية الديناميكية باستخدام Remotion و React. تغطي آلية معالجة المدخلات من مجلد start/<project_name> وقراءة الصور والبرومبت والطلبات، وتحويلها إلى مقاطع فيديو متكاملة وحفظها في out/. |
| `tech-background-skill` | Custom specialized skill for tech_background_skill. |

## ☁️ Cloudflare — Cloudflare (2)

| Skill | What it does |
|-------|--------------|
| `cloudflare-ai-resources` | Provides comprehensive guidelines, instructions, billing protection rules, and boilerplate templates to work with Cloudflare Workers AI free models (Text, Image, and Audio) using the official documentation reference. |
| `k6-load-testing` | "Comprehensive k6 load testing skill for API, browser, and scalability testing. Write realistic load scenarios, analyze results, and integrate with CI/CD." |

## 🧰 أدوات النظام — System Meta (5)

| Skill | What it does |
|-------|--------------|
| `majlis-rules` | Custom specialized skill for antigravity_rules. |
| `find-skills` | البحث والاستكشاف المتقدم عن الأدوات والمهارات المفتوحة المصدر المتاحة على GitHub والمكتبات العالمية وتضمينها بالنظام. تستخدم لاستكشاف الحلول وجلب الاعتماديات التقنية للوكلاء تلقائياً. |
| `google-antigravity-sdk` | "Design, implement, and debug autonomous AI agents and multi-agent systems using the Google Antigravity (AGY) SDK. ACTIVATE this skill when the user wants to create, configure, or orchestrate Google Antigravity agents." |
| `skill-creator` | توليد، تصميم، وبناء المهارات البرمجية والوكلاء الجدد تلقائياً وفق المواصفات القياسية لنظام أنتيغرافيتي. تُستخدم لإنشاء وتجهيز ملفات SKILL.md وتأسيس متطلبات التشغيل والأكواد التأسيسية. |
| `workflow-skill-creator` | Distills a completed user workflow or interaction into a reusable agent skill. Use when the user asks to turn their workflow, interaction, or multi-step process into a skill, or when they say "make this a skill", "create a skill from what we just did", "package this workflow" or similar. Do not use for creating skills from scratch without an existing workflow (use a generic skill-creator for that). |

---

**المجموع Total: 77 مهارة منشورة ×4 منصات deployed across 4 targets.**
