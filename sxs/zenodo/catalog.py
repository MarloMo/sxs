
# NOTE: This string is placed into the top of the catalog JSON file as a JSON string.  JSON strings
# are enclosed in double quotes, so it would quickly get ugly if we used double quotes within this
# description, even though python makes that easy.
catalog_file_description = """
    This JSON file has the following format.  Comments are, of course, not present (since JSON does not support
    comments).  Single quotes here are, of course, double quotes in the rest of the file (since JSON encloses
    strings in double quotes).  Anything inside <angle brackets> is just standing in for the relevant value.  An
    ellipsis ... indicates that the preceding structure can be repeated.  Also note that the metadata entries for
    simulations may not be present if the record on zenodo is closed-access; see catalog_private_metadata.json if
    you have access to those simulations, which will contain the missing information.  That file should be read
    and written automatically by functions in this module, so that the catalog dict returned will contain all
    available information.

    {
        'catalog_file_description': '<this description>',
        'modified': '<YYYY-MM-DDThh:mm:ss.ssssss>',  # UTC time of last-modified record in this file
        'records': {  # Includes *all* records published on Zenodo in the 'sxs' community, not just simulations
            '<id>': {  # This Zenodo ID key is a *string* containing the 'id' value inside this object (JSON requires keys to be strings)
                # More details about this 'representation' object at http://developers.zenodo.org/#depositions
                'conceptdoi': '10.5281/zenodo.<conceptrecid>',  # Permanent DOI for all versions of this record
                'conceptrecid': '<conceptrecid>',  # ~7-digit integer (as string) collectively identifying all versions of this record
                'created': '<YYYY-MM-DDThh:mm:ss.ssssss>',  # UTC time of creation of this record on Zenodo
                'doi': '10.5281/zenodo.<id>',  # Permanent DOI for this record
                'doi_url': 'https://doi.org/10.5281/zenodo.<id>',  # URL for permanent DOI of this record
                'id': <id>,  # ~7-digit integer uniquely identifying this record
                'links': {
                     'badge': 'https://zenodo.org/badge/doi/10.5281/zenodo.<id>.svg',
                     'bucket': 'https://zenodo.org/api/files/<uuid>',  # Base URL for file uploads and downloads
                     'conceptbadge': 'https://zenodo.org/badge/doi/10.5281/zenodo.<conceptrecid>.svg',
                     'conceptdoi': 'https://doi.org/10.5281/zenodo.<conceptrecid>',  # Permanent link to webpage for most-recent version
                     'discard': 'https://zenodo.org/api/deposit/depositions/<id>/actions/discard',  # API action to discard a draft
                     'doi': 'https://doi.org/10.5281/zenodo.<id>',  # Permanent URL for this version
                     'edit': 'https://zenodo.org/api/deposit/depositions/<id>/actions/edit',  # API action to edit this record
                     'files': 'https://zenodo.org/api/deposit/depositions/<id>/files',  # Only present for author
                     'html': 'https://zenodo.org/deposit/<id>',  # Webpage for this version
                     'latest': 'https://zenodo.org/api/records/<id>',  # API endpoint for most-recent version
                     'latest_html': 'https://zenodo.org/record/<id>',  # Webpage for most-recent version
                     'publish': 'https://zenodo.org/api/deposit/depositions/<id>/actions/publish',  # Only present for author
                     'record': 'https://zenodo.org/api/records/<id>',  # Only present for author
                     'record_html': 'https://zenodo.org/record/<id>',  # Webpage for this particular version; only present for author
                     'self': 'https://zenodo.org/api/deposit/depositions/<id>'
                },
                'metadata': {  # Note that this is Zenodo metadata, and is different from the SXS metadata found below
                    'access_right': '<access>',  # Can be 'open', 'closed', 'embargoed', or 'restricted'
                    'communities': [
                        {'identifier': '<community_name>'},  # Names may include 'sxs' and 'zenodo'
                        ...
                    ],
                    'creators': [
                        {
                            'name': '<name>',  # Name of this creator in the format Family name, Given names
                            'affiliation': '<affiliation>',  # (Optional) Affiliation of this creator
                            'orcid': '<orcid>',  # (Optional) ORCID identifier of this creator
                            'gnd': '<gnd>'  # (Optional) GND identifier of this creator
                        },
                        ...
                    ],
                    'description': '<description>',  # Text description of this record
                    'doi': '10.5281/zenodo.<id>',  # Permanent DOI of this record
                    'keywords': [
                        '<keyword>',  # Optional; this array may be empty
                        ...
                    ],
                    'license': '<license_type>',  # Usually 'CC-BY-4.0' for SXS
                    'prereserve_doi': {'doi': '10.5281/zenodo.<id>', 'recid': <id>},
                    'publication_date': '<YYYY-MM-DD>',  # Possibly meaningless date (UTC)
                    'title': '<title>',
                    'upload_type': 'dataset'
                },
                'modified': '<YYYY-MM-DDThh:mm:ss.ssssss>',  # (UTC) Last modification of this record (possibly just Zenodo metadata modified)
                'owner': <user_id>,  # ~5-digit integer identifying the user who owns this record
                'record_id': <id>,  # Same as 'id'
                'state': '<state>',  # Can be 'done', 'inprogress', 'error', 'unsubmitted', possibly others
                'submitted': <submitted>,  # True or false (always true for published records)
                'title': '<title>'  # Same as ['metadata']['title'],
                'files': [  # May not be present if this simulation is closed-access; see catalog_private_metadata.json as noted above
                    # See https://data.black-holes.org/waveforms/documentation.html for
                    # detailed descriptions of the *contents* of the files in each record.
                    {
                        'checksum': '<checksum>',  # MD5 checksum of file on Zenodo
                        'filename': '<filename>',  # Name of file; may contain slashes denoting directories
                        'filesize': <filesize>,  # Number of bytes in the file
                        'id': '<fileid>',  # A standard UUID (hexadecimal with characters in the pattern 8-4-4-4-12)
                        'links': {
                            'download': 'https://zenodo.org/api/files/<bucket>/<filename>',  # The URL to use to download this file
                            'self': 'https://zenodo.org/api/deposit/depositions/<deposition_id>/files/<fileid>'  # Ignore this
                        }
                    },
                    ...  # Other file descriptions in the order in which they were uploaded (not necessarily a meaningful order)
                ]
            },
            ...
        },
        'simulations': {  # Physical data (masses, spins, etc.) for all available SXS simulations
            '<sxs_id>': {  # The SXS ID is a string like SXS:BHNS:0001 or SXS:BBH:1234
                'url': '<URL>',  # The URL of the Zenodo 'conceptdoi' link, which *resolves to* the most-recent version
                #
                # NOTE: All of the following may be absent if this simulation is closed-access, or simply does not have metadata.
                #
                # Variable content describing (mostly) physical parameters of the system.  It's basically a
                # python-compatible version of the information contained in 'metadata.txt' from the
                # highest-resolution run in the most-recent version of this simulation.  That file is meant to
                # be more-or-less as suggested in <https://arxiv.org/abs/0709.0093>.  The conversion to a
                # python-compatible format means that keys like 'simulation-name' have had hyphens replaced by
                # underscores so that they can be used as variable names in python and any other sane language
                # (with apologies to Lisp).  As far as possible, values that are just strings in that file
                # have been converted into the relevant types -- like numbers, integers, and arrays.  Note
                # that some keys like eccentricity are sometimes numbers and sometimes the string '<number'
                # (meaning that the eccentricity is less than the number), which is necessarily a string.
                #
                # Below are just the first few keys that *may* be present.  Note that closed-access
                # simulations will have empty dictionaries here.
                #
                'simulation_name': '<directory_name>',  # This may be distinctly uninformative
                'alternative_names': '<sxs_id>',  # This may be a list of strings
                'initial_data_type': '<type>',  # Something like 'BBH_CFMS'
                'object_types': '<type>',  # Currently 'BHBH', 'BHNS', or 'NSNS'
                'number_of_orbits': <number>,  # This is a float, rather than an integer
                'relaxed_mass_ratio': <q>,  # Usually greater than 1 (exceptions are due to junk radiation)
                'relaxed_chi_eff': <chi_eff>,  # Dimensionless effective spin quantity
                'relaxed_chi1_perp': <chi1_perp>,  # Magnitude of component of chi1 orthogonal to 'relaxed_orbital_frequency'
                'relaxed_chi2_perp': <chi2_perp>,  # Magnitude of component of chi2 orthogonal to 'relaxed_orbital_frequency'
                'relaxed_mass1': <m2>,
                'relaxed_mass2': <m1>,
                'relaxed_dimensionless_spin1': [
                    <chi1_x>,
                    <chi1_y>,
                    <chi1_z>
                ],
                'relaxed_dimensionless_spin2': [
                    <chi2_x>,
                    <chi2_y>,
                    <chi2_z>
                ],
                'relaxed_eccentricity': <eccentricity>,  # A float or possibly a string containing '<' and a float
                'relaxed_orbital_frequency': [
                    <omega_x>,
                    <omega_y>,
                    <omega_z>
                ],
                'relaxed_measurement_time': <time>,
                ...
            },
            ...
        }
    }
"""


