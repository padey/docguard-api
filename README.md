# WORK IN PROGRESS
- Python API for https://www.docguard.io/

## Current Status
- Search Function works
- Submit Function in progress
- curlify is used right now for debugging, will be deleted

# HowTo
### Searching a Hash Value
python3 docguard2.py -search -api-key "YOUR_API_KEY" -hash "2063ca2301695cb53c6acfbd614da6a2e5ed691cf712491fb19ac25b4eaac481"

### Submitting a File
python3 docguard2.py -submit -api-key "YOUR_API_KEY" -file "lololala.ps1" [OPTINAL: -password "infected" -public "true/false"]
