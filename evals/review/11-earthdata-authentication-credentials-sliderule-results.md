# Row 11 results: docsearch / conceptual

> Auto-generated. Open this file alongside `11-earthdata-authentication-credentials-sliderule-review.md` —
> verdicts go there, this side is read-only.

**Query:** `earthdata authentication credentials sliderule`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/earthdata.html
  - https://docs.slideruleearth.io/background/NASA-Earthdata.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** earthdata authentication setup

---

## 📚 docsearch results (top 5)

#### r1 — score 0.653

- **url:** https://docs.slideruleearth.io/developer_guide/articles/security_model.html
- **title:** 2026-03-12: Security Model
- **section:** Overview
- **category:** `developer_guide`
- **matched_tokens:** ['authentication', 'credentials', 'sliderule']

**Full text:**

```
SlideRule Earth leverages GitHub authentication and account membership status within the GitHub SlideRuleEarth organization to authorize access to SlideRule services. Credentials are provided by users using a JSON Web Token (JWT) issued by the SlideRule Earth login service ( login.slideruleearth.io ). A userâs JWT contains claims used and verified by SlideRule services to allow access.
```

#### r2 — score 0.566

- **url:** https://docs.slideruleearth.io/developer_guide/articles/private_clusters.html
- **title:** 2026-01-20: Private Clusters
- **section:** SlideRule Authenticator
- **category:** `developer_guide`
- **matched_tokens:** ['authentication', 'credentials', 'sliderule']

**Full text:**

```
The SlideRule Authenticator is an AWS Lambdaâbased authentication service that delegates user authentication to GitHub. User login requests are redirected to GitHubâs authorization endpoint, where credentials are verified by GitHub. Upon successful authentication, GitHub returns an authorization grant that the service exchanges for an access token to establish the userâs identity. The SlideRule Authenticator is available at https://login.slideruleearth.io and exposes the following API endpoints. /auth/github/login : Initiates the OAuth 2.1 authorization code flow for browser-based clients. /auth/github/device : Implements the OAuth 2.0 device authorization flow for CLI and Python clients. /auth/github/pat : Supports authentication using GitHub personal access tokens for automated systems. /auth/refresh : Exchanges a valid refresh token for a new JSON Web Token (JWT). /auth/pem : Returns the public signing key in PEM format. /.well-known/jwks.json : Publishes the public signing keys in JWKS format. /.well-known/openid-configuration : Provides OpenID Connect discovery metadata.
```

#### r3 — score 0.613

- **url:** https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['authentication', 'credentials', 'sliderule']

**Full text:**

```
The second step of obtaining credentials also requires some specialized code, but since most of our datasets are in AWS and authenticated through NASA DAACs, most of the authentication code is generic. But even still, because of this, each raster dataset supported by SlideRule needs to be registered with SlideRule ahead of time and provided in what we call an Asset Directory.
```

#### r4 — score 0.493

- **url:** https://docs.slideruleearth.io/developer_guide/how_tos/amazon_linux_arm_setup.html
- **title:** Setting Up Amazon Linux Development Environment
- **section:** 2-Factor Authentication
- **category:** `developer_guide`
- **matched_tokens:** ['authentication', 'credentials', 'sliderule']

**Full text:**

```
Make sure to setup an initial .aws/credentials file so that it has the sliderule profile access key and secret access key. The credentials file will look something like: [ default ] aws_access_key_id = _ aws_secret_access_key = _ aws_session_token = _ [ sliderule ] aws_access_key_id = _ aws_secret_access_key = _ To populate the default keys and session token, run: aws --profile = sliderule sts get-session-token --serial-number arn:aws:iam:: $account_number :mfa/ $user_name --token-code = $code To login to the AWS Elastic Container Registry, run: aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $account_number .dkr.ecr. $region .amazonaws.com Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.555

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- **title:** Release v5.0.x
- **section:** Breaking Changes
- **category:** `release_notes`
- **matched_tokens:** ['authentication', 'earthdata', 'sliderule']

**Full text:**

```
v5.0.7 - The atl24-s3 asset has been renamed to icesat2-atl24 to reflect that it is now the default asset for ATL24. This will also make the transition from local S3 storage to Earthdata Cloud seamless, as the name will not need to change when that happens. v5.0.3 - The use of the SlideRule Provisioning System has been deprecated. All accounts in the system must be replaced by GitHub accounts. Authentication for private clusters is now handled by the SlideRule Authenticator at https://login.slideruleearth.io. The Python client now supports only two authentication flows: (1) the use of a PAT key from GitHub, and (2) an interactive device-flow login to GitHub Support for .netrc files has been removed The environment variable PS_GITHUB_TOKEN has been renamed to SLIDERULE_GITHUB_TOKEN to remove the âProvisioning Systemâ prefix identifier. The ps_username and ps_password parameters in sliderule.authenticate have been removed. The update_available_servers function can no longer be used to change the number of nodes in a running cluster; it can only be used to initialize the number of nodes in a cluster that is to be deployed and then status the number of nodes that are running. v5.0.3 - The use of the SlideRule Manager has been deprecated.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.289

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Historical Perspective
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 11
- **matched_tokens:** ['earthdata']