def _include_file_data(login, record):
    """Ensure that 'files' field is present in the input record"""
    if 'files' not in record:
        if 'files' in record.get('links', {}):
            url = record['links']['files']
        elif 'id' in record:
            url = login.base_url + 'api/deposit/depositions/{0}/files'.format(record['id'])
        else:
            return record  # We have failed, but we're not too upset
        r = login.session.get(url)
        if r.status_code == 200:  # Otherwise, we just couldn't add this record; oh well.
            r_json = r.json()
            record['files'] = r_json
    return record


def _create_simulations_skeleton(record_list):
    """Create a dictionary of simulations with information for downloading SXS metadata"""
    from .. import sxs_id
    return {
        sxs_id(r.get('title', '')): {
            'url': r['links']['conceptdoi'],
            'metadata_file_info': max([f for f in r.get('files', []) if '/metadata.json' in f['filename']],
                                      default={}, key=lambda f:f['filename'])
        }
        for r in record_list if sxs_id(r.get('title', ''))
    }


def _download_sxs_metadata(login, simulations):
    """Download metadata.json from Zenodo for each simulation, if needed"""
    import traceback
    from tqdm.autonotebook import tqdm
    for sxs_id in tqdm(simulations, dynamic_ncols=True):
        download_url = simulations[sxs_id].get('metadata_file_info', {}).get('links', {}).get('download', '')
        if not download_url:
            continue
        try:
            metadata = login.session.get(download_url).json()
            simulations[sxs_id].pop('metadata_file_info')
            simulations[sxs_id].update(metadata)
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()



