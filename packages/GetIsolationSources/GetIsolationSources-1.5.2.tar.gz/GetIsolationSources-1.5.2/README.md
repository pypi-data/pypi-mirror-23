**GetIsolationSources** is a small command line utility that, given fasta files containing GenBank IDs in sequence descriptions, generates a per sequence list of isolation sources and their distribution (i.e. number of sequences per isolation source).

It searches for IDs using regular expressions in accordance with [NCBI specifications](http://www.ncbi.nlm.nih.gov/Sequin/acc.html), so the format of description strings does not matter.

To obtain needed information it uses automated Entrez queries, so you need a working Internet connection to perform the analysis. Queries are made in accordance with NCBI load-balance regulations, therefore processing several thousand records may take several minutes or even longer.

It is distributed as a source code supporting python setup tools.

**GetIsolationSources uses [BioPython](http://biopython.org/wiki/Main_Page).** So if you're using source code distribution, the latest version of [BioPython](http://biopython.org/wiki/Main_Page) should be installed.

[**Downaloads**](https://github.com/allista/GetIsolationSource/releases)

***

**GetIsolationSources** by [**Allis Tauri**](https://github.com/allista) is licensed under the [MIT](https://github.com/allista/GetIsolationSources/blob/master/LICENSE) license.