# WORK IN PROGRESS
 may crash.. may not.

* Python API for <https://www.docguard.io/>

There are two functions.


1. Search for HASH
2. Submit for Analyze
3. Each Request will be saved under the FileSha256hash.json

# HowTo

### Searching a Hash Value

`python3 docguard.py -search -api-key "YOUR_API_KEY" -hash "30090f902cead484616d3a8041f0e18242b22566aeea28160865bfe2227f72f6"`


> Output: Verdict: Malicious FileName: eicar-adobe-acrobat-javascript-alert.pdf
>
> FileType: PDF File
>
> FileSha256Hash: 948ee1d9e0df1dc678f420239fddce99e0268978e65502d0ec31615b0a57b29a
>
> Response saved as: 948ee1d9e0df1dc678f420239fddce99e0268978e65502d0ec31615b0a57b29a.json

### Submitting a File

`python3 docguard.py -submit -api-key "YOUR_API_KEY" -file "testfiles/eicar-adobe-acrobat-javascript-alert.pdf" (optinal arguments: -password "file_password" & -public = "true/false", default: false)`


> Verdict: Malicious FileName: eicar-adobe-acrobat-javascript-alert.pdf
>
> FileType: PDF File
>
> FileSha256Hash: 948ee1d9e0df1dc678f420239fddce99e0268978e65502d0ec31615b0a57b29a
>
> Response saved as: 948ee1d9e0df1dc678f420239fddce99e0268978e65502d0ec31615b0a57b29a.json