def create(login=None):
    """Create the catalog from scratch

    This function will take quite some time (more than 15 minutes), because it has to download
    each metadata file individually, which necessarily requires a separate Zenodo request
    for each download.

    """
    from textwrap import dedent
    from . import Login

    # If login is None, this creates a Login object to use
    l = login or Login()

    # Get the list of all SXS records from Zenodo
    records = l.search(q='communities:sxs')

    # Closed-access records don't have their files included by default; add them
    records = [_include_file_data(l, record) for record in records]

    # Sort the list of records by title
    records = sorted(records, key=lambda r: r.get('title', ''))
    
    # Find the most recent modification time in any record
    modified = max(r.get('modified', '') for r in records)

    # Make an outline of the 'simulations' dict, with info for highest-Lev metadata.json file in
    # place of the actual metadata.
    simulations = _create_simulations_skeleton(records)

    # Loop through the dictionary we just created, and download the metadata.json for each one
    _download_sxs_metadata(l, simulations)

    # Create the catalog itself
    catalog = {
        'catalog_file_description': dedent(catalog_file_description).split('\n')[1:-1],
        'modified': modified,
        'records': {r['links']['conceptdoi']: r for r in records},
        'simulations': simulations
    }
    return catalog


def split_catalog(catalog):
    """Split catalog four ways: private vs. public, and complete vs. just simulations

    This function splits the catalog into four separate parts:

      1) The complete catalog for open-access systems
      2) The SXS metadata for open-access systems
      3) The complete catalog for all systems
      4) The SXS metadata for all systems

    The complete catalog contains all Zenodo metadata and SXS metadata, as well as a description of
    the catalog and the most recent modification time.  The simulations are useful for serving data
    used in the waveform index table at <https://data.black-holes.org/waveforms/catalog.html>,
    because it is significantly less data.  The private data can be served via the wiki, with the
    public data as a fallback if the user's web browser does not send credentials along with the
    request for the data.

    """
    import copy
    private_catalog = copy.deepcopy(catalog)
    private_simulations = copy.deepcopy(catalog['simulations'])
    public_catalog = {
        'catalog_file_description': catalog['catalog_file_description'],
        'modified': catalog['modified'],
        'records': {
            recid: catalog['records'][recid]
            for recid in catalog['records']
            if catalog['records'][recid].get('metadata', {}).get('access_right', '') == 'open'
        }
    }
    public_conceptdoi_links = [public_catalog['records'][recid].get('links', {}).get('conceptdoi', None)
                               for recid in public_catalog['records']]
    public_catalog['simulations'] = {
        sxs_id: catalog['simulations'][sxs_id]
        for sxs_id in catalog['simulations']
        if catalog['simulations'][sxs_id]['url'] in public_conceptdoi_links
    }
    public_simulations = copy.deepcopy(public_catalog['simulations'])
    return private_catalog, private_simulations, public_catalog, public_simulations


