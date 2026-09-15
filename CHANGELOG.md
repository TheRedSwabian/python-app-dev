# CHANGELOG


## v1.0.0 (2026-09-15)

### Bug Fixes

- App directory is added by default to path
  ([`562372f`](https://github.com/TheRedSwabian/python-app-dev/commit/562372fa69aeb9ea8c678d9114a19697d82377b0))

- Application path is not in required paths
  ([`d1927ed`](https://github.com/TheRedSwabian/python-app-dev/commit/d1927edc78ec0932c6310fa14cbc0434d9feecdb))

- Base json config does not use alias
  ([`ccbd402`](https://github.com/TheRedSwabian/python-app-dev/commit/ccbd402551e61522dfbb97a53101b0e93963120d))

- Class name is not consistent
  ([`dc17cf7`](https://github.com/TheRedSwabian/python-app-dev/commit/dc17cf7c606d088d2ad8f447f235fd066574ed44))

- Directory not added if the binary is in the app root
  ([`9c5858a`](https://github.com/TheRedSwabian/python-app-dev/commit/9c5858a6c208c5fda7b1b200c8aec3aaad1cd80b))

- Exception is thrown if file is not found
  ([`4b44d10`](https://github.com/TheRedSwabian/python-app-dev/commit/4b44d10d7f2d5eae9fa37768d626c216f7ac7848))

- Install scoop app class violates the single responsibility principle
  ([`641cde0`](https://github.com/TheRedSwabian/python-app-dev/commit/641cde097029f3b11451c24e0802aebd7035738a))

- Manifest file path not shown if parsing failed
  ([`45e792a`](https://github.com/TheRedSwabian/python-app-dev/commit/45e792a7e278a852d14cbcc6c79530df60f3b71e))

- Optional arguments type is wrong
  ([`9687f6a`](https://github.com/TheRedSwabian/python-app-dev/commit/9687f6a634046d16aee3d4f3b738b3ff31ef1c6a))

- Optional types are not optional arguments
  ([`5a64123`](https://github.com/TheRedSwabian/python-app-dev/commit/5a64123f8f049d90788e566892c226e2ddd4b68f))

- Powershell $PSHOME variable is not expanded
  ([`99f564e`](https://github.com/TheRedSwabian/python-app-dev/commit/99f564ea42f52516f352978917432ad2c7467934))

- Powershell module path is empty
  ([`e42bf78`](https://github.com/TheRedSwabian/python-app-dev/commit/e42bf7897ce49d7cf5750e554810990e43474724))

- Quote python_version in pypeline.yaml
  ([`ed8dfe4`](https://github.com/TheRedSwabian/python-app-dev/commit/ed8dfe484bc7391ae415c5b2aff45c60b60a99c8))

- Report stderr as None when it is merged into stdout
  ([`0a63612`](https://github.com/TheRedSwabian/python-app-dev/commit/0a63612b23014a644be801f5317600a0cc3a6e1a))

- Scoop install 'Get-FileHash' fails
  ([`6fa3592`](https://github.com/TheRedSwabian/python-app-dev/commit/6fa3592c32760f7b8a6d63026b2a1f4cf65ccdd8))

- Scoop wrapper finds apps twice
  ([`4b704ad`](https://github.com/TheRedSwabian/python-app-dev/commit/4b704ad615cfb91cbf51748be46b9a15a7e85585))

- Scoop.cmd ignores the powershell proxy settings
  ([`44daef6`](https://github.com/TheRedSwabian/python-app-dev/commit/44daef67ee734b94b2f0f8bfe1afd13c43ecc7df))

- Semantic versioning can not build package with poetry
  ([`92d65d2`](https://github.com/TheRedSwabian/python-app-dev/commit/92d65d21900beb1301e408cb696338aefa3ada9e))

- Single env path is not parsed properly
  ([`6a4bb3e`](https://github.com/TheRedSwabian/python-app-dev/commit/6a4bb3e948fc2730ccd3f2ff84023554cb63ca59))

- Wrong scoop executable is returned
  ([`3867df0`](https://github.com/TheRedSwabian/python-app-dev/commit/3867df07643dcde3e1ca484091e70aa458a1630d))

- Wrong scoop executable is returned
  ([`f1a6a6a`](https://github.com/TheRedSwabian/python-app-dev/commit/f1a6a6ae598e7cc55a926e704e7870fe298c4100))

### Documentation

- Move information from internals to features
  ([`97231d6`](https://github.com/TheRedSwabian/python-app-dev/commit/97231d6d1a2c6029171cee4a69f4c5ec830727db))

- Remove username from project title
  ([`991cf61`](https://github.com/TheRedSwabian/python-app-dev/commit/991cf61ab45533a1d31e356a9d6c2e02c276ff17))

### Features

- Add base config mixin class
  ([`25293fe`](https://github.com/TheRedSwabian/python-app-dev/commit/25293fe661d7a7674c2f3c40fbb9e44f0de1f438))

- Add compile commands parsing
  ([`237adac`](https://github.com/TheRedSwabian/python-app-dev/commit/237adac9b05cf53efa7181dd2b172a97877bc46e))

- Add configs merge
  ([`f2e77eb`](https://github.com/TheRedSwabian/python-app-dev/commit/f2e77eb2a73ca5ca46aa94d998fb45c906c2c558))

- Add custom configuration for steps
  ([`5c056d1`](https://github.com/TheRedSwabian/python-app-dev/commit/5c056d10f133240a86a8bcaa6dadd73f08378b4f))

- Add dry_run option for executing runnables
  ([`927a662`](https://github.com/TheRedSwabian/python-app-dev/commit/927a662dbb61a5287587677dacd3ef51d1df641a))

- Add env setup sh
  ([`e6301bc`](https://github.com/TheRedSwabian/python-app-dev/commit/e6301bc8acc9111e1d2fb57f431762707ce38551))

- Add environment setup scripts generator
  ([`a7d096b`](https://github.com/TheRedSwabian/python-app-dev/commit/a7d096b8c1fd564f29d762b3307f567863001bae))

- Add find helper methods
  ([`6b487de`](https://github.com/TheRedSwabian/python-app-dev/commit/6b487deb755650c6e9e94e317e4e9b16163478f3))

- Add log to file context manager
  ([`a333716`](https://github.com/TheRedSwabian/python-app-dev/commit/a3337164ce358de00f7dec9c5f67caac5118b814))

- Add option to force runnable execution
  ([`06fde72`](https://github.com/TheRedSwabian/python-app-dev/commit/06fde72d02d4f040bd1c756e9e6f33484a082c2c))

- Add runnable config dependency
  ([`057155b`](https://github.com/TheRedSwabian/python-app-dev/commit/057155bab1d584a28f1cbfbe21ee6cb9acaf88cd))

- Add runnable id to track dependencies
  ([`8106975`](https://github.com/TheRedSwabian/python-app-dev/commit/810697581c2739ea39baa6527d3d3624e58ca6e3))

- Add support for python 3.10+ optional types
  ([`40e307f`](https://github.com/TheRedSwabian/python-app-dev/commit/40e307f3d4ce9bdebf00f11be0ac8c463f478350))

- Add support for scoop apps environment variables
  ([`7b63034`](https://github.com/TheRedSwabian/python-app-dev/commit/7b6303458c527f86aa980d1e86faf1f6c30b18e3))

- Add timeout support for subprocess execution
  ([`01d76d7`](https://github.com/TheRedSwabian/python-app-dev/commit/01d76d7c2da946b3850fd672d96e00c44d7e331d))

- Allow hiding code location in console log output
  ([`4f5fa15`](https://github.com/TheRedSwabian/python-app-dev/commit/4f5fa15503727038465f32069574c93e51a1103b))

setup_logger now takes show_code_location. It is off by default, which keeps the console output of
  every existing caller unchanged.

The log file is not affected. A log file is read for debugging, so it keeps the code location in all
  cases.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

- Capture subprocess output
  ([`de4960c`](https://github.com/TheRedSwabian/python-app-dev/commit/de4960cef867b3978942216db227cfd6a1319439))

- Check if scoop is installed in user home
  ([`007cf6a`](https://github.com/TheRedSwabian/python-app-dev/commit/007cf6a6d349483a6cbeb170168b840a4fdc5acb))

- Clear log file
  ([`76d1e08`](https://github.com/TheRedSwabian/python-app-dev/commit/76d1e080d2879a71142adb1636cc1ea2031c0022))

- Data register supports dynamically loaded classes
  ([`b4329ef`](https://github.com/TheRedSwabian/python-app-dev/commit/b4329ef5c9b330a7010aabbccd008600df91ccdb))

- Execute runnable if new input files are detected
  ([`eaa2dbd`](https://github.com/TheRedSwabian/python-app-dev/commit/eaa2dbd8699bd998be905362b48d8293691baac1))

- Execute runnables without dependency management
  ([`04c8799`](https://github.com/TheRedSwabian/python-app-dev/commit/04c879935054911426886adaf9dc8f6cfcb39716))

- Executor support for always run runnables
  ([`8015b85`](https://github.com/TheRedSwabian/python-app-dev/commit/8015b858d457691978c6d161a990ae492fa5015c))

- Make subprocess executor robust against invalid encoding and capturing output while printing
  ([`6a0d5f0`](https://github.com/TheRedSwabian/python-app-dev/commit/6a0d5f01db8f2e19ecca837084a31edfe523348b))

- Make the pipeline loader generic
  ([`b516274`](https://github.com/TheRedSwabian/python-app-dev/commit/b5162749433af13f14057aa278b5cbcc2df36142))

- Make view class generic
  ([`3a641b7`](https://github.com/TheRedSwabian/python-app-dev/commit/3a641b74839639351661d8a230c46662ad56e7f0))

- Provide generic data registry
  ([`a6806e2`](https://github.com/TheRedSwabian/python-app-dev/commit/a6806e24639d44530825e72ef4074c4b08e806a2))

- Read env paths for scoop tools
  ([`a253165`](https://github.com/TheRedSwabian/python-app-dev/commit/a253165356672764d80288664f5ff57dbdbad12a))

- Rename module to py-app-dev
  ([`206b8ac`](https://github.com/TheRedSwabian/python-app-dev/commit/206b8ac6c5e43cb36fdf4172fe7b14c782185329))

- Subprocess print stdout in realtime
  ([`78dc4ac`](https://github.com/TheRedSwabian/python-app-dev/commit/78dc4ac02f9a1ff85cd45c697f2538757994683a))

- Support callbacks with any number of args
  ([`5304ca6`](https://github.com/TheRedSwabian/python-app-dev/commit/5304ca6f94e270792a2c742dfb23f7d20a5abcd0))

- Support case insensitive scoop manifest data
  ([`86d56a5`](https://github.com/TheRedSwabian/python-app-dev/commit/86d56a5167efa2699b3874cee8f49a38153ec982))

- Support config with location tracing
  ([`ea71583`](https://github.com/TheRedSwabian/python-app-dev/commit/ea71583de05425b0744c6ae58d4dbef2a75a81dc))

- Support deserialize method
  ([`17e063d`](https://github.com/TheRedSwabian/python-app-dev/commit/17e063ddb39a94eb1d248403239d299511563d88))

- Support directories as dependencies
  ([`da98390`](https://github.com/TheRedSwabian/python-app-dev/commit/da983901e3c4d4b354ab7c57f61859962391cef7))

- Support lists for registering arguments
  ([`64e477f`](https://github.com/TheRedSwabian/python-app-dev/commit/64e477f27ff65e25fc46fa0647a1c2096892af14))

- Support registering arguments with action
  ([`0fc0261`](https://github.com/TheRedSwabian/python-app-dev/commit/0fc02617712afdacd63b622bf69114542009d64e))

- Support version for scoop apps
  ([`e2484ed`](https://github.com/TheRedSwabian/python-app-dev/commit/e2484ed58b00aced1e02ecb4d808a35ec19b40d3))

- Suprocess executor can override the env
  ([`c51a413`](https://github.com/TheRedSwabian/python-app-dev/commit/c51a4138f415ee7d4342dea4c4292556c32ee188))

- Update PipelineConfig to support a Union of List and OrderedDict
  ([`bb919d6`](https://github.com/TheRedSwabian/python-app-dev/commit/bb919d6462db4d94433b33c02489b11ce418c5d3))

- Use shell for subprocess executor
  ([`baced78`](https://github.com/TheRedSwabian/python-app-dev/commit/baced787c081f746fd21abf007d76a8cfdca0481))

- **config**: Support merging named elements
  ([`4915d4a`](https://github.com/TheRedSwabian/python-app-dev/commit/4915d4a7ff1bb9c9f4bada7386ccaf0832158bad))
