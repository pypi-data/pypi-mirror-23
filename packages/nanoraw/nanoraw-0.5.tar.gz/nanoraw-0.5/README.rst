pMetadata-Version: 1.1
Name: nanoraw
Version: 0.5
Author: Marcus Stoiber
Author-email: mhstoiber at lbl gov
Home-page: https://github.com/marcus1487/nanoraw
Download-url: UNKNOWN
Summary: Analysis of nanopore sequencing data.
License: BSD
Description: Summary
        -------
        
        This package provides tools for the analysis of raw nanopore sequencing
        data, including correction of basecalls and visualization.
        
        Full Documentation
        ------------------
        
        Full documentation avaialable at Read the Docs: https://nanoraw.readthedocs.io
        
        Installation
        ------------
        
        Install nanoraw without plotting dependencies (base genome_resquiggle algorithm and text outputs: wig and fasta)
        
        ::
        
           pip install nanoraw
        
        Install nanoraw with plotting dependencies (requires separate installation of R packages ggplot2 and cowplot)
        
        ::
        
           pip install nanoraw[plot]
        
        Install nanoraw via pip
        
        ::
        
            pip install nanoraw
        
        Install bleeding edge via github
        
        ::
        
            pip install git+https://github.com/marcus1487/nanoraw.git
        
        Usage
        -----
        
        ::
        
            nanoraw -h
            nanoraw [command] [options]
        
        
        Main Command (Must be run before any other commands):
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        -   :code:`genome_resquiggle`: Re-annotate raw signal with genomic aignement of existing basecalls.
        
        Genome Anchored Plotting Commands:
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        -   :code:`plot_max_coverage`: Plot signal in regions with the maximum coverage.
        -   :code:`plot_genome_location`: Plot signal at defined genomic locations.
        -   :code:`plot_motif_centered`: Plot signal at regions centered on a specific motif.
        -   :code:`plot_max_difference`: Plot signal where signal differs the most between two groups.
        -   :code:`plot_most_significant`: Plot signal where signal differs the most significantly between two groups.
        -   :code:`plot_motif_with_stats`: Plot signal from several regions and test statistics centered on a motif of interst.
        
        Sequencing Time Anchored Plotting Command:
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        -   :code:`plot_correction`: Plot segmentation before and after correction.
        -   :code:`plot_multi_correction`: Plot multiple raw signals anchored by genomic location.
        
        Other Plotting Command:
        ^^^^^^^^^^^^^^^^^^^^^^^
        
        -   :code:`plot_kmer`: Plot signal quantiles acorss kmers.
        -   :code:`cluster_most_significant`: Clustering traces at bases with significant differences.
        
        Auxiliary Command:
        ^^^^^^^^^^^^^^^^^^
        
        -  :code:`write_most_significant_fasta`: Write sequence where signal differs the most significantly between two groups.
        -  :code:`write_wiggles` :  Write wiggle files for nanopore signal values, coverage, and statistics.
        
            Get additional help for subcommands with ``nanoraw [command] -h``
        
        Requirements
        ------------
        
        -  HDF5 (http://micro.stanford.edu/wiki/Install_HDF5#Install)
        -  graphmap (https://github.com/isovic/graphmap)
           OR
        -  BWA-MEM (<http://bio-bwa.sourceforge.net/>)
        
        python Requirements:
        ^^^^^^^^^^^^^^^^^^^^
        
        -  numpy
        -  scipy
        -  h5py
        
        Optional plotting packages (install R packages with `install.packages([package_name])` from an R prompt):
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        -  rpy2 (python package; with R installation)
        -  ggplot2 (required for all plotting subcommands)
        -  cowplot (required for plot_motif_with_stats subcommand)
        
        Citation
        --------
        
        Stoiber, M.H. et al. De novo Identification of DNA Modifications Enabled by Genome-Guided Nanopore Signal Processing. bioRxiv (2016).
        
        http://biorxiv.org/content/early/2017/04/10/094672
        
        Legal
        -----
        
        nanoraw v.1 Copyright (c) 2016, The Regents of the University of
        California, through Lawrence Berkeley National Laboratory (subject to
        receipt of any required approvals from the U.S. Dept. of Energy). All
        rights reserved.
        
        If you have questions about your rights to use or distribute this
        software, please contact Berkeley Lab's Innovation and Partnerships
        department at IPO@lbl.gov referring to " nanoraw v.1 (2016-199)."
        
        NOTICE. This software was developed under funding from the U.S.
        Department of Energy. As such, the U.S. Government has been granted for
        itself and others acting on its behalf a paid-up, nonexclusive,
        irrevocable, worldwide license in the Software to reproduce, prepare
        derivative works, and perform publicly and display publicly. Beginning
        five (5) years after the date permission to assert copyright is obtained
        from the U.S. Department of Energy, and subject to any subsequent five
        (5) year renewals, the U.S. Government is granted for itself and others
        acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide
        license in the Software to reproduce, prepare derivative works,
        distribute copies to the public, perform publicly and display publicly,
        and to permit others to do so.
Keywords: nanopore high-throughput sequencing correction genome
Platform: UNKNOWN