def write_split_catalogs(catalog, public_dir='~/.sxs/catalog/', private_dir='~/.sxs/catalog/'):
    """Write four versions of the catalog to files

    The input catalog is first split into four parts by `split_catalog` (see that function's
    docstring for details).  These will be written into four separate JSON files.  If the public and
    private directories input as arguments to this function are the same, the files will be named
    private_catalog.json, private_simulations.json, public_catalog.json, and
    public_simulations.json.  Otherwise, the prefixes will be removed so that the files are named
    either catalog.json or simulations.json when placed in their respective directories.

    Parameters
    ==========
    catalog: dict
        The catalog in the standard format output by functions in this submodule, and described in
        `sxs.zenodo.catalog.catalog_file_description`.
    public_dir: str, optional [defaults to '~/.sxs/catalog/']
    private_dir: str, optional [defaults to '~/.sxs/catalog/']
        Absolute or relative paths to the directory in which the files will be written.  If they do
        not exist, they will be created.  Note that, as explained above, the output file names will
        depend on whether these two arguments are the same or different.

    """
    from os.path import expanduser, normpath, join, exists, dirname
    import json

    def mkdirs(path):
        # In python >3.2, this could just be os.makedirs(path, exist_ok=True)
        import errno
        import os
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    public_dir = normpath(expanduser(public_dir))
    private_dir = normpath(expanduser(private_dir))
    mkdirs(public_dir)
    mkdirs(private_dir)

    if public_dir == private_dir:
        public_prefix = 'public_'
        private_prefix = 'private_'
    else:
        public_prefix = ''
        private_prefix = ''
    
    private_catalog, private_simulations, public_catalog, public_simulations = split_catalog(catalog)

    public_catalog_path = join(public_dir, public_prefix+'catalog.json')
    public_simulations_path = join(public_dir, public_prefix+'simulations.json')
    private_catalog_path = join(private_dir, private_prefix+'catalog.json')
    private_simulations_path = join(private_dir, private_prefix+'simulations.json')
    with open(public_catalog_path, 'w') as f:
        json.dump(public_catalog, f, indent=2, separators=(',', ': '), ensure_ascii=True)
    with open(public_simulations_path, 'w') as f:
        json.dump(public_simulations, f, indent=None, separators=(',', ':'), ensure_ascii=True)
    with open(private_catalog_path, 'w') as f:
        json.dump(private_catalog, f, indent=2, separators=(',', ': '), ensure_ascii=True)
    with open(private_simulations_path, 'w') as f:
        json.dump(private_simulations, f, indent=None, separators=(',', ':'), ensure_ascii=True)


def update(login=None, path='~/.sxs/catalog/private_catalog.json', verbosity=1,
           public_out_dir='~/.sxs/catalog/', private_out_dir='~/.sxs/catalog/'):
    """Update a local copy of the SXS catalog from Zenodo

    Note: This function works in place, by overwriting the input catalog file, as well as the other
    three versions of it produced by `split_catalog`.

    Parameters
    ==========
    login: sxs.zenodo.Login object, optional [defaults to new Login object]
        This is used to query Zenodo for new data.
    path: str, optional [defaults to '~/.sxs/catalog/private_catalog.json']
        Absolute or relative path to JSON file containing the complete catalog.  If the path does
        not end with '.json', it is assumed to be a directory containing a 'catalog.json' or
        'private_catalog.json' file.
    verbosity: int, optional [defaults to 1]
        Amount of information to output.  Less than 1 corresponds to no output; 1 to only print a
        notice if the private file cannot be retrieved; greater than 1 to print a notice about
        wherever the file is retrieved; greater than 2 shows the stdout/stderr from external calls;
        and greater than 3 also asks git to be verbose.
    public_out_dir: str, optional [defaults to '~/.sxs/catalog/']
    private_out_dir: str, optional [defaults to '~/.sxs/catalog/']
        These are passed to the `save_split_catalogs` function; see that function's docstring for
        details.

    """
    from os.path import expanduser, join, dirname, exists
    import json

    # Make sure that the catalog file exists
    path = expanduser(path)
    if not path.endswith('.json'):
        path = join(path, 'private_catalog.json')
        if not exists(path):
            path = join(path, 'catalog.json')
    if not exists(path):
        raise ValueError("Could not find catalog file in '{0}'.".format(dirname(path)))

    # Read the catalog file
    with open(path, 'r') as f:
        catalog = json.load(f)
    records = catalog['records']
    simulations = catalog['simulations']

    # If login is None, this creates a Login object to use
    l = login or Login()

    # Get the list of all SXS records from Zenodo
    new_records = {r['links']['conceptdoi']: r for r in l.search(q='communities:sxs')}

    # Loop through the new records, ensuring that they are all present and current in the old records
    for r in new_records:
        if r not in records or new_records[r].get('modified', 0) != records[r].get('modified', 1):
            records[r] = _include_file_data(l, new_records[r])
            new_simulation = _create_simulations_skeleton([records[r],])
            simulations.update(new_simulation)

    write_split_catalogs(catalog, public_dir=public_out_dir, private_dir=private_out_dir)
    return catalog