**Full text:**

```
The primary distribution architecture
is the Earth Observing system Data and Information system (EOSDIS) with major facilities
at the Distributed Active Archive Centers (DAAC) located across the United States. The
DAACs act as stewards of the Earth observing satellites and field measurement programs and
are responsible for processing, archiving, documenting and distributing data. For the original
ICESat mission and for the ICESat-2 mission the designated DAAC is the National Snow
and Ice Data Center (NSIDC) in Boulder Colorado. NSIDC is the primary DAAC for snow
and ice processes with a particular focus in snow, ice, atmosphere and ocean interactions and
has been operational since 1976. The partnership between the NSIDC team and the ICESat-2 mission has been extremely
successful in data product development and distribution via Earthdata Search. The mecha-
nisms of searching and selecting data repositories in NSIDC are well established and provide
useful tools for data filtering and visualization.
4
```

#### r2 — score 0.340

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['sliderule']

**Full text:**

```
SlideRule runs in Amazon’s
cloud under GSFC Code 606’s Science Managed Cloud Environment (SMCE) and has access
to NASA’s Cumulus data archives. SlideRule provides web-services for researchers and other
data systems to generate custom data products in real-time using processing parameters
supplied at the time of the request. Scientists access SlideRule directly from any Python environment using a provided client;
a Javascript client is also provided for integrating SlideRule into other web-based systems. SlideRule is currently being used by glacier, snow, and bathymetry researchers to process
tens of thousands of ICESat-2 granules each month. SlideRule also supports private instantiations of its infrastructure that require authen-
ticated access. These instantiations, called private clusters, are managed by the SlideRule
Provisioning System at https://ps.slideruleearth.io. Private clusters are used for execut-
ing large processing runs, providing dedicated compute resources, and running proprietary
algorithms.
42
```

#### r3 — score 0.326

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 52
- **matched_tokens:** ['sliderule']

**Full text:**

```
Both compute and storage services in AWS are available through the SlideRule SMCE
account and will be used on an as-needed basis.
The following data resources will be stored in the SlideRule SMCE account S3 bucket:
• Labeled photon data
• Global bathymetry mask
• Refractive index
• Uncertainty lookup table
The following Docker images will be stored in the SlideRule SMCE account container registry:
• SlideRule server, intelligent load balancer, and monitor
• Python runtime environment
The following applications will be hosted in the SlideRule SMCE S3 bucket:
• Graphic web interface
• Documentation webpage
45
```

#### r4 — score 0.275

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['sliderule']

**Full text:**

```
ATL24.g The gold standard product will be generated by a private instantiation of SlideRule
running in the AWS US-West-2 data center. The granules will initially exist in SlideRule’s
private S3 bucket prior to transfer to NSIDC. Moving forward, the ATL24.g option will
exist in SlideRule as a client facing product with subsetting capabilities. ATL24.s and ATL24.p Web-services will be provided by the public instantiation of Slid-
eRule. Includes interfacing to the client, and reading the ATL24 granules from S3. Graphical web interface The interface will be hosted in AWS S3 and served by Amazon’s
CloudFront at https://client.slieruleearth.io
The gold standard ATL24 product will be generated on a per-granule basis using SlideRule
and following the prescribed nearshore/coastal bathymetry mask to coordinate and execute
the full suite of contributing classification algorithms. This gold standard data product will
be a global resource using the most current algorithmic workflow and will be available to
users via sub-setting. Ultimately, the ATL24.g product provides the most robust algorithm
parameterization for global applications but does not provide the option for users to adjust
the input parameters. Figure 1 shows the execution flow from an incoming ATL24.g request
all the way to the output of a gold standard h5 granule.
3.3 ATL24 ATBD Sections
ATL24 primary input is ATL03, using the geolocated photon point cloud to determine
classifications of sea surface and seafloor.
```

#### r5 — score 0.282

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['sliderule']

**Full text:**

```
6.2 Deployment Environment
ATL24 will use SlideRule to provide the compute infrastructure for all four project objectives:
• The atl24g gold standard product will be generated by a private instantiation of SlideRule
running in the AWS us-west-2 data center. The granules will initially exist in SlideRule’s
private S3 bucket prior to being transferred to the NSIDC.
• The atl24s and atl24p web services will be provided by the public instantiation of
SlideRule that runs in the AWS us-west-2 data center.
• The graphical web interface will be hosted in AWS S3 and served by Amazon’s CloudFront
at https://client.slideruleearth.io. Figure 10: Top Level SlideRule Architecture
SlideRule Native Runtime
The native runtime environment for SlideRule services is an extended Lua interpreter
where each request maps to a Lua script that instantiates custom classes written in C++ to
perform the processing needed to fulfill the request. The runtime is designed to quickly complete requests and return results back to users in
near real-time. To that end, all requests are expected to complete within 10 minutes, and
results are streamed back to the user as soon as they are available, over a TCP/IP connection
that remains open for the entire time of the request. (It is typical for the users that request
many granules to be processed at once to start receiving results for parts of their request
that have finished before other parts of their request have even begun to be processed).
```

---

