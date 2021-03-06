"""List of metadata fields, along with various attributes for use in catalog web page

"""

metadata_fields = [
    {
        'name': 'name',
        'title': r'Name',
        'tooltip': 'Primary short name by which this simulation is known',
        'type': 'text',
        'visible': True,
        'width': '110',
    },
    {
        'name': 'initial_separation',
        'title': r'$\mathrm{sep}^{\mathrm{ini}}$',
        'tooltip': 'Initial separation',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_orbital_frequency',
        'title': r'$\|\vec{\Omega}^{\mathrm{orb}\ \mathrm{ini}}\|$',
        'tooltip': 'Initial orbital frequency',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_adot',
        'title': r'$\dot{a}^{\mathrm{ini}}$',
        'tooltip': 'initial rate of change of separation',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'object_types',
        'title': r'Object types',
        'tooltip': 'Types of objects (BHBH, BHNS, or NSNS)',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'object1',
        'title': r'Object 1',
        'tooltip': 'Type of object 1 (BH or NS)',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'object2',
        'title': r'Object 2',
        'tooltip': 'Type of object 2 (BH or NS)',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'eos',
        'title': 'EOS',
        'tooltip': 'Equation of state',
        'type': 'text',
        'visible': False,
        'width': '180',
    },
    {
        'name': 'initial_ADM_energy',
        'title': r'$E^{\mathrm{ADM}}$',
        'tooltip': 'ADM energy measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_linear_momentum_mag',
        'title': r'$\|\vec{P}^{\mathrm{ADM}}\|$',
        'tooltip': 'ADM linear momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_linear_momentum_x',
        'title': r'${P}^{\mathrm{ADM}}_x$',
        'tooltip': 'x component of ADM linear momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_linear_momentum_y',
        'title': r'${P}^{\mathrm{ADM}}_y$',
        'tooltip': 'y component of ADM linear momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_linear_momentum_z',
        'title': r'${P}^{\mathrm{ADM}}_z$',
        'tooltip': 'z component of ADM linear momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_angular_momentum_mag',
        'title': r'$\|\vec{L}^{\mathrm{ADM}}\|$',
        'tooltip': 'ADM angular momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_angular_momentum_x',
        'title': r'${L}^{\mathrm{ADM}}_x$',
        'tooltip': 'x component of ADM angular momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_angular_momentum_y',
        'title': r'${L}^{\mathrm{ADM}}_y$',
        'tooltip': 'y component of ADM angular momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_ADM_angular_momentum_z',
        'title': r'${L}^{\mathrm{ADM}}_z$',
        'tooltip': 'z component of ADM angular momentum measured in the initial data',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_mass_ratio',
        'title': r'$M^{\mathrm{ini}, 1} / M^{\mathrm{ini}, 2}$',
        'tooltip': 'Ratio of initial masses',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_mass1',
        'title': r'$M^{\mathrm{ini}, 1}$',
        'tooltip': 'Initial mass of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_mass2',
        'title': r'$M^{\mathrm{ini}, 2}$',
        'tooltip': 'Initial mass of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_dimensionless_spin1_mag',
        'title': r'$\|\vec{\chi}^{\mathrm{ini}, 1}\|$',
        'tooltip': 'Initial dimensionless spin of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_dimensionless_spin1_x',
        'title': r'${\chi}^{\mathrm{ini}, 1}_x$',
        'tooltip': 'x component of Initial dimensionless spin of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_dimensionless_spin1_y',
        'title': r'${\chi}^{\mathrm{ini}, 1}_y$',
        'tooltip': 'y component of Initial dimensionless spin of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_dimensionless_spin1_z',
        'title': r'${\chi}^{\mathrm{ini}, 1}_z$',
        'tooltip': 'z component of Initial dimensionless spin of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_dimensionless_spin2_mag',
        'title': r'$\|\vec{\chi}^{\mathrm{ini}, 2}\|$',
        'tooltip': 'Initial dimensionless spin of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_dimensionless_spin2_x',
        'title': r'${\chi}^{\mathrm{ini}, 2}_x$',
        'tooltip': 'x component of Initial dimensionless spin of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_dimensionless_spin2_y',
        'title': r'${\chi}^{\mathrm{ini}, 2}_y$',
        'tooltip': 'y component of Initial dimensionless spin of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_dimensionless_spin2_z',
        'title': r'${\chi}^{\mathrm{ini}, 2}_z$',
        'tooltip': 'z component of Initial dimensionless spin of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'initial_position1_mag',
        'title': r'$\|\vec{x}^{\mathrm{ini}, 1}\|$',
        'tooltip': 'Initial position of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_position1_x',
        'title': r'${x}^{\mathrm{ini}, 1}_x$',
        'tooltip': 'x component of Initial position of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_position1_y',
        'title': r'${x}^{\mathrm{ini}, 1}_y$',
        'tooltip': 'y component of Initial position of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_position1_z',
        'title': r'${x}^{\mathrm{ini}, 1}_z$',
        'tooltip': 'z component of Initial position of object 1',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_position2_mag',
        'title': r'$\|\vec{x}^{\mathrm{ini}, 2}\|$',
        'tooltip': 'Initial position of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_position2_x',
        'title': r'${x}^{\mathrm{ini}, 2}_x$',
        'tooltip': 'x component of Initial position of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_position2_y',
        'title': r'${x}^{\mathrm{ini}, 2}_y$',
        'tooltip': 'y component of Initial position of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_position2_z',
        'title': r'${x}^{\mathrm{ini}, 2}_z$',
        'tooltip': 'z component of Initial position of object 2',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'relaxation_time',
        'title': r'$t^{\mathrm{rel}}$',
        'tooltip': 'Time at which system has "relaxed" from initial transient stage',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_time',
        'title': r'$t^{\mathrm{ref}}$',
        'tooltip': 'Time at which "reference" quantities are measured',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_mass_ratio',
        'title': r'$M^{\mathrm{ref}, 1} / M^{\mathrm{ref}, 2}$',
        'tooltip': 'Ratio of masses at reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_mass1',
        'title': r'$M^{\mathrm{ref}, 1}$',
        'tooltip': 'Mass of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_mass2',
        'title': r'$M^{\mathrm{ref}, 2}$',
        'tooltip': 'Mass of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin1_mag',
        'title': r'$\|\vec{\chi}^{\mathrm{ref}, 1}\|$',
        'tooltip': 'Dimensionless spin of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin1_x',
        'title': r'${\chi}^{\mathrm{ref}, 1}_x$',
        'tooltip': 'x component of Dimensionless spin of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin1_y',
        'title': r'${\chi}^{\mathrm{ref}, 1}_y$',
        'tooltip': 'y component of Dimensionless spin of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin1_z',
        'title': r'${\chi}^{\mathrm{ref}, 1}_z$',
        'tooltip': 'z component of Dimensionless spin of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin2_mag',
        'title': r'$\|\vec{\chi}^{\mathrm{ref}, 2}\|$',
        'tooltip': 'Dimensionless spin of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin2_x',
        'title': r'${\chi}^{\mathrm{ref}, 2}_x$',
        'tooltip': 'x component of Dimensionless spin of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin2_y',
        'title': r'${\chi}^{\mathrm{ref}, 2}_y$',
        'tooltip': 'y component of Dimensionless spin of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_dimensionless_spin2_z',
        'title': r'${\chi}^{\mathrm{ref}, 2}_z$',
        'tooltip': 'z component of Dimensionless spin of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position1_mag',
        'title': r'$\|\vec{x}^{\mathrm{ref}, 1}\|$',
        'tooltip': 'Position of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position1_x',
        'title': r'${x}^{\mathrm{ref}, 1}_x$',
        'tooltip': 'x component of Position of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position1_y',
        'title': r'${x}^{\mathrm{ref}, 1}_y$',
        'tooltip': 'y component of Position of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position1_z',
        'title': r'${x}^{\mathrm{ref}, 1}_z$',
        'tooltip': 'z component of Position of object 1 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position2_mag',
        'title': r'$\|\vec{x}^{\mathrm{ref}, 2}\|$',
        'tooltip': 'Position of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position2_x',
        'title': r'${x}^{\mathrm{ref}, 2}_x$',
        'tooltip': 'x component of Position of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position2_y',
        'title': r'${x}^{\mathrm{ref}, 2}_y$',
        'tooltip': 'y component of Position of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_position2_z',
        'title': r'${x}^{\mathrm{ref}, 2}_z$',
        'tooltip': 'z component of Position of object 2 after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_orbital_frequency_mag',
        'title': r'$\|\vec{\Omega}^{\mathrm{orb}\ \mathrm{ref}}\|$',
        'tooltip': 'Orbital frequency after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_orbital_frequency_x',
        'title': r'${\Omega}^{\mathrm{orb}\ \mathrm{ref}}_x$',
        'tooltip': 'x component of Orbital frequency after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_orbital_frequency_y',
        'title': r'${\Omega}^{\mathrm{orb}\ \mathrm{ref}}_y$',
        'tooltip': 'y component of Orbital frequency after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_orbital_frequency_z',
        'title': r'${\Omega}^{\mathrm{orb}\ \mathrm{ref}}_z$',
        'tooltip': 'z component of Orbital frequency after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'reference_eccentricity',
        'title': r'$e^{\mathrm{ref}}$',
        'tooltip': 'Eccentricity after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'reference_mean_anomaly',
        'title': r'$M^{\mathrm{ref}}$ (mean anomaly)',
        'tooltip': 'Mean anomaly after reference time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'merger_time',
        'title': r'$t^{\mathrm{merg}}$',
        'tooltip': 'Merger time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'number_of_orbits',
        'title': r'$N^{\mathrm{orbits}}$',
        'tooltip': 'Number of orbits from beginning of simulation to merger',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': True,
    },
    {
        'name': 'final_time',
        'title': r'$t^{\mathrm{fin}}$',
        'tooltip': 'Final time',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_mass',
        'title': r'$M^{\mathrm{rem}}$',
        'tooltip': 'Mass of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_dimensionless_spin_mag',
        'title': r'$\|\vec{\chi}^{\mathrm{rem}}\|$',
        'tooltip': 'Dimensionless spin of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_dimensionless_spin_x',
        'title': r'${\chi}^{\mathrm{rem}}_x$',
        'tooltip': 'x component of Dimensionless spin of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_dimensionless_spin_y',
        'title': r'${\chi}^{\mathrm{rem}}_y$',
        'tooltip': 'y component of Dimensionless spin of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_dimensionless_spin_z',
        'title': r'${\chi}^{\mathrm{rem}}_z$',
        'tooltip': 'z component of Dimensionless spin of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_velocity_mag',
        'title': r'$\|\vec{v}^{\mathrm{rem}}\|$',
        'tooltip': 'Velocity of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_velocity_x',
        'title': r'${v}^{\mathrm{rem}}_x$',
        'tooltip': 'x component of Velocity of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_velocity_y',
        'title': r'${v}^{\mathrm{rem}}_y$',
        'tooltip': 'y component of Velocity of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'remnant_velocity_z',
        'title': r'${v}^{\mathrm{rem}}_z$',
        'tooltip': 'z component of Velocity of remnant object',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'disk_mass',
        'title': r'$M^{\mathrm{disk}}$',
        'tooltip': 'Mass of any remaining disk',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'ejecta_mass',
        'title': r'$M^{\mathrm{ejecta}}$',
        'tooltip': 'Ejecta mass',
        'type': 'float',
        'sorter': 'limit_or_float',
        'visible': False,
    },
    {
        'name': 'initial_data_type',
        'title': r'ID type',
        'tooltip': 'Initial-data type',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'simulation_name',
        'title': r'Full name',
        'tooltip': 'Full simulation name used in production',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'alternative_names',
        'title': r'Other names',
        'tooltip': 'Other names by which this run has been known',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'authors_emails',
        'title': r"Authors' emails",
        'tooltip': 'Researchers who contributed to the generation of this waveform',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'simulation_bibtex_keys',
        'title': r'Sim bib keys',
        'tooltip': 'ADS BibTeX keys for this simulation',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'code_bibtex_keys',
        'title': r'Code bib keys',
        'tooltip': 'ADS BibTeX keys for the evolution code',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'initial_data_bibtex_keys',
        'title': r'ID bib keys',
        'tooltip': 'ADS BibTeX keys for the initial data',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'quasicircular_bibtex_keys',
        'title': r'QC bib keys',
        'tooltip': 'ADS BibTeX keys for eccentricity reduction',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'spec_revisions',
        'title': r'SpEC revisions',
        'tooltip': 'SpEC revisions',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'spells_revision',
        'title': r'SPELLS revision',
        'tooltip': 'SPELLS revision',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'keywords',
        'title': r'Keywords',
        'tooltip': 'Keywords to qualitatively identify this simulation',
        'type': 'text',
        'visible': False,
    },
    {
        'name': 'point_of_contact_email',
        'title': r'Contact',
        'tooltip': 'Point-of-contact email for this waveform.  Usually the person having placed the waveform into the repository.',
        'type': 'text',
        'visible': True,
        'itemTemplate': 'sxs_format_email'
    },
    {
        'title': 'Files',
        'type': 'text',
        'filtering': False,
        'visible': True,
        'itemTemplate': 'sxs_format_downloads'
    }
]