def modification_time(representation_list):
    return max(r['modified'] for r in representation_list)


def sxs_metadata_file_description(representation):
    """Find metadata file from highest Lev for this simulation"""
    from os.path import basename
    files = representation.get('files', [])
    metadata_files = [f for f in files if basename(f['filename'])=='metadata.json']
    metadata_files = sorted(metadata_files, key=lambda f: f['filename'])
    if not metadata_files:
        return None
    return metadata_files[-1]


def fetch_metadata(url, login=None, *args, **kwargs):
    """Get the json file from zenodo"""
    from .api import Login
    login = login or Login(*args, **kwargs)
    r = login.session.get(url)
    if r.status_code != 200:
        return {}
    try:
        return r.json()
    except:
        return {}


def nginx_map(sxs_id_to_conceptrecid, map_file_path=None):
    """Create a mapping from SXS identifiers to Zenodo record numbers for nginx

    The input must be a catalog file.  The output is formatted for inclusion into an nginx
    configuration.  Note that this map file includes a `map_hash_max_size` directive, and thus must
    precede any `map` directives, or you will get an error that this directive is a duplicate (even
    if you never explicitly gave it previously).

    The output map matches the plain SXS identifier (with nothing following it).

    Parameters
    ==========
    sxs_id_to_conceptrecid: dict
        A dictionary mapping SXS IDs to Zenodo's concept-record IDs.
    map_file_path: None or string [defaults to None]
        Relative or absolute path to the nginx map file to be output.  If `None`, the function first
        attempts to write the file into '~/.sxs/catalog/sxs_to_zenodo.map'; if that is not possible,
        it tries to write to the same file in the current working directory.

    """
    from os.path import expanduser, exists, join, dirname
    import json
    import math
    def touch(fname, times=None):
        from os import utime
        try:
            with open(fname, 'a'):
                utime(fname, times)
            return True
        except:
            pass
        return False
    # Decide on where to put the output
    if map_file_path is None:
        if touch(expanduser('~/.sxs/catalog/sxs_to_zenodo.map')):
            map_file_path = expanduser('~/.sxs/catalog/sxs_to_zenodo.map')
        elif touch('sxs_to_zenodo.map'):
            map_file_path = 'sxs_to_zenodo.map'
        else:
            raise ValueError("Cannot write to 'sxs_to_zenodo.map' file in current directory or in ~/.sxs/catalog/.")
    else:
        map_file_path = expanduser(map_file_path)
    # Figure out how to construct the output
    size = 64 * 2**math.ceil(math.log2(len(sxs_id_to_doi_url)+1))  # nginx needs this to know the hash size
    record_string = "  {0} {1};\n"
    # Construct the output
    with open(map_file_path, 'w') as f:
        f.write("map_hash_max_size {0};\n".format(size))
        f.write("map $sxs_id $zenodo_identifier {\n")
        f.write("    default ../communities/sxs;\n")  # A bit hackish, but it gets us where we want to go
        for sxs_identifier in sorted(sxs_id_to_conceptrecid):
            f.write("    {0} {1};\n".format(sxs_identifier, sxs_id_to_conceptrecid[sxs_identifier]))
        f.write("}\n")
